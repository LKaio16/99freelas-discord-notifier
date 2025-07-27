import discord
from discord import app_commands
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import asyncio
import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente
load_dotenv('config.env')

TOKEN = os.getenv('DISCORD_TOKEN')
CHANNEL_ID = 1399037898233479219  # Canal padrão

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

avisados = set()
pausado = False
canais_ativos = {CHANNEL_ID}  # Set com IDs dos canais ativos

def get_html_selenium(url):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--window-size=1920,1080')
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get(url)
    html = driver.page_source
    driver.quit()
    return html

@tree.command(name="pause", description="Pausa o monitoramento de projetos")
async def pause_command(interaction: discord.Interaction):
    global pausado
    pausado = True
    await interaction.response.send_message("⏸️ Monitoramento pausado! O bot não irá mais verificar novos projetos.")

@tree.command(name="resume", description="Retoma o monitoramento de projetos")
async def resume_command(interaction: discord.Interaction):
    global pausado
    pausado = False
    await interaction.response.send_message("▶️ Monitoramento retomado! O bot voltará a verificar novos projetos.")

@tree.command(name="setchannel", description="Define o canal onde o bot enviará notificações de novos projetos")
async def setchannel_command(interaction: discord.Interaction):
    global canais_ativos
    canal_id = interaction.channel_id
    canais_ativos.add(canal_id)
    await interaction.response.send_message(f"✅ Canal <#{canal_id}> configurado para receber notificações de novos projetos!")

@tree.command(name="removechannel", description="Remove o canal atual da lista de notificações")
async def removechannel_command(interaction: discord.Interaction):
    global canais_ativos
    canal_id = interaction.channel_id
    if canal_id in canais_ativos:
        canais_ativos.remove(canal_id)
        await interaction.response.send_message(f"❌ Canal <#{canal_id}> removido da lista de notificações!")
    else:
        await interaction.response.send_message(f"⚠️ Este canal não estava na lista de notificações.")

@tree.command(name="listchannels", description="Lista todos os canais configurados para receber notificações")
async def listchannels_command(interaction: discord.Interaction):
    if not canais_ativos:
        await interaction.response.send_message("📋 Nenhum canal configurado para notificações.")
        return
    
    canais_texto = []
    for canal_id in canais_ativos:
        canal = client.get_channel(canal_id)
        if canal:
            canais_texto.append(f"• <#{canal_id}> ({canal.name})")
        else:
            canais_texto.append(f"• <#{canal_id}> (Canal não encontrado)")
    
    embed = discord.Embed(
        title="📋 Canais Configurados",
        description="\n".join(canais_texto),
        color=0x00bfff
    )
    await interaction.response.send_message(embed=embed)

async def checar_projetos():
    url = "https://www.99freelas.com.br/projects?order=mais-recentes&categoria=web-mobile-e-software"
    primeira_analise = True
    while True:
        if not pausado:
            try:
                print("Consultando página de projetos (Selenium)...")
                html = get_html_selenium(url)
                with open('pagina.html', 'w', encoding='utf-8') as f:
                    f.write(html)
                soup = BeautifulSoup(html, 'html.parser')
                projetos = soup.select('li.result-item')

                print(f"Projetos encontrados: {len(projetos)}")
                novos = []
                for projeto in projetos:
                    titulo_tag = projeto.select_one('h1.title a')
                    if not titulo_tag:
                        continue
                    titulo = titulo_tag.text.strip()
                    link = titulo_tag['href']
                    descricao_tag = projeto.select_one('div.description')
                    descricao = ''
                    if descricao_tag:
                        # Remove o texto dos botões 'Expandir' e 'Esconder'
                        for btn in descricao_tag.select('.read-more, .less-link, .read-less, .more-link, .details'):
                            btn.decompose()
                        descricao = descricao_tag.get_text(separator='\n', strip=True)
                    # Limpa tags <br> e espaços extras
                    descricao = descricao.replace('\r', '').replace('\n', ' ').replace('  ', ' ')
                    # Limita a descrição a 200 caracteres e adiciona reticências se necessário
                    max_desc = 200
                    if len(descricao) > max_desc:
                        descricao = descricao[:max_desc-3].rstrip() + '...'
                    print(f"Projeto encontrado: {titulo} ({link})")
                    if titulo not in avisados:
                        avisados.add(titulo)
                        novos.append({
                            'titulo': titulo,
                            'link': link,
                            'descricao': descricao
                        })

                if primeira_analise:
                    print(f"Primeira análise: {len(projetos)} projetos encontrados. Nenhuma mensagem enviada.")
                    primeira_analise = False
                elif novos:
                    print(f"{len(novos)} projeto(s) novo(s) encontrado(s):")
                    for projeto in novos:
                        print(f"- {projeto['titulo']} ({projeto['link']})")
                        embed = discord.Embed(
                            title=projeto['titulo'],
                            url=f"https://www.99freelas.com.br{projeto['link']}",
                            description=projeto['descricao'],
                            color=0x00bfff
                        )
                        embed.set_footer(text="99Freelas")
                        # Adiciona a imagem de perfil do bot à direita
                        if client.user and client.user.avatar:
                            embed.set_thumbnail(url=client.user.avatar.url)
                        
                        # Envia para todos os canais configurados
                        for canal_id in canais_ativos:
                            try:
                                canal = client.get_channel(canal_id)
                                if canal:
                                    await canal.send(embed=embed)
                            except Exception as e:
                                print(f"Erro ao enviar mensagem para canal {canal_id}: {e}")
                else:
                    print("Nenhum projeto novo encontrado.")
            except Exception as e:
                print(f"Erro ao checar projetos: {e}")
        else:
            print("Monitoramento pausado...")
        await asyncio.sleep(100)  # Espera 100 segundos

@client.event
async def on_ready():
    print(f'Logado como {client.user}')
    await tree.sync()
    client.loop.create_task(checar_projetos())

if __name__ == "__main__":
    client.run(TOKEN) 