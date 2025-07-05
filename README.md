# GitHub ATS Resume Generator 🚀

Um CLI Python divertido e gamificado que gera currículos ATS-friendly a partir dos seus repositórios GitHub usando LLM para análise inteligente!

## ✨ Funcionalidades

- 🤖 **Análise inteligente** de repositórios com LLM (OpenRouter + modelos opensource)
- 📄 **Múltiplos formatos** de saída (PDF, HTML, Markdown)
- 🎮 **Sistema gamificado** com pontuação, níveis e conquistas
- 🎨 **3 temas visuais** (Light, Dark, Cyberpunk)
- 📊 **Métricas automáticas** (stars, forks, linguagens, seguidores)
- 🏆 **Sistema de badges** e conquistas
- 🎲 **Easter eggs** e citações motivacionais
- ⚡ **Otimizado para ATS** (Applicant Tracking Systems)

## 🚀 Instalação Rápida

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/GithubATS.git
cd GithubATS

# Instale as dependências
pip install -r requirements.txt

# Configure as variáveis de ambiente
cp .env.example .env
# Edite o arquivo .env com seus tokens
```

## 🔧 Configuração Detalhada

### 1. Token do GitHub
Crie um token em: https://github.com/settings/tokens
- Selecione escopo: `public_repo` (para repos públicos) ou `repo` (para privados)

### 2. Variáveis de Ambiente
```bash
# Método 1: Arquivo .env (recomendado)
cp .env.example .env
# Edite o arquivo .env

# Método 2: Export direto
export GITHUB_TOKEN="ghp_seu_token_aqui"
export OPENROUTER_API_KEY="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"
```

### 3. Teste a Configuração
```bash
python example.py
```

## 📖 Uso Completo

### Comandos Principais

```bash
# Gerar currículo básico (PDF)
python app.py generate

# Currículo gamificado tema cyberpunk
python app.py generate --theme cyberpunk --gamified --output meu-cv.pdf

# Gerar em HTML
python app.py generate --format html --output curriculo.html

# Ver estatísticas detalhadas
python app.py stats

# Ajuda completa
python app.py --help
```

### Opções Disponíveis

| Opção | Valores | Descrição |
|-------|---------|-----------|
| `--theme` | `light`, `dark`, `cyberpunk` | Tema visual do currículo |
| `--format` | `pdf`, `html`, `markdown` | Formato de saída |
| `--gamified` | - | Ativa modo gamificado |
| `--output` | `arquivo.ext` | Nome do arquivo de saída |
| `--token` | `token` | Token GitHub (ou use variável de ambiente) |

## 🎮 Sistema de Gamificação

### 📊 Pontuação
- ⭐ **Stars**: 10 pontos cada
- 🍴 **Forks**: 5 pontos cada
- 📦 **Repositórios**: 2 pontos cada
- 💻 **Linguagens**: 15 pontos cada
- 👥 **Seguidores**: 3 pontos cada

### 🏅 Níveis
- 🌱 **Padawan Developer** (0-199 pontos)
- 💻 **Script Kiddie** (200-499 pontos)
- ⚡ **Code Warrior** (500-999 pontos)
- 🚀 **Ninja Master** (1000+ pontos)

### 🏆 Conquistas
- 🌟 **Star Collector**: Colete stars nos seus repos
- 🍴 **Fork Master**: Tenha seus projetos "forkados"
- 📚 **Polyglot**: Domine múltiplas linguagens
- 🚀 **Project Creator**: Crie muitos repositórios
- 👑 **Influencer Dev**: Ganhe seguidores

## 🎨 Temas Visuais

### 🌞 Light Theme
- Design profissional e limpo
- Cores suaves e legíveis
- Ideal para impressão

### 🌙 Dark Theme
- Visual moderno e elegante
- Cores escuras com acentos roxos
- Perfeito para desenvolvedores

### 🌈 Cyberpunk Theme
- Estilo futurista com neon
- Animações CSS e efeitos visuais
- Para quem quer se destacar!

## 🧪 Exemplos de Uso

### Exemplo Básico
```bash
# Currículo simples em PDF
python app.py generate --output meu-curriculo.pdf
```

### Exemplo Avançado
```bash
# Currículo gamificado tema cyberpunk em HTML
python app.py generate \
  --theme cyberpunk \
  --format html \
  --gamified \
  --output portfolio.html
```

### Exemplo com Token Personalizado
```bash
# Usando token específico
python app.py generate --token ghp_seu_token_aqui --output cv.pdf
```

## 🔧 Desenvolvimento

### Estrutura do Projeto
```
GithubATS/
├── app.py                 # CLI principal
├── src/
│   ├── github_analyzer.py # Análise do GitHub
│   ├── llm_client.py     # Cliente LLM
│   ├── resume_generator.py # Gerador de currículos
│   └── gamification.py   # Sistema de gamificação
├── templates/            # Templates Jinja2
│   ├── base.md.j2       # Template Markdown
│   ├── light.html.j2    # Tema claro
│   ├── dark.html.j2     # Tema escuro
│   └── cyberpunk.html.j2 # Tema cyberpunk
├── output/              # Arquivos gerados
├── test_app.py         # Testes unitários
└── example.py          # Exemplo de uso
```

### Executar Testes
```bash
python test_app.py
```

### Executar Exemplo
```bash
python example.py
```

## 🤖 Modelos LLM Suportados

O projeto usa OpenRouter com modelos opensource:
- **microsoft/wizardlm-2-8x22b** (padrão)
- **meta-llama/llama-3.1-8b-instruct**
- **mistralai/mixtral-8x7b-instruct**

## 🐛 Solução de Problemas

### Erro: "Token do GitHub não encontrado"
```bash
# Verifique se o token está configurado
echo $GITHUB_TOKEN

# Configure se necessário
export GITHUB_TOKEN="seu_token_aqui"
```

### Erro: "Erro ao gerar PDF"
O PDF requer WeasyPrint. Se falhar:
1. Use formato HTML: `--format html`
2. Instale dependências do sistema (Ubuntu/Debian):
```bash
sudo apt-get install python3-dev python3-pip python3-cffi python3-brotli libpango-1.0-0 libharfbuzz0b libpangoft2-1.0-0
```

### Erro: "LLM não disponível"
- Verifique conexão com internet
- Confirme se OPENROUTER_API_KEY está configurada
- O app funciona sem LLM (usa dados básicos do GitHub)

## 📊 Métricas e Analytics

O app coleta automaticamente:
- 📦 Número de repositórios
- ⭐ Total de stars recebidas
- 🍴 Total de forks
- 👥 Seguidores e seguindo
- 💻 Linguagens de programação usadas
- 📅 Atividade recente nos repositórios

## 🎯 Otimização ATS

O currículo é otimizado para sistemas ATS:
- ✅ Estrutura clara com seções bem definidas
- ✅ Palavras-chave técnicas relevantes
- ✅ Formato legível por máquinas
- ✅ Informações de contato padronizadas
- ✅ Habilidades técnicas destacadas

## 🤝 Contribuindo

1. Fork o projeto
2. Crie uma branch: `git checkout -b feature/nova-funcionalidade`
3. Commit suas mudanças: `git commit -m 'Adiciona nova funcionalidade'`
4. Push para a branch: `git push origin feature/nova-funcionalidade`
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para detalhes.

## 🙏 Agradecimentos

- **OpenRouter** pela API de LLM opensource
- **GitHub** pela API robusta
- **Typer** pelo framework CLI incrível
- **Rich** pela interface linda no terminal
- **WeasyPrint** pela geração de PDF
- **Jinja2** pelo sistema de templates

## 🚀 Roadmap

- [ ] Suporte a mais temas visuais
- [ ] Integração com LinkedIn
- [ ] Análise de commits e contribuições
- [ ] Dashboard web interativo
- [ ] Exportação para LaTeX
- [ ] Integração com portfólios online
- [ ] Análise de soft skills via commits
- [ ] Recomendações de melhoria do perfil

---

**Feito com ❤️ e muito ☕ por desenvolvedores, para desenvolvedores!**

*Transforme seu GitHub em um currículo profissional em segundos!* 🚀
