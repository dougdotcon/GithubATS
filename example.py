#!/usr/bin/env python3
"""
Exemplo de uso do GitHub ATS Resume Generator
"""

import os
from dotenv import load_dotenv
from src.github_analyzer import GitHubAnalyzer
from src.llm_client import LLMClient
from src.resume_generator import ResumeGenerator
from src.gamification import GamificationEngine

def main():
    """Exemplo de uso completo"""
    
    # Carregar variáveis de ambiente
    load_dotenv()
    
    # Verificar se as chaves estão configuradas
    github_token = os.getenv('GITHUB_TOKEN')
    openrouter_key = os.getenv('OPENROUTER_API_KEY')
    
    if not github_token:
        print("❌ GITHUB_TOKEN não encontrado!")
        print("💡 Configure com: export GITHUB_TOKEN='seu_token'")
        return
    
    if not openrouter_key:
        print("❌ OPENROUTER_API_KEY não encontrado!")
        print("💡 Configure no arquivo .env")
        return
    
    print("🚀 Exemplo de uso do GitHub ATS Resume Generator\n")
    
    try:
        # 1. Analisar GitHub
        print("📊 Analisando perfil GitHub...")
        analyzer = GitHubAnalyzer(github_token)
        user_data = analyzer.get_user_info()
        print(f"👋 Usuário: {user_data['name']} (@{user_data['login']})")
        
        # 2. Analisar repositórios
        print("📦 Analisando repositórios...")
        repos_data = analyzer.analyze_repositories(limit=5)  # Limitar para exemplo
        print(f"📁 Encontrados {len(repos_data)} repositórios")
        
        # 3. Obter estatísticas
        print("📈 Calculando estatísticas...")
        stats = analyzer.get_stats()
        print(f"⭐ Total de stars: {stats['total_stars']}")
        print(f"🍴 Total de forks: {stats['total_forks']}")
        
        # 4. Gamificação
        print("🎮 Calculando gamificação...")
        gamification = GamificationEngine()
        game_data = gamification.calculate_score(stats)
        print(f"🎯 Pontuação: {game_data['total_points']}")
        print(f"🏅 Nível: {game_data['level_emoji']} {game_data['level_name']}")
        
        # 5. Processar com LLM (apenas primeiro repo para exemplo)
        if repos_data:
            print("🤖 Processando com LLM...")
            llm_client = LLMClient()
            
            # Processar apenas o primeiro repositório para exemplo
            first_repo = repos_data[0]
            analysis = llm_client._analyze_single_repository(first_repo)
            
            if analysis:
                print(f"✅ Análise LLM do repo '{first_repo['name']}':")
                print(f"   📝 Título: {analysis.get('llm_title', 'N/A')}")
                print(f"   📄 Descrição: {analysis.get('llm_description', 'N/A')}")
                print(f"   🛠️ Skills: {', '.join(analysis.get('llm_skills', []))}")
            else:
                print("⚠️ Análise LLM não disponível (usando dados básicos)")
        
        # 6. Gerar currículo de exemplo
        print("📝 Gerando currículo de exemplo...")
        
        # Preparar dados (com ou sem análise LLM)
        if repos_data and analysis:
            repos_data[0].update(analysis)
        
        resume_data = {
            'user': user_data,
            'repositories': repos_data,
            'stats': stats
        }
        
        # Gerar em diferentes formatos
        generator = ResumeGenerator(theme='light', gamified=True)
        
        # Markdown
        generator.generate(resume_data, 'output/exemplo.md', 'markdown')
        print("✅ Currículo Markdown gerado: output/exemplo.md")
        
        # HTML
        generator.generate(resume_data, 'output/exemplo.html', 'html')
        print("✅ Currículo HTML gerado: output/exemplo.html")
        
        # Tentar PDF (pode falhar se WeasyPrint não estiver configurado)
        try:
            generator.generate(resume_data, 'output/exemplo.pdf', 'pdf')
            print("✅ Currículo PDF gerado: output/exemplo.pdf")
        except Exception as e:
            print(f"⚠️ PDF não pôde ser gerado: {e}")
        
        print("\n🎉 Exemplo concluído com sucesso!")
        print("📁 Verifique a pasta 'output' para os arquivos gerados")
        
        # Mostrar citação motivacional
        quote = gamification.get_random_quote()
        print(f"\n✨ {quote}")
        
    except Exception as e:
        print(f"❌ Erro durante execução: {e}")
        print("💡 Verifique suas configurações e conexão com a internet")

if __name__ == '__main__':
    main()
