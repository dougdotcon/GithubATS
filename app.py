#!/usr/bin/env python3
"""
GitHub ATS Resume Generator
Um CLI divertido para gerar currículos ATS-friendly a partir do GitHub
"""

import random
from typing import Optional
import typer
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.table import Table
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

# Configuração do CLI
app = typer.Typer(
    name="github-ats-resume",
    help="Gerador de currículos ATS-friendly a partir do GitHub",
    rich_markup_mode="rich"
)
console = Console()

# Easter eggs - citações motivacionais
MOTIVATIONAL_QUOTES = [
    "'Code is poetry written in logic' - Unknown",
    "'The best error message is the one that never shows up' - Thomas Fuchs",
    "'Programming isn't about what you know; it's about what you can figure out' - Chris Pine",
    "'Clean code always looks like it was written by someone who cares' - Robert C. Martin",
    "'First, solve the problem. Then, write the code' - John Johnson"
]

def show_banner():
    """Exibe banner divertido do app"""
    banner = """
    ╔══════════════════════════════════════════════════════════════╗
    ║                    GitHub ATS Resume Generator               ║
    ║                                                              ║
    ║              Transforme seu GitHub em um currículo           ║
    ║                     profissional e divertido!               ║
    ╚══════════════════════════════════════════════════════════════╝
    """
    console.print(Panel(banner, style="bold blue"))

    # Easter egg - citação aleatória
    quote = random.choice(MOTIVATIONAL_QUOTES)
    console.print(f"\n{quote}\n", style="italic yellow")

@app.command()
def generate(
    token: Optional[str] = typer.Option(
        None, 
        "--token", 
        envvar="GITHUB_TOKEN",
        help="Token de acesso do GitHub"
    ),
    output: str = typer.Option(
        "resume.pdf", 
        "--output", "-o",
        help="Arquivo de saída (ex: resume.pdf, resume.html)"
    ),
    theme: str = typer.Option(
        "light",
        "--theme", "-t", 
        help="Tema do currículo: light, dark, cyberpunk"
    ),
    gamified: bool = typer.Option(
        False,
        "--gamified", "-g",
        help="Ativar modo gamificado com pontuação e badges"
    ),
    format: str = typer.Option(
        "pdf",
        "--format", "-f",
        help="Formato de saída: pdf, html, markdown"
    )
):
    """
    Gera um currículo ATS-friendly a partir dos seus repositórios GitHub
    """
    show_banner()

    if not token:
        console.print("Token do GitHub não encontrado!", style="bold red")
        console.print("Configure com: export GITHUB_TOKEN='seu_token'")
        raise typer.Exit(1)

    console.print(f"Tema selecionado: [bold]{theme}[/bold]")
    console.print(f"Formato: [bold]{format}[/bold]")
    console.print(f"Modo gamificado: [bold]{'Sim' if gamified else 'Não'}[/bold]")
    console.print(f"Arquivo de saída: [bold]{output}[/bold]\n")
    
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
    ) as progress:
        
        # Importar módulos necessários
        task1 = progress.add_task("Carregando módulos...", total=None)
        from src.github_analyzer import GitHubAnalyzer
        from src.llm_client import LLMClient
        from src.resume_generator import ResumeGenerator
        progress.update(task1, completed=True)

        # Conectar ao GitHub
        task2 = progress.add_task("Conectando ao GitHub...", total=None)
        analyzer = GitHubAnalyzer(token)
        user_data = analyzer.get_user_info()
        progress.update(task2, completed=True)

        console.print(f"Olá, [bold green]{user_data['name']}[/bold green]!")

        # Analisar repositórios
        task3 = progress.add_task("Analisando repositórios...", total=None)
        repos_data = analyzer.analyze_repositories()
        progress.update(task3, completed=True)

        # Processar com LLM
        task4 = progress.add_task("Processando com IA...", total=None)
        llm_client = LLMClient()
        processed_repos = llm_client.analyze_repositories(repos_data)
        progress.update(task4, completed=True)

        # Gerar currículo
        task5 = progress.add_task("Gerando currículo...", total=None)
        generator = ResumeGenerator(theme=theme, gamified=gamified)
        resume_data = {
            'user': user_data,
            'repositories': processed_repos,
            'stats': analyzer.get_stats()
        }
        generator.generate(resume_data, output, format)
        progress.update(task5, completed=True)

    console.print(f"\n[bold green]Currículo gerado com sucesso![/bold green]")
    console.print(f"Arquivo salvo em: [bold blue]{output}[/bold blue]")

    if gamified:
        show_gamification_stats(analyzer.get_stats())

@app.command()
def stats(
    token: Optional[str] = typer.Option(
        None,
        "--token",
        envvar="GITHUB_TOKEN",
        help="Token de acesso do GitHub"
    )
):
    """
    Mostra estatísticas gamificadas do seu GitHub
    """
    show_banner()

    if not token:
        console.print("Token do GitHub não encontrado!", style="bold red")
        raise typer.Exit(1)

    from src.github_analyzer import GitHubAnalyzer

    with console.status("Coletando estatísticas..."):
        analyzer = GitHubAnalyzer(token)
        stats = analyzer.get_detailed_stats()

    show_detailed_stats(stats)

def show_gamification_stats(stats: dict):
    """Exibe estatísticas gamificadas"""
    from src.gamification import GamificationEngine

    gamification = GamificationEngine()
    game_data = gamification.calculate_score(stats)

    # Mostrar ASCII art do nível
    console.print(Panel(game_data['level_ascii'], style="bold green"))

    # Tabela de pontuação
    table = Table(title="Suas Conquistas de Desenvolvedor")
    table.add_column("Conquista", style="cyan")
    table.add_column("Valor", style="magenta")
    table.add_column("Pontos", style="green")

    table.add_row("Total de Stars", str(stats.get('total_stars', 0)), f"{stats.get('total_stars', 0) * 10}")
    table.add_row("Total de Forks", str(stats.get('total_forks', 0)), f"{stats.get('total_forks', 0) * 5}")
    table.add_row("Repositórios", str(stats.get('total_repos', 0)), f"{stats.get('total_repos', 0) * 2}")
    table.add_row("Linguagens", str(len(stats.get('languages', []))), f"{len(stats.get('languages', [])) * 15}")
    if game_data['activity_bonus'] > 0:
        table.add_row("Bônus Atividade", "", f"{game_data['activity_bonus']}")
    table.add_row("PONTUAÇÃO TOTAL", "", f"[bold green]{game_data['total_points']}[/bold green]")

    console.print(table)

    # Mostrar nível e progresso
    console.print(f"\nSeu nível: [bold yellow]{game_data['level_name']}[/bold yellow]")

    if game_data['next_level_points']:
        console.print(f"Progresso para próximo nível: [bold blue]{game_data['progress_to_next']:.1f}%[/bold blue]")
        console.print(f"Pontos necessários: [bold red]{game_data['next_level_points'] - game_data['total_points']}[/bold red]")

    # Mostrar conquistas
    if game_data['achievements']:
        achievements_table = Table(title="Conquistas Desbloqueadas")
        achievements_table.add_column("Badge", style="yellow")
        achievements_table.add_column("Descrição", style="white")
        achievements_table.add_column("Tier", style="green")

        for achievement in game_data['achievements']:
            tier_color = {"gold": "yellow", "silver": "white", "bronze": "orange"}.get(achievement['tier'], "white")
            achievements_table.add_row(
                achievement['name'],
                achievement['description'],
                f"[{tier_color}]{achievement['tier'].upper()}[/{tier_color}]"
            )

        console.print(achievements_table)

    # Mensagem de celebração
    celebration = gamification.get_celebration_message(game_data['level_name'])
    console.print(f"\n{celebration}")

    # Citação motivacional
    quote = gamification.get_random_quote()
    console.print(f"\n{quote}", style="italic cyan")

def show_detailed_stats(stats: dict):
    """Exibe estatísticas detalhadas"""
    from src.gamification import GamificationEngine

    gamification = GamificationEngine()

    # Mostrar informações detalhadas
    console.print(Panel(f"Análise Detalhada do Perfil GitHub", style="bold blue"))

    # Estatísticas gerais
    general_table = Table(title="Estatísticas Gerais")
    general_table.add_column("Métrica", style="cyan")
    general_table.add_column("Valor", style="green")

    general_table.add_row("Repositórios Públicos", str(stats.get('total_repos', 0)))
    general_table.add_row("Total de Stars", str(stats.get('total_stars', 0)))
    general_table.add_row("Total de Forks", str(stats.get('total_forks', 0)))
    general_table.add_row("Seguidores", str(stats.get('followers', 0)))
    general_table.add_row("Seguindo", str(stats.get('following', 0)))

    console.print(general_table)

    # Top linguagens
    if stats.get('languages'):
        lang_table = Table(title="Top Linguagens de Programação")
        lang_table.add_column("Linguagem", style="yellow")
        lang_table.add_column("Repositórios", style="green")

        for lang, count in list(stats['languages'].items())[:10]:
            lang_table.add_row(lang, str(count))

        console.print(lang_table)

    # Mostrar gamificação
    show_gamification_stats(stats)

    # Badges disponíveis
    badges = gamification.get_github_stats_badges(stats)
    console.print("\n[bold]Badges para usar no seu README:[/bold]")
    for badge in badges:
        console.print(f"   • {badge['label']}: [blue]{badge['url']}[/blue]")

if __name__ == "__main__":
    app()
