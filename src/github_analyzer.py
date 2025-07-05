"""
Módulo para análise de repositórios GitHub
"""

import base64
from typing import Dict, List, Optional
from github import Github, GithubException
from collections import Counter
import re

class GitHubAnalyzer:
    """Analisador de dados do GitHub"""
    
    def __init__(self, token: str):
        """Inicializa o analisador com token do GitHub"""
        self.github = Github(token)
        self.user = self.github.get_user()
        
    def get_user_info(self) -> Dict:
        """Coleta informações básicas do usuário"""
        try:
            return {
                'name': self.user.name or self.user.login,
                'login': self.user.login,
                'email': self.user.email or '',
                'bio': self.user.bio or '',
                'location': self.user.location or '',
                'company': self.user.company or '',
                'blog': self.user.blog or '',
                'avatar_url': self.user.avatar_url,
                'public_repos': self.user.public_repos,
                'followers': self.user.followers,
                'following': self.user.following,
                'created_at': self.user.created_at.isoformat() if self.user.created_at else None
            }
        except GithubException as e:
            raise Exception(f"Erro ao obter dados do usuário: {e}")
    
    def analyze_repositories(self, limit: int = 20) -> List[Dict]:
        """Analisa repositórios do usuário"""
        repos_data = []

        try:
            # Pegar repositórios ordenados por stars
            repos = self.user.get_repos(sort='updated', direction='desc')

            count = 0
            for repo in repos:
                if count >= limit:
                    break

                # Analisar APENAS repositórios próprios (não forks)
                if repo.fork:
                    continue
                
                repo_data = {
                    'name': repo.name,
                    'full_name': repo.full_name,
                    'description': repo.description or '',
                    'language': repo.language,
                    'stars': repo.stargazers_count,
                    'forks': repo.forks_count,
                    'size': repo.size,
                    'created_at': repo.created_at.isoformat() if repo.created_at else None,
                    'updated_at': repo.updated_at.isoformat() if repo.updated_at else None,
                    'topics': repo.get_topics(),
                    'is_fork': repo.fork,
                    'readme_content': self._get_readme_content(repo),
                    'languages': self._get_repository_languages(repo),
                    'url': repo.html_url
                }
                
                repos_data.append(repo_data)
                count += 1
                
        except GithubException as e:
            raise Exception(f"Erro ao analisar repositórios: {e}")
            
        return repos_data
    
    def _get_readme_content(self, repo) -> str:
        """Extrai conteúdo do README do repositório"""
        try:
            # Tentar diferentes nomes de README
            readme_names = ['README.md', 'README.rst', 'README.txt', 'README', 'readme.md']
            
            for readme_name in readme_names:
                try:
                    readme = repo.get_contents(readme_name)
                    if readme.encoding == 'base64':
                        content = base64.b64decode(readme.content).decode('utf-8')
                        # Limitar tamanho para não sobrecarregar a LLM
                        return content[:3000] if len(content) > 3000 else content
                    return readme.decoded_content.decode('utf-8')[:3000]
                except:
                    continue
                    
            return ""
        except:
            return ""
    
    def _get_repository_languages(self, repo) -> Dict[str, int]:
        """Obtém linguagens do repositório"""
        try:
            return repo.get_languages()
        except:
            return {}
    
    def get_stats(self) -> Dict:
        """Calcula estatísticas gerais"""
        repos = list(self.user.get_repos())

        # Filtrar apenas repositórios próprios (não forks)
        own_repos = [repo for repo in repos if not repo.fork]

        total_stars = sum(repo.stargazers_count for repo in own_repos)
        total_forks = sum(repo.forks_count for repo in own_repos)

        # Contar linguagens
        all_languages = []
        for repo in own_repos:
            if repo.language:
                all_languages.append(repo.language)
        
        language_counts = Counter(all_languages)
        
        return {
            'total_repos': len(own_repos),
            'total_stars': total_stars,
            'total_forks': total_forks,
            'languages': dict(language_counts.most_common(10)),
            'public_repos': len(own_repos),  # Apenas repos próprios
            'followers': self.user.followers,
            'following': self.user.following
        }
    
    def get_detailed_stats(self) -> Dict:
        """Estatísticas detalhadas para modo gamificado"""
        stats = self.get_stats()
        repos = list(self.user.get_repos())

        # Filtrar apenas repositórios próprios (não forks)
        own_repos = [repo for repo in repos if not repo.fork]

        # Repositórios mais populares
        top_repos = sorted(own_repos, key=lambda r: r.stargazers_count, reverse=True)[:5]

        # Atividade recente
        recent_repos = sorted(own_repos, key=lambda r: r.updated_at or r.created_at, reverse=True)[:5]
        
        stats.update({
            'top_repositories': [
                {
                    'name': repo.name,
                    'stars': repo.stargazers_count,
                    'language': repo.language,
                    'description': repo.description or ''
                }
                for repo in top_repos
            ],
            'recent_activity': [
                {
                    'name': repo.name,
                    'updated_at': repo.updated_at.isoformat() if repo.updated_at else None,
                    'language': repo.language
                }
                for repo in recent_repos
            ]
        })
        
        return stats
