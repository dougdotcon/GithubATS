<div align="center">
  <img src="logo.png" alt="GitHub ATS Logo" width="200"/>
  <h1>GitHub ATS Resume Generator</h1>
  <p>Um CLI Python divertido e gamificado que gera currículos ATS-friendly a partir dos seus repositórios GitHub usando LLM para análise inteligente!</p>

  <p>
    <a href="#funcionalidades">Funcionalidades</a> •
    <a href="#instalação">Instalação</a> •
    <a href="#uso">Uso</a> •
    <a href="#gamificação">Gamificação</a> •
    <a href="#temas">Temas</a> •
    <a href="#desenvolvimento">Desenvolvimento</a> •
    <a href="#solução-de-problemas">Solução de Problemas</a>
  </p>
</div>

---

## 📋 Funcionalidades

<table>
  <tr>
    <td>
      <ul>
        <li><b>Análise inteligente</b> de repositórios com LLM</li>
        <li><b>Múltiplos formatos</b> de saída (PDF, HTML, Markdown)</li>
        <li><b>Sistema gamificado</b> com pontuação e níveis</li>
        <li><b>3 temas visuais</b> (Light, Dark, Cyberpunk)</li>
      </ul>
    </td>
    <td>
      <ul>
        <li><b>Métricas automáticas</b> (stars, forks, linguagens)</li>
        <li><b>Sistema de badges</b> e conquistas</li>
        <li><b>Easter eggs</b> e citações motivacionais</li>
        <li><b>Otimizado para ATS</b> (Applicant Tracking Systems)</li>
      </ul>
    </td>
  </tr>
</table>

## 💻 Instalação

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

### Configuração Detalhada

<details>
<summary><b>1. Token do GitHub</b></summary>
<p>
Crie um token em: https://github.com/settings/tokens
<ul>
  <li>Selecione escopo: <code>public_repo</code> (para repos públicos) ou <code>repo</code> (para privados)</li>
</ul>
</p>
</details>

<details>
<summary><b>2. Variáveis de Ambiente</b></summary>

```bash
# Método 1: Arquivo .env (recomendado)
cp .env.example .env
# Edite o arquivo .env

# Método 2: Export direto
export GITHUB_TOKEN="ghp_seu_token_aqui"
export OPENROUTER_API_KEY="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"
```
</details>

<details>
<summary><b>3. Teste a Configuração</b></summary>

```bash
python example.py
```
</details>

## 🚀 Uso

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

## 🎮 Gamificação

<div align="center">
  <table>
    <tr>
      <th>Pontuação</th>
      <th>Níveis</th>
      <th>Conquistas</th>
    </tr>
    <tr>
      <td>
        <ul>
          <li><b>Stars</b>: 10 pontos cada</li>
          <li><b>Forks</b>: 5 pontos cada</li>
          <li><b>Repositórios</b>: 2 pontos cada</li>
          <li><b>Linguagens</b>: 15 pontos cada</li>
          <li><b>Seguidores</b>: 3 pontos cada</li>
        </ul>
      </td>
      <td>
        <ul>
          <li><b>Padawan Developer</b> (0-199 pontos)</li>
          <li><b>Script Kiddie</b> (200-499 pontos)</li>
          <li><b>Code Warrior</b> (500-999 pontos)</li>
          <li><b>Ninja Master</b> (1000+ pontos)</li>
        </ul>
      </td>
      <td>
        <ul>
          <li><b>Star Collector</b>: Colete stars nos seus repos</li>
          <li><b>Fork Master</b>: Tenha seus projetos "forkados"</li>
          <li><b>Polyglot</b>: Domine múltiplas linguagens</li>
          <li><b>Project Creator</b>: Crie muitos repositórios</li>
          <li><b>Influencer Dev</b>: Ganhe seguidores</li>
        </ul>
      </td>
    </tr>
  </table>
</div>

## 🎨 Temas

<div align="center">
  <table>
    <tr>
      <th width="33%">Light Theme</th>
      <th width="33%">Dark Theme</th>
      <th width="33%">Cyberpunk Theme</th>
    </tr>
    <tr>
      <td>
        <ul>
          <li>Design profissional e limpo</li>
          <li>Cores suaves e legíveis</li>
          <li>Ideal para impressão</li>
        </ul>
      </td>
      <td>
        <ul>
          <li>Visual moderno e elegante</li>
          <li>Cores escuras com acentos roxos</li>
          <li>Perfeito para desenvolvedores</li>
        </ul>
      </td>
      <td>
        <ul>
          <li>Estilo futurista com neon</li>
          <li>Animações CSS e efeitos visuais</li>
          <li>Para quem quer se destacar!</li>
        </ul>
      </td>
    </tr>
  </table>
</div>

## 🧪 Exemplos de Uso

<details>
<summary><b>Exemplo Básico</b></summary>

```bash
# Currículo simples em PDF
python app.py generate --output meu-curriculo.pdf
```
</details>

<details>
<summary><b>Exemplo Avançado</b></summary>

```bash
# Currículo gamificado tema cyberpunk em HTML
python app.py generate \
  --theme cyberpunk \
  --format html \
  --gamified \
  --output portfolio.html
```
</details>

<details>
<summary><b>Exemplo com Token Personalizado</b></summary>

```bash
# Usando token específico
python app.py generate --token ghp_seu_token_aqui --output cv.pdf
```
</details>

## 🔧 Desenvolvimento

### Estrutura do Projeto

```
GithubATS/
├── app.py                 # CLI principal
├── src/
│   ├── github_analyzer.py # Análise do GitHub
│   ├── llm_client.py      # Cliente LLM
│   ├── resume_generator.py # Gerador de currículos
│   └── gamification.py    # Sistema de gamificação
├── templates/             # Templates Jinja2
│   ├── base.md.j2         # Template Markdown
│   ├── light.html.j2      # Tema claro
│   ├── dark.html.j2       # Tema escuro
│   └── cyberpunk.html.j2  # Tema cyberpunk
├── output/                # Arquivos gerados
├── test_app.py            # Testes unitários
└── example.py             # Exemplo de uso
```

### Executar Testes

```bash
python test_app.py
```

## 🤖 Modelos LLM Suportados

O projeto usa OpenRouter com modelos opensource:
- **microsoft/wizardlm-2-8x22b** (padrão)
- **meta-llama/llama-3.1-8b-instruct**
- **mistralai/mixtral-8x7b-instruct**

## ⚠️ Solução de Problemas

<details>
<summary><b>Erro: "Token do GitHub não encontrado"</b></summary>

```bash
# Verifique se o token está configurado
echo $GITHUB_TOKEN

# Configure se necessário
export GITHUB_TOKEN="seu_token_aqui"
```
</details>

<details>
<summary><b>Erro: "Erro ao gerar PDF"</b></summary>
<p>
O PDF requer WeasyPrint. Se falhar:
<ol>
  <li>Use formato HTML: <code>--format html</code></li>
  <li>Instale dependências do sistema (Ubuntu/Debian):</li>
</ol>

```bash
sudo apt-get install python3-dev python3-pip python3-cffi python3-brotli libpango-1.0-0 libharfbuzz0b libpangoft2-1.0-0
```
</p>
</details>

<details>
<summary><b>Erro: "LLM não disponível"</b></summary>
<ul>
  <li>Verifique conexão com internet</li>
  <li>Confirme se OPENROUTER_API_KEY está configurada</li>
  <li>O app funciona sem LLM (usa dados básicos do GitHub)</li>
</ul>
</details>

## 📊 Métricas e Analytics

O app coleta automaticamente:
- Número de repositórios
- Total de stars recebidas
- Total de forks
- Seguidores e seguindo
- Linguagens de programação usadas
- Atividade recente nos repositórios

## 🎯 Otimização ATS

O currículo é otimizado para sistemas ATS:
- Estrutura clara com seções bem definidas
- Palavras-chave técnicas relevantes
- Formato legível por máquinas
- Informações de contato padronizadas
- Habilidades técnicas destacadas

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

---

<div align="center">
  <p>Desenvolvido com dedicação para otimizar sua presença profissional</p>
</div>
