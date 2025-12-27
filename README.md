# GithubATS

<div align="center">
  <img src="logo.png" alt="GithubATS Logo" width="200"/>
  <p><strong>Intelligent GitHub Resume Generator</strong></p>
  <p>A gamified Python CLI that generates ATS-friendly resumes from your GitHub repositories using intelligent LLM analysis.</p>
  
  <p>
    <a href="#features">Features</a> •
    <a href="#installation">Installation</a> •
    <a href="#usage">Usage</a> •
    <a href="#gamification">Gamification</a> •
    <a href="#themes">Themes</a>
  </p>

  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
  [![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://python.org)
</div>

---

## ✨ Features

GithubATS transforms your GitHub profile into a professional, ATS-optimized resume by analyzing your repositories with Large Language Models (LLMs).

### Core Capabilities
- **Intelligent Analysis**: LLM-powered analysis of repository content, technologies, and complexity
- **ATS Optimization**: Generates resumes formatted specifically to pass Applicant Tracking Systems
- **Multiple Formats**: Export to PDF, HTML, or Markdown
- **Gamification System**: Earn points, levels, and achievements based on your coding activity
- **Visual Themes**: Choose between Light, Dark, and Cyberpunk visual styles
- **Automated Metrics**: Automatic extraction of stars, forks, and language statistics
- **Badge System**: Collect badges and achievements to showcase your skills

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- GitHub Personal Access Token
- OpenRouter API Key (or compatible OpenAI endpoint)

### Install via pip
bash
pip install githubats


### Manual Installation
bash
# Clone the repository
git clone https://github.com/your-username/GithubATS.git
cd GithubATS

# Install dependencies
pip install -r requirements.txt

# Create environment file
cp .env.example .env


## ⚙️ Configuration

1. **GitHub Token**: Generate at [GitHub Settings](https://github.com/settings/tokens)
   - Required scopes: `public_repo` (public) or `repo` (private)

2. **LLM API Key**: Get an API key from [OpenRouter](https://openrouter.ai/) or any OpenAI-compatible provider

3. **Environment Variables**: Configure your `.env` file:
bash
GITHUB_TOKEN="ghp_your_token_here"
OPENROUTER_API_KEY="sk-or-v1-your_key_here"


## 🚀 Usage

### Basic Commands

bash
# Generate basic resume
python app.py generate

# Generate gamified cyberpunk themed resume
python app.py generate --theme cyberpunk --gamified --output my-resume.pdf

# Generate HTML format
python app.py generate --format html --output resume.html

# View statistics
python app.py stats

# Show help
python app.py --help


### Options Reference

| Flag | Values | Description |
|------|--------|-------------|
| `--theme` | `light`, `dark`, `cyberpunk` | Visual theme |
| `--format` | `pdf`, `html`, `markdown` | Output format |
| `--gamified` | - | Enable gamification features |
| `--output` | `filename` | Output file path |

## 🎮 Gamification

The gamification system adds a fun layer to resume building:

- **Experience Points (XP)**: Earned by analyzing repos and complexity
- **Levels**: Progress from Rookie to Code Master
- **Achievements**: Unlock badges for milestones (e.g., "First Repo Analyzed", "10k+ Lines of Code")
- **Motivational Quotes**: Random programming quotes appear during processing

## 🎨 Themes

| Theme | Description |
|-------|-------------|
| **Light** | Clean, professional white background |
| **Dark** | Modern dark mode with muted colors |
| **Cyberpunk** | Futuristic neon aesthetic with terminal vibes |

## 🔧 Development

bash
# Run tests
pytest

# Lint code
black .
flake8

# Build package
python setup.py sdist bdist_wheel


## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments
- Built with Python and LLM integration
- Gamification inspired by developer productivity apps
- ATS optimization based on recruiter feedback