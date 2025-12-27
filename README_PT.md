# GithubATS

<div align="center">
  <img src="logo.png" alt="GithubATS Logo" width="200"/>
  <p><strong>Gerador de Currículo Inteligente</strong></p>
  <p>Um CLI Python gamificado que gera currículos ATS-friendly a partir dos seus repositórios GitHub usando análise inteligente de LLM.</p>
  
  <p>
    <a href="#funcionalidades">Funcionalidades</a> •
    <a href="#instalação">Instalação</a> •
    <a href="#uso">Uso</a> •
    <a href="#gamificação">Gamificação</a> •
    <a href="#temas">Temas</a>
  </p>

  [![Licença: MIT](https://img.shields.io/badge/Licença-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
  [![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://python.org)
</div>

---

## ✨ Funcionalidades

O GithubATS transforma seu perfil GitHub em um currículo profissional e otimizado para ATS, analisando seus repositórios com Modelos de Linguagem Grandes (LLMs).

### Capacidades Principais
- **Análise Inteligente**: Análise LLM do conteúdo de repositórios, tecnologias e complexidade
- **Otimização ATS**: Gera currículos formatados especificamente para passar por Applicant Tracking Systems
- **Múltiplos Formatos**: Exporte para PDF, HTML ou Markdown
- **Sistema Gamificado**: Ganhe pontos, níveis e conquistas baseados na sua atividade de codificação
- **Temas Visuais**: Escolha entre os estilos visuais Claro, Escuro e Cyberpunk
- **Métricas Automáticas**: Extração automática de stars, forks e estatísticas de linguagens
- **Sistema de Emblemas**: Colete badges e conquistas para mostrar suas habilidades

## 📦 Instalação

### Pré-requisitos
- Python 3.8 ou superior
- Token Pessoal de Acesso do GitHub
- Chave de API do OpenRouter (ou endpoint compatível com OpenAI)

### Instalar via pip
bash
pip install githubats


### Instalação Manual
bash
# Clone o repositório
git clone https://github.com/seu-usuario/GithubATS.git
cd GithubATS

# Instale as dependências
pip install -r requirements.txt

# Crie o arquivo de ambiente
cp .env.example .env


## ⚙️ Configuração

1. **Token GitHub**: Gere em [Configurações do GitHub](https://github.com/settings/tokens)
   - Escopos necessários: `public_repo` (público) ou `repo` (privado)

2. **Chave API LLM**: Obtenha uma chave de API da [OpenRouter](https://openrouter.ai/) ou qualquer provedor compatível com OpenAI

3. **Variáveis de Ambiente**: Configure seu arquivo `.env`:
bash
GITHUB_TOKEN="ghp_seu_token_aqui"
OPENROUTER_API_KEY="sk-or-v1-sua_chave_aqui"


## 🚀 Uso

### Comandos Básicos

bash
# Gerar currículo básico
python app.py generate

# Gerar currículo gamificado tema cyberpunk
python app.py generate --theme cyberpunk --gamified --output meu-cv.pdf

# Gerar em formato HTML
python app.py generate --format html --output curriculo.html

# Ver estatísticas
python app.py stats

# Mostrar ajuda
python app.py --help


### Referência de Opções

| Flag | Valores | Descrição |
|------|--------|-------------|
| `--theme` | `light`, `dark`, `cyberpunk` | Tema visual |
| `--format` | `pdf`, `html`, `markdown` | Formato de saída |
| `--gamified` | - | Ativar recursos gamificados |
| `--output` | `arquivo` | Caminho do arquivo de saída |

## 🎮 Gamificação

O sistema gamificado adiciona uma camada divertida à construção de currículos:

- **Pontos de Experiência (XP)**: Ganho ao analisar repositórios e complexidade
- **Níveis**: Progrida de Iniciante para Mestre do Código
- **Conquistas**: Desbloqueie badges por marcos (ex: "Primeiro Repo Analisado", "10k+ Linhas de Código")

## 🎨 Temas

| Tema | Descrição |
|-------|-------------|
| **Claro** | Fundo branco limpo e profissional |
| **Escuro** | Modo escuro moderno com cores sutis |
| **Cyberpunk** | Estética neon futurista com vibe de terminal |

## 🔧 Desenvolvimento

bash
# Executar testes
pytest

# Formatar código
black .
flake8

# Construir pacote
python setup.py sdist bdist_wheel


## 📝 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 🙏 Agradecimentos
- Construído com Python e integração LLM
- Gamificação inspirada em aplicativos de produtividade para desenvolvedores
- Otimização ATS baseada em feedback de recrutadores