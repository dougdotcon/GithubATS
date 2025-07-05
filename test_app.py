#!/usr/bin/env python3
"""
Testes básicos para o GitHub ATS Resume Generator
"""

import unittest
from unittest.mock import Mock, patch
from src.gamification import GamificationEngine
from src.llm_client import LLMClient

class TestGamificationEngine(unittest.TestCase):
    """Testes para o sistema de gamificação"""
    
    def setUp(self):
        self.engine = GamificationEngine()
        self.sample_stats = {
            'total_repos': 10,
            'total_stars': 25,
            'total_forks': 5,
            'followers': 15,
            'languages': {'Python': 5, 'JavaScript': 3, 'Go': 2}
        }
    
    def test_calculate_score(self):
        """Testa cálculo de pontuação"""
        result = self.engine.calculate_score(self.sample_stats)
        
        # Verificar se todos os campos estão presentes
        self.assertIn('total_points', result)
        self.assertIn('level', result)
        self.assertIn('level_name', result)
        self.assertIn('achievements', result)
        
        # Verificar cálculo básico de pontos
        expected_points = (25 * 10) + (5 * 5) + (10 * 2) + (3 * 15) + (15 * 3)  # stars + forks + repos + languages + followers
        self.assertGreaterEqual(result['total_points'], expected_points)
    
    def test_level_determination(self):
        """Testa determinação de níveis"""
        # Teste nível baixo
        low_stats = {'total_repos': 1, 'total_stars': 0, 'total_forks': 0, 'followers': 0, 'languages': {'Python': 1}}
        result = self.engine.calculate_score(low_stats)
        self.assertEqual(result['level'], 'padawan')
        
        # Teste nível alto
        high_stats = {'total_repos': 50, 'total_stars': 100, 'total_forks': 50, 'followers': 100, 'languages': {'Python': 10, 'JS': 5}}
        result = self.engine.calculate_score(high_stats)
        self.assertEqual(result['level'], 'ninja_master')
    
    def test_achievements_calculation(self):
        """Testa cálculo de conquistas"""
        result = self.engine.calculate_score(self.sample_stats)
        achievements = result['achievements']
        
        # Deve ter pelo menos uma conquista
        self.assertGreater(len(achievements), 0)
        
        # Verificar estrutura das conquistas
        for achievement in achievements:
            self.assertIn('name', achievement)
            self.assertIn('emoji', achievement)
            self.assertIn('description', achievement)
            self.assertIn('tier', achievement)
    
    def test_random_quote(self):
        """Testa geração de citações aleatórias"""
        quote = self.engine.get_random_quote()
        self.assertIsInstance(quote, str)
        self.assertGreater(len(quote), 0)
    
    def test_badge_generation(self):
        """Testa geração de badges"""
        badges = self.engine.get_github_stats_badges(self.sample_stats)
        
        self.assertGreater(len(badges), 0)
        
        for badge in badges:
            self.assertIn('label', badge)
            self.assertIn('value', badge)
            self.assertIn('color', badge)
            self.assertIn('url', badge)
            self.assertTrue(badge['url'].startswith('https://img.shields.io/'))

class TestLLMClient(unittest.TestCase):
    """Testes para o cliente LLM"""
    
    def setUp(self):
        # Mock da API key para testes
        with patch.dict('os.environ', {'OPENROUTER_API_KEY': 'test-key'}):
            self.client = LLMClient()
    
    def test_initialization(self):
        """Testa inicialização do cliente"""
        self.assertEqual(self.client.api_key, 'test-key')
        self.assertEqual(self.client.base_url, 'https://openrouter.ai/api/v1')
        self.assertIn('Authorization', self.client.headers)
    
    def test_prepare_repository_context(self):
        """Testa preparação do contexto do repositório"""
        repo_data = {
            'name': 'test-repo',
            'description': 'A test repository',
            'language': 'Python',
            'stars': 10,
            'forks': 2,
            'topics': ['python', 'testing'],
            'languages': {'Python': 100, 'JavaScript': 50},
            'readme_content': 'This is a test README content'
        }
        
        context = self.client._prepare_repository_context(repo_data)
        
        self.assertIn('test-repo', context)
        self.assertIn('A test repository', context)
        self.assertIn('Python', context)
        self.assertIn('10', context)  # stars
        self.assertIn('python, testing', context)  # topics

class TestIntegration(unittest.TestCase):
    """Testes de integração"""
    
    def test_full_workflow_mock(self):
        """Testa fluxo completo com dados mockados"""
        # Dados de exemplo
        user_data = {
            'name': 'Test User',
            'email': 'test@example.com',
            'login': 'testuser'
        }
        
        repos_data = [
            {
                'name': 'test-repo',
                'description': 'Test repository',
                'language': 'Python',
                'stars': 5,
                'forks': 1,
                'topics': ['python'],
                'languages': {'Python': 100},
                'readme_content': 'Test README',
                'url': 'https://github.com/testuser/test-repo'
            }
        ]
        
        stats = {
            'total_repos': 1,
            'total_stars': 5,
            'total_forks': 1,
            'followers': 0,
            'languages': {'Python': 1}
        }
        
        # Testar gamificação
        engine = GamificationEngine()
        game_result = engine.calculate_score(stats)
        
        self.assertIsInstance(game_result, dict)
        self.assertIn('total_points', game_result)
        self.assertIn('level', game_result)

def run_tests():
    """Executa todos os testes"""
    unittest.main(verbosity=2)

if __name__ == '__main__':
    run_tests()
