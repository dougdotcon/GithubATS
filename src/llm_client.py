"""
Cliente LLM para análise de repositórios usando OpenRouter
"""

import os
import json
import requests
from typing import Dict, List, Optional
import time

class LLMClient:
    """Cliente para comunicação com LLM via OpenRouter"""
    
    def __init__(self):
        """Inicializa cliente LLM"""
        self.api_key = os.getenv("OPENROUTER_API_KEY")
        if not self.api_key:
            raise ValueError("OPENROUTER_API_KEY não encontrada nas variáveis de ambiente")
        
        self.base_url = "https://openrouter.ai/api/v1"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://github.com/GithubATS",
            "X-Title": "GitHub ATS Resume Generator"
        }
        
        # Modelo opensource recomendado
        self.model = "microsoft/wizardlm-2-8x22b"  # Modelo opensource potente
        
    def analyze_repositories(self, repos_data: List[Dict]) -> List[Dict]:
        """Analisa repositórios usando LLM"""
        processed_repos = []
        
        for repo in repos_data:
            try:
                analysis = self._analyze_single_repository(repo)
                if analysis:
                    repo.update(analysis)
                    processed_repos.append(repo)
                    
                # Rate limiting - pausa entre requests
                time.sleep(1)
                
            except Exception as e:
                print(f"Erro ao analisar repositório {repo['name']}: {e}")
                # Adicionar repo sem análise LLM em caso de erro
                repo.update({
                    'llm_title': repo['name'],
                    'llm_description': repo['description'] or 'Projeto de desenvolvimento',
                    'llm_skills': [repo['language']] if repo['language'] else [],
                    'llm_achievements': [],
                    'llm_category': 'Desenvolvimento'
                })
                processed_repos.append(repo)
        
        return processed_repos
    
    def _analyze_single_repository(self, repo: Dict) -> Optional[Dict]:
        """Analisa um único repositório"""
        
        # Preparar contexto para análise
        context = self._prepare_repository_context(repo)
        
        prompt = f"""
Analise este repositório GitHub e forneça uma análise estruturada em JSON.

CONTEXTO DO REPOSITÓRIO:
{context}

Forneça a resposta APENAS em formato JSON válido com esta estrutura:
{{
    "llm_title": "Título profissional do projeto (máximo 60 caracteres)",
    "llm_description": "Descrição concisa e profissional (máximo 150 caracteres)",
    "llm_skills": ["lista", "de", "tecnologias", "e", "habilidades"],
    "llm_achievements": ["conquistas", "métricas", "ou", "destaques"],
    "llm_category": "Categoria do projeto (ex: Web Development, Data Science, Mobile, etc.)"
}}

INSTRUÇÕES:
- Seja conciso e profissional
- Foque em habilidades técnicas relevantes para ATS
- Destaque conquistas mensuráveis quando possível
- Use terminologia técnica apropriada
- Mantenha descrições dentro dos limites de caracteres
"""

        try:
            response = requests.post(
                f"{self.base_url}/chat/completions",
                headers=self.headers,
                json={
                    "model": self.model,
                    "messages": [
                        {
                            "role": "system", 
                            "content": "Você é um especialista em análise de código e criação de currículos técnicos. Responda sempre em JSON válido."
                        },
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ],
                    "temperature": 0.3,
                    "max_tokens": 500
                },
                timeout=30
            )
            
            if response.status_code == 200:
                result = response.json()
                content = result['choices'][0]['message']['content'].strip()
                
                # Tentar extrair JSON da resposta
                try:
                    # Remover markdown se presente
                    if content.startswith('```json'):
                        content = content.replace('```json', '').replace('```', '').strip()
                    elif content.startswith('```'):
                        content = content.replace('```', '').strip()
                    
                    return json.loads(content)
                    
                except json.JSONDecodeError as e:
                    print(f"Erro ao parsear JSON: {e}")
                    print(f"Conteúdo recebido: {content}")
                    return None
            else:
                print(f"Erro na API: {response.status_code} - {response.text}")
                return None
                
        except requests.exceptions.RequestException as e:
            print(f"Erro de conexão: {e}")
            return None
    
    def _prepare_repository_context(self, repo: Dict) -> str:
        """Prepara contexto do repositório para análise"""
        context_parts = []
        
        # Informações básicas
        context_parts.append(f"Nome: {repo['name']}")
        if repo['description']:
            context_parts.append(f"Descrição: {repo['description']}")
        
        # Métricas
        context_parts.append(f"Linguagem principal: {repo['language'] or 'Não especificada'}")
        context_parts.append(f"Stars: {repo['stars']}")
        context_parts.append(f"Forks: {repo['forks']}")
        
        # Tópicos/tags
        if repo['topics']:
            context_parts.append(f"Tópicos: {', '.join(repo['topics'])}")
        
        # Linguagens do repositório
        if repo['languages']:
            langs = list(repo['languages'].keys())[:5]  # Top 5 linguagens
            context_parts.append(f"Tecnologias: {', '.join(langs)}")
        
        # README (primeiros parágrafos)
        if repo['readme_content']:
            readme_preview = repo['readme_content'][:800]  # Limitar tamanho
            context_parts.append(f"README:\n{readme_preview}")
        
        return "\n".join(context_parts)
    
    def generate_professional_summary(self, user_data: Dict, stats: Dict) -> str:
        """Gera resumo profissional baseado nos dados do usuário"""
        
        prompt = f"""
Crie um resumo profissional conciso (máximo 200 palavras) baseado nestes dados do GitHub:

DADOS DO USUÁRIO:
- Nome: {user_data.get('name', 'Desenvolvedor')}
- Bio: {user_data.get('bio', '')}
- Localização: {user_data.get('location', '')}
- Empresa: {user_data.get('company', '')}

ESTATÍSTICAS:
- Repositórios públicos: {stats.get('total_repos', 0)}
- Total de stars: {stats.get('total_stars', 0)}
- Seguidores: {stats.get('followers', 0)}
- Principais linguagens: {', '.join(list(stats.get('languages', {}).keys())[:5])}

Crie um resumo profissional que:
- Destaque experiência técnica
- Mencione principais tecnologias
- Seja otimizado para ATS
- Use linguagem profissional
- Foque em resultados e impacto
"""

        try:
            response = requests.post(
                f"{self.base_url}/chat/completions",
                headers=self.headers,
                json={
                    "model": self.model,
                    "messages": [
                        {
                            "role": "system",
                            "content": "Você é um especialista em criação de currículos técnicos otimizados para ATS."
                        },
                        {
                            "role": "user", 
                            "content": prompt
                        }
                    ],
                    "temperature": 0.4,
                    "max_tokens": 300
                },
                timeout=30
            )
            
            if response.status_code == 200:
                result = response.json()
                return result['choices'][0]['message']['content'].strip()
            else:
                return "Desenvolvedor apaixonado por tecnologia com experiência em múltiplas linguagens de programação e projetos open source."
                
        except Exception as e:
            print(f"Erro ao gerar resumo profissional: {e}")
            return "Desenvolvedor apaixonado por tecnologia com experiência em múltiplas linguagens de programação e projetos open source."
