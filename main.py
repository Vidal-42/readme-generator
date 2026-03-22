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
    subtitulo = typer.prompt("1b. Subtítulo")
    objetivo = typer.prompt("2. Objetivo (O que faz?)")
    decisoes = typer.prompt("3. Decisões Técnicas")
    ambiente = typer.prompt("4. Ambiente da execução")
    dependencias = typer.prompt("5. dependencias")
    uso = typer.prompt("5. Comando de execução")
    licenca = typer.prompt("6. Licença")

    typer.echo("\n🚀 Lendo estrutura de pastas e gerando arquivo...")

    # Captura a estrutura real usando o outro arquivo
    estrutura_real = capturar_estrutura()

    # Montagem do Template
    conteudo = f"""# {titulo}
> {subtitulo}

## 🎯 Objetivo 
{objetivo}

## 🎲 Decisões Técnicas e Implementação
- {decisoes}

## 📂 Estrutura 
{estrutura_real}

## ⚙️ Guia de Configuração
1. **Ambiente:** {ambiente}
2. **Dependências:** {dependencias}

## 🚀 Execução
```bash
{uso}
```

## 📊 6. Visualização de Evidências
> [!TIP]
> Use python3 main.py --help para ver os comandos

## 📄 8. Licença
Distribuído sob a licença {licenca}. Veja o arquivo LICENSE para mais detalhes.
"""
# Escrita do arquivo
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(conteudo)

    typer.secho("\n✨ README.md criado com sucesso!", fg=typer.colors.GREEN, bold=True)
if __name__ == "__main__":
    app()