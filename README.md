# 🤖 Bot 99Freelas Notifier

<div align="center">
  <img src="https://www.99freelas.com.br/assets/images/logo-99freelas.png" alt="99Freelas Logo" width="200"/>
  
  [![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
  [![Discord](https://img.shields.io/badge/Discord-Bot-7289DA.svg)](https://discord.com/)
  [![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
</div>

## 📋 Descrição

Bot automatizado para o Discord que monitora a página de projetos do [99Freelas](https://www.99freelas.com.br) e notifica automaticamente quando novos projetos são publicados na categoria **Web, Mobile & Software**.

### ✨ Funcionalidades

- 🔍 **Monitoramento Automático**: Verifica novos projetos a cada 100 segundos
- 📢 **Notificações Inteligentes**: Envia embeds personalizados no Discord
- ⏸️ **Controle Total**: Comandos para pausar/retomar o monitoramento
- 📍 **Múltiplos Canais**: Configure vários canais para receber notificações
- 🛡️ **Proteção Anti-Spam**: Não envia o mesmo projeto duas vezes
- 🎨 **Design Profissional**: Embeds com cores, imagens e formatação limpa

## 🚀 Instalação

### Pré-requisitos

- Python 3.8 ou superior
- Google Chrome instalado
- Bot do Discord configurado

### Passo a Passo

1. **Clone o repositório**
   ```bash
   git clone https://github.com/seu-usuario/bot-99freelas.git
   cd bot-99freelas
   ```

2. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure o token do bot**
   - Edite o arquivo `config.env`
   - Substitua `SEU_TOKEN_AQUI` pelo token do seu bot
   ```env
   DISCORD_TOKEN=seu_token_do_bot_aqui
   ```

4. **Execute o bot**
   ```bash
   python bot_99freelas.py
   ```

## 🤖 Adicionar o Bot ao Discord

Clique no link abaixo para adicionar o bot ao seu servidor:

**[🔗 Adicionar Bot ao Discord](https://discord.com/oauth2/authorize?client_id=1399036818262851624&permissions=34359838720&integration_type=0&scope=bot)**

### Permissões Necessárias

- ✅ Enviar Mensagens
- ✅ Usar Comandos de Aplicação
- ✅ Ler Mensagens
- ✅ Gerenciar Mensagens

## 📝 Comandos Disponíveis

| Comando | Descrição | Exemplo |
|---------|-----------|---------|
| `/setchannel` | Configura o canal atual para receber notificações | `/setchannel` |
| `/removechannel` | Remove o canal atual da lista de notificações | `/removechannel` |
| `/listchannels` | Lista todos os canais configurados | `/listchannels` |
| `/pause` | Pausa o monitoramento de projetos | `/pause` |
| `/resume` | Retoma o monitoramento de projetos | `/resume` |

## ⚙️ Configuração

### Configurar Canais

1. **Adicionar canal:**
   - Vá para o canal desejado
   - Digite `/setchannel`
   - O bot confirmará a configuração

2. **Remover canal:**
   - Vá para o canal que deseja remover
   - Digite `/removechannel`
   - O bot removerá da lista

3. **Ver canais configurados:**
   - Digite `/listchannels` em qualquer lugar
   - O bot mostrará todos os canais ativos

### Controle de Monitoramento

- **Pausar:** `/pause` - Para de verificar novos projetos
- **Retomar:** `/resume` - Volta a verificar novos projetos

## 📊 Como Funciona

1. **Primeira Execução**: O bot analisa todos os projetos atuais sem enviar notificações
2. **Monitoramento Contínuo**: Verifica novos projetos a cada 100 segundos
3. **Detecção Inteligente**: Compara com projetos já notificados
4. **Notificação Automática**: Envia embed personalizado para todos os canais configurados

## 🎨 Exemplo de Notificação

```
┌─────────────────────────────────────┐
│ 🆕 Desenvolvimento de App Mobile    │
│                                     │
│ Descrição do projeto: Olá! Estou   │
│ em busca de um desenvolvedor...     │
│                                     │
│ 🔗 Ver projeto no 99Freelas         │
│                                     │
│ 99Freelas                          │
└─────────────────────────────────────┘
```

## 🛠️ Tecnologias Utilizadas

- **Python 3.8+** - Linguagem principal
- **Discord.py** - API do Discord
- **Selenium** - Web scraping automatizado
- **BeautifulSoup4** - Parsing HTML
- **python-dotenv** - Gerenciamento de variáveis de ambiente

## 📁 Estrutura do Projeto

```
bot-99freelas/
├── bot_99freelas.py      # Código principal do bot
├── config.env            # Configurações (token, etc.)
├── requirements.txt      # Dependências Python
├── README.md            # Este arquivo
└── pagina.html          # HTML da página (gerado automaticamente)
```

## 🔧 Personalização

### Alterar Intervalo de Verificação

Edite a linha no arquivo `bot_99freelas.py`:
```python
await asyncio.sleep(100)  # 100 segundos = ~1.6 minutos
```

### Alterar Categoria de Projetos

Edite a URL no arquivo `bot_99freelas.py`:
```python
url = "https://www.99freelas.com.br/projects?order=mais-recentes&categoria=web-mobile-e-software"
```

## 🐛 Solução de Problemas

### Bot não encontra projetos
- Verifique se o Chrome está instalado
- Confirme se a internet está funcionando
- Verifique se o site 99Freelas está acessível

### Erro de permissão
- Certifique-se de que o bot tem permissão para enviar mensagens no canal
- Verifique se o bot foi adicionado corretamente ao servidor

### Token inválido
- Confirme se o token no `config.env` está correto
- Verifique se o bot está ativo no Discord Developer Portal

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 🤝 Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para:

1. Fazer um fork do projeto
2. Criar uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abrir um Pull Request

## 📞 Suporte

Se você encontrar algum problema ou tiver dúvidas:

- Abra uma [issue](https://github.com/seu-usuario/bot-99freelas/issues)
- Entre em contato através do Discord (lkaio16)
- Verifique a [documentação do 99Freelas](https://www.99freelas.com.br)

---

<div align="center">
  <p>Feito com ❤️ para a comunidade de freelancers</p>
  <p>Powered by <a href="https://www.99freelas.com.br">99Freelas</a></p>
</div> 