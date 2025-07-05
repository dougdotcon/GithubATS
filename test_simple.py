#!/usr/bin/env python3
"""
Teste simples para verificar se tudo está funcionando
"""

def test_imports():
    """Testa imports básicos"""
    try:
        import typer
        print("✅ Typer importado com sucesso")
        
        from rich.console import Console
        print("✅ Rich importado com sucesso")
        
        from src.gamification import GamificationEngine
        print("✅ GamificationEngine importado com sucesso")
        
        from src.github_analyzer import GitHubAnalyzer
        print("✅ GitHubAnalyzer importado com sucesso")
        
        from src.llm_client import LLMClient
        print("✅ LLMClient importado com sucesso")
        
        from src.resume_generator import ResumeGenerator
        print("✅ ResumeGenerator importado com sucesso")
        
        return True
    except Exception as e:
        print(f"❌ Erro no import: {e}")
        return False

def test_gamification():
    """Testa sistema de gamificação"""
    try:
        from src.gamification import GamificationEngine
        
        engine = GamificationEngine()
        
        # Dados de teste
        stats = {
            'total_repos': 10,
            'total_stars': 25,
            'total_forks': 5,
            'followers': 15,
            'languages': {'Python': 5, 'JavaScript': 3}
        }
        
        result = engine.calculate_score(stats)
        
        print(f"✅ Pontuação calculada: {result['total_points']}")
        print(f"✅ Nível: {result['level_name']}")
        print(f"✅ Conquistas: {len(result['achievements'])}")
        
        quote = engine.get_random_quote()
        print(f"✅ Citação: {quote[:50]}...")
        
        return True
    except Exception as e:
        print(f"❌ Erro na gamificação: {e}")
        return False

def test_templates():
    """Testa se os templates existem"""
    import os
    
    templates = [
        'templates/base.md.j2',
        'templates/light.html.j2',
        'templates/dark.html.j2',
        'templates/cyberpunk.html.j2'
    ]
    
    for template in templates:
        if os.path.exists(template):
            print(f"✅ Template encontrado: {template}")
        else:
            print(f"❌ Template não encontrado: {template}")
            return False
    
    return True

def main():
    """Executa todos os testes"""
    print("🧪 Executando testes simples...\n")
    
    tests = [
        ("Imports", test_imports),
        ("Gamificação", test_gamification),
        ("Templates", test_templates)
    ]
    
    passed = 0
    total = len(tests)
    
    for name, test_func in tests:
        print(f"\n📋 Testando {name}:")
        if test_func():
            passed += 1
            print(f"✅ {name} passou!")
        else:
            print(f"❌ {name} falhou!")
    
    print(f"\n📊 Resultado: {passed}/{total} testes passaram")
    
    if passed == total:
        print("🎉 Todos os testes passaram! O projeto está funcionando.")
    else:
        print("⚠️ Alguns testes falharam. Verifique os erros acima.")

if __name__ == '__main__':
    main()
