"""
Configurações do GitHub ATS Resume Generator
"""

import os
from typing import Dict, Any

class Config:
    """Classe de configuração centralizada"""
    
    # APIs
    GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
    OPENROUTER_API_KEY = os.getenv('OPENROUTER_API_KEY', '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')
    
    # OpenRouter
    OPENROUTER_BASE_URL = 'https://openrouter.ai/api/v1'
    DEFAULT_MODEL = 'microsoft/wizardlm-2-8x22b'  # Modelo opensource
    
    # Configurações padrão
    DEFAULT_THEME = os.getenv('DEFAULT_THEME', 'light')
    DEFAULT_OUTPUT_FORMAT = os.getenv('DEFAULT_OUTPUT_FORMAT', 'pdf')
    DEFAULT_REPO_LIMIT = 20
    
    # Temas disponíveis
    AVAILABLE_THEMES = ['light', 'dark', 'cyberpunk']
    
    # Formatos disponíveis
    AVAILABLE_FORMATS = ['pdf', 'html', 'markdown']
    
    # Sistema de pontuação
    POINTS_CONFIG = {
        'star': 10,
        'fork': 5,
        'repo': 2,
        'language': 15,
        'follower': 3
    }
    
    # Níveis de gamificação
    LEVELS = [
        {'min': 0, 'max': 199, 'name': 'Padawan Developer', 'emoji': '🌱'},
        {'min': 200, 'max': 499, 'name': 'Script Kiddie', 'emoji': '💻'},
        {'min': 500, 'max': 999, 'name': 'Code Warrior', 'emoji': '⚡'},
        {'min': 1000, 'max': float('inf'), 'name': 'Ninja Master', 'emoji': '🚀'}
    ]
    
    # Configurações de template
    TEMPLATE_CONFIG = {
        'max_repos_display': 8,
        'max_skills_display': 15,
        'max_languages_display': 10,
        'readme_max_length': 3000
    }
    
    # Timeouts e limites
    API_TIMEOUT = 30
    RATE_LIMIT_DELAY = 1  # segundos entre requests LLM
    
    @classmethod
    def validate(cls) -> Dict[str, Any]:
        """Valida configurações e retorna status"""
        issues = []
        
        if not cls.GITHUB_TOKEN:
            issues.append("GITHUB_TOKEN não configurado")
        
        if not cls.OPENROUTER_API_KEY:
            issues.append("OPENROUTER_API_KEY não configurado")
        
        if cls.DEFAULT_THEME not in cls.AVAILABLE_THEMES:
            issues.append(f"Tema padrão '{cls.DEFAULT_THEME}' não é válido")
        
        if cls.DEFAULT_OUTPUT_FORMAT not in cls.AVAILABLE_FORMATS:
            issues.append(f"Formato padrão '{cls.DEFAULT_OUTPUT_FORMAT}' não é válido")
        
        return {
            'valid': len(issues) == 0,
            'issues': issues,
            'github_configured': bool(cls.GITHUB_TOKEN),
            'llm_configured': bool(cls.OPENROUTER_API_KEY)
        }
    
    @classmethod
    def get_headers(cls) -> Dict[str, str]:
        """Retorna headers para requisições OpenRouter"""
        return {
            "Authorization": f"Bearer {cls.OPENROUTER_API_KEY}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://github.com/GithubATS",
            "X-Title": "GitHub ATS Resume Generator"
        }
