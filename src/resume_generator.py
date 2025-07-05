"""
Gerador de currículos em múltiplos formatos
"""

import os
from pathlib import Path
from typing import Dict, Any
from jinja2 import Environment, FileSystemLoader
import weasyprint
import markdown
from src.llm_client import LLMClient

class ResumeGenerator:
    """Gerador de currículos com múltiplos temas e formatos"""
    
    def __init__(self, theme: str = "light", gamified: bool = False):
        """Inicializa o gerador"""
        self.theme = theme
        self.gamified = gamified
        
        # Configurar Jinja2
        template_dir = Path(__file__).parent.parent / "templates"
        self.env = Environment(loader=FileSystemLoader(str(template_dir)))
        
        # Cliente LLM para resumo profissional
        self.llm_client = LLMClient()
        
    def generate(self, resume_data: Dict[str, Any], output_path: str, format: str = "pdf"):
        """Gera o currículo no formato especificado"""
        
        # Gerar resumo profissional com LLM
        professional_summary = self._generate_professional_summary(
            resume_data['user'], 
            resume_data['stats']
        )
        
        # Preparar dados para template
        template_data = {
            'user': resume_data['user'],
            'repositories': resume_data['repositories'],
            'stats': resume_data['stats'],
            'professional_summary': professional_summary,
            'gamified': self.gamified,
            'theme': self.theme
        }
        
        if format.lower() == "pdf":
            self._generate_pdf(template_data, output_path)
        elif format.lower() == "html":
            self._generate_html(template_data, output_path)
        elif format.lower() == "markdown":
            self._generate_markdown(template_data, output_path)
        else:
            raise ValueError(f"Formato não suportado: {format}")
    
    def _generate_professional_summary(self, user_data: Dict, stats: Dict) -> str:
        """Gera resumo profissional usando LLM"""
        try:
            return self.llm_client.generate_professional_summary(user_data, stats)
        except Exception as e:
            print(f"Erro ao gerar resumo profissional: {e}")
            # Fallback para resumo padrão
            return self._generate_default_summary(user_data, stats)
    
    def _generate_default_summary(self, user_data: Dict, stats: Dict) -> str:
        """Gera resumo padrão sem LLM"""
        name = user_data.get('name', 'Desenvolvedor')
        total_repos = stats.get('total_repos', 0)
        languages = list(stats.get('languages', {}).keys())[:3]
        
        summary = f"Desenvolvedor apaixonado por tecnologia com {total_repos} repositórios públicos no GitHub. "
        
        if languages:
            summary += f"Experiência em {', '.join(languages)} e outras tecnologias. "
        
        summary += "Focado em criar soluções inovadoras e contribuir para projetos open source."
        
        return summary
    
    def _generate_pdf(self, template_data: Dict, output_path: str):
        """Gera PDF usando WeasyPrint"""
        try:
            # Primeiro gerar HTML
            html_content = self._render_html_template(template_data)
            
            # Converter para PDF
            html_doc = weasyprint.HTML(string=html_content)
            html_doc.write_pdf(output_path)
            
        except Exception as e:
            print(f"Erro ao gerar PDF: {e}")
            # Fallback: gerar HTML se PDF falhar
            html_path = output_path.replace('.pdf', '.html')
            self._generate_html(template_data, html_path)
            print(f"PDF falhou, HTML gerado em: {html_path}")
    
    def _generate_html(self, template_data: Dict, output_path: str):
        """Gera arquivo HTML"""
        html_content = self._render_html_template(template_data)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
    
    def _generate_markdown(self, template_data: Dict, output_path: str):
        """Gera arquivo Markdown"""
        template = self.env.get_template('base.md.j2')
        markdown_content = template.render(**template_data)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
    
    def _render_html_template(self, template_data: Dict) -> str:
        """Renderiza template HTML baseado no tema"""
        template_name = f"{self.theme}.html.j2"
        
        try:
            template = self.env.get_template(template_name)
            return template.render(**template_data)
        except Exception as e:
            print(f"Erro ao carregar template {template_name}: {e}")
            # Fallback para template light
            template = self.env.get_template('light.html.j2')
            return template.render(**template_data)
    
    def preview_html(self, resume_data: Dict) -> str:
        """Gera preview HTML para visualização"""
        professional_summary = self._generate_professional_summary(
            resume_data['user'], 
            resume_data['stats']
        )
        
        template_data = {
            'user': resume_data['user'],
            'repositories': resume_data['repositories'],
            'stats': resume_data['stats'],
            'professional_summary': professional_summary,
            'gamified': self.gamified,
            'theme': self.theme
        }
        
        return self._render_html_template(template_data)
    
    def get_available_themes(self) -> list:
        """Retorna lista de temas disponíveis"""
        return ['light', 'dark', 'cyberpunk']
    
    def get_available_formats(self) -> list:
        """Retorna lista de formatos disponíveis"""
        return ['pdf', 'html', 'markdown']
