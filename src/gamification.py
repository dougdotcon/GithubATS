"""
Sistema de gamificação para o GitHub ATS Resume Generator
"""

import random
from typing import Dict, List, Tuple
from datetime import datetime

class GamificationEngine:
    """Engine de gamificação com sistema de pontos, níveis e conquistas"""
    
    # Citações motivacionais para easter eggs
    MOTIVATIONAL_QUOTES = [
        "💻 'Code is poetry written in logic' - Unknown",
        "🚀 'The best error message is the one that never shows up' - Thomas Fuchs", 
        "⚡ 'Programming isn't about what you know; it's about what you can figure out' - Chris Pine",
        "🎯 'Clean code always looks like it was written by someone who cares' - Robert C. Martin",
        "🔥 'First, solve the problem. Then, write the code' - John Johnson",
        "🌟 'Any fool can write code that a computer can understand. Good programmers write code that humans can understand' - Martin Fowler",
        "🎨 'Code never lies, comments sometimes do' - Ron Jeffries",
        "🚀 'The most important property of a program is whether it accomplishes the intention of its user' - C.A.R. Hoare",
        "⚡ 'Simplicity is the ultimate sophistication' - Leonardo da Vinci",
        "🎯 'Make it work, make it right, make it fast' - Kent Beck"
    ]
    
    # ASCII Art para diferentes níveis
    ASCII_ART = {
        'padawan': """
    PADAWAN DEVELOPER
    ╭─────────────────────╮
    │   ░░░░░░░░░░░░░░░   │
    │   ░ LEARNING... ░   │
    │   ░░░░░░░░░░░░░░░   │
    ╰─────────────────────╯
        """,
        'script_kiddie': """
    SCRIPT KIDDIE
    ╭─────────────────────╮
    │   ████░░░░░░░░░░░   │
    │   ░ PROGRESSING ░   │
    │   ████░░░░░░░░░░░   │
    ╰─────────────────────╯
        """,
        'code_warrior': """
    CODE WARRIOR
    ╭─────────────────────╮
    │   ████████░░░░░░░   │
    │   ░ ADVANCING! ░    │
    │   ████████░░░░░░░   │
    ╰─────────────────────╯
        """,
        'ninja_master': """
    NINJA MASTER
    ╭─────────────────────╮
    │   ████████████████  │
    │   ░ LEGENDARY!! ░   │
    │   ████████████████  │
    ╰─────────────────────╯
        """
    }
    
    def __init__(self):
        """Inicializa o engine de gamificação"""
        pass
    
    def calculate_score(self, stats: Dict) -> Dict:
        """Calcula pontuação total e nível do desenvolvedor"""
        
        # Sistema de pontuação
        points = 0
        points += stats.get('total_stars', 0) * 10      # 10 pontos por star
        points += stats.get('total_forks', 0) * 5       # 5 pontos por fork
        points += stats.get('total_repos', 0) * 2       # 2 pontos por repo
        points += len(stats.get('languages', [])) * 15  # 15 pontos por linguagem
        points += stats.get('followers', 0) * 3         # 3 pontos por seguidor
        
        # Bônus por atividade recente (se tiver repos atualizados recentemente)
        recent_activity_bonus = self._calculate_activity_bonus(stats)
        points += recent_activity_bonus
        
        # Determinar nível
        level_info = self._determine_level(points)
        
        # Calcular conquistas
        achievements = self._calculate_achievements(stats)
        
        return {
            'total_points': points,
            'level': level_info['level'],
            'level_name': level_info['name'],
            'level_emoji': level_info['emoji'],
            'level_ascii': level_info['ascii'],
            'achievements': achievements,
            'progress_to_next': level_info['progress_to_next'],
            'next_level_points': level_info['next_level_points'],
            'activity_bonus': recent_activity_bonus
        }
    
    def _calculate_activity_bonus(self, stats: Dict) -> int:
        """Calcula bônus por atividade recente"""
        # Implementação simplificada - em uma versão real, 
        # analisaríamos commits recentes
        total_repos = stats.get('total_repos', 0)
        if total_repos > 10:
            return 50  # Bônus por ter muitos repos
        elif total_repos > 5:
            return 25
        return 0
    
    def _determine_level(self, points: int) -> Dict:
        """Determina nível baseado na pontuação"""
        
        levels = [
            {'min': 0, 'max': 199, 'name': 'Padawan Developer', 'emoji': '', 'key': 'padawan'},
            {'min': 200, 'max': 499, 'name': 'Script Kiddie', 'emoji': '', 'key': 'script_kiddie'},
            {'min': 500, 'max': 999, 'name': 'Code Warrior', 'emoji': '', 'key': 'code_warrior'},
            {'min': 1000, 'max': float('inf'), 'name': 'Ninja Master', 'emoji': '', 'key': 'ninja_master'}
        ]
        
        current_level = None
        for level in levels:
            if level['min'] <= points <= level['max']:
                current_level = level
                break
        
        if not current_level:
            current_level = levels[-1]  # Fallback para o nível mais alto
        
        # Calcular progresso para próximo nível
        if current_level['max'] == float('inf'):
            progress_to_next = 100  # Nível máximo
            next_level_points = 0
        else:
            next_level_points = current_level['max'] + 1
            progress_to_next = min(100, ((points - current_level['min']) / (next_level_points - current_level['min'])) * 100)
        
        return {
            'level': current_level['key'],
            'name': current_level['name'],
            'emoji': current_level['emoji'],
            'ascii': self.ASCII_ART.get(current_level['key'], ''),
            'progress_to_next': round(progress_to_next, 1),
            'next_level_points': next_level_points if next_level_points > 0 else None
        }
    
    def _calculate_achievements(self, stats: Dict) -> List[Dict]:
        """Calcula conquistas baseadas nas estatísticas"""
        achievements = []
        
        # Conquista: Star Collector
        stars = stats.get('total_stars', 0)
        if stars >= 100:
            achievements.append({
                'name': 'Star Collector Master',
                'emoji': '',
                'description': f'Coletou {stars} stars!',
                'tier': 'gold'
            })
        elif stars >= 50:
            achievements.append({
                'name': 'Star Collector',
                'emoji': '',
                'description': f'Coletou {stars} stars!',
                'tier': 'silver'
            })
        elif stars >= 10:
            achievements.append({
                'name': 'First Stars',
                'emoji': '',
                'description': f'Primeiras {stars} stars!',
                'tier': 'bronze'
            })
        
        # Conquista: Fork Master
        forks = stats.get('total_forks', 0)
        if forks >= 50:
            achievements.append({
                'name': 'Fork Master',
                'emoji': '',
                'description': f'{forks} forks conquistados!',
                'tier': 'gold'
            })
        elif forks >= 10:
            achievements.append({
                'name': 'Fork Collector',
                'emoji': '',
                'description': f'{forks} forks!',
                'tier': 'silver'
            })

        # Conquista: Polyglot
        languages = len(stats.get('languages', []))
        if languages >= 10:
            achievements.append({
                'name': 'Polyglot Master',
                'emoji': '',
                'description': f'Domina {languages} linguagens!',
                'tier': 'gold'
            })
        elif languages >= 5:
            achievements.append({
                'name': 'Polyglot',
                'emoji': '',
                'description': f'Conhece {languages} linguagens!',
                'tier': 'silver'
            })

        # Conquista: Project Creator
        repos = stats.get('total_repos', 0)
        if repos >= 50:
            achievements.append({
                'name': 'Project Architect',
                'emoji': '',
                'description': f'{repos} projetos criados!',
                'tier': 'gold'
            })
        elif repos >= 20:
            achievements.append({
                'name': 'Project Creator',
                'emoji': '',
                'description': f'{repos} projetos!',
                'tier': 'silver'
            })
        elif repos >= 5:
            achievements.append({
                'name': 'First Projects',
                'emoji': '',
                'description': f'{repos} primeiros projetos!',
                'tier': 'bronze'
            })

        # Conquista: Social Coder
        followers = stats.get('followers', 0)
        if followers >= 100:
            achievements.append({
                'name': 'Influencer Dev',
                'emoji': '',
                'description': f'{followers} seguidores!',
                'tier': 'gold'
            })
        elif followers >= 25:
            achievements.append({
                'name': 'Social Coder',
                'emoji': '',
                'description': f'{followers} seguidores!',
                'tier': 'silver'
            })
        
        return achievements
    
    def get_random_quote(self) -> str:
        """Retorna uma citação motivacional aleatória"""
        return random.choice(self.MOTIVATIONAL_QUOTES)
    
    def get_celebration_message(self, level_name: str) -> str:
        """Retorna mensagem de celebração baseada no nível"""
        celebrations = {
            'Padawan Developer': "Todo grande desenvolvedor começou assim! Continue aprendendo!",
            'Script Kiddie': "Você está evoluindo! Seus scripts estão ficando mais sofisticados!",
            'Code Warrior': "Impressionante! Você é um verdadeiro guerreiro do código!",
            'Ninja Master': "LENDÁRIO! Você alcançou o nível máximo de ninja do código!"
        }
        return celebrations.get(level_name, "Parabéns pelo seu progresso!")
    
    def generate_badge_url(self, label: str, message: str, color: str = "blue") -> str:
        """Gera URL para badge do shields.io"""
        return f"https://img.shields.io/badge/{label}-{message}-{color}"
    
    def get_github_stats_badges(self, stats: Dict) -> List[Dict]:
        """Gera badges para estatísticas do GitHub"""
        badges = []
        
        badges.append({
            'label': 'Repositórios',
            'value': stats.get('total_repos', 0),
            'color': 'blue',
            'url': self.generate_badge_url('Repos', str(stats.get('total_repos', 0)), 'blue')
        })
        
        badges.append({
            'label': 'Stars',
            'value': stats.get('total_stars', 0),
            'color': 'yellow',
            'url': self.generate_badge_url('Stars', str(stats.get('total_stars', 0)), 'yellow')
        })
        
        badges.append({
            'label': 'Forks',
            'value': stats.get('total_forks', 0),
            'color': 'green',
            'url': self.generate_badge_url('Forks', str(stats.get('total_forks', 0)), 'green')
        })
        
        badges.append({
            'label': 'Seguidores',
            'value': stats.get('followers', 0),
            'color': 'orange',
            'url': self.generate_badge_url('Followers', str(stats.get('followers', 0)), 'orange')
        })
        
        return badges
