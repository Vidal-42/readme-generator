import os
import typer
from analisador import capturar_estrutura

app = typer.Typer()

@app.command()
def gerar():
    """Gera o README.md perguntando os dados e lendo a estrutura real."""
    
    typer.secho("📝 Responda às perguntas para gerar seu README", fg=typer.colors.CYAN, bold=True)

    # Coleta de informações via Terminal
    titulo = typer.prompt("1. Título do Projeto")
    subtitulo = typer.prompt("1b. Subtítulo/Slogan", default="Desenvolvido com Python")
    objetivo = typer.prompt("2. Objetivo (O que faz?)")
    decisoes = typer.prompt("3. Decisões Técnicas", default="Uso de Typer e venv")
    uso = typer.prompt("6. Comando de execução", default="python3 main.py")
    licenca = typer.prompt("9. Licença", default="MIT")

    typer.echo("\n🚀 Lendo estrutura de pastas e gerando arquivo...")

    # Captura a estrutura real usando o outro arquivo
    estrutura_real = capturar_estrutura()

    # Montagem do Template
    conteudo = f"""# {titulo}
> {subtitulo}

## 🎯 Objetivo do Projeto
{objetivo}

## 🛠️ Decisões Técnicas e Implementação
- {decisoes}

## 📂 Estrutura do Repositório
{estrutura_real}

## ⚙️ Guia de Configuração
1. **Ambiente:** `python3 -m venv .venv && source .venv/bin/activate`
2. **Dependências:** `pip install -r requirements.txt` (se houver)

## 🚀 Execução
```bash
{uso}
```

## 📊 6. Visualização de Evidências
Notas
[!TIP]
Use python3 main.py --help para ver os comandos

## 📄 8. Licença
Distribuído sob a licença {licenca}. Veja o arquivo LICENSE para mais detalhes.
"""
# Escrita do arquivo
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(conteudo)

    typer.secho("\n✨ README.md criado com sucesso!", fg=typer.colors.GREEN, bold=True)
if __name__ == "__main__":
    app()