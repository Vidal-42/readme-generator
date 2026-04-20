import typer
import os
import re
from pathlib import Path
from src.analisador import (
    capturar_estrutura_python,
    detectar_dependencias,
    sugerir_resumo_projeto,
    detectar_variaveis_ambiente,
    sugerir_comando_execucao,
    obter_versao_python
)
from src.gerador import montar_template

app = typer.Typer()

def validar_caminho_linux(caminho: str) -> Path:
    """Converte o caminho para Path, expande '~' e verifica se é um formato Linux válido."""
    caminho_expandido = os.path.expanduser(caminho)
    return Path(caminho_expandido).resolve()

@app.callback(invoke_without_command=True)
def main(
    ctx: typer.Context,
    caminho: str = typer.Argument(None, help="Caminho do projeto no formato Linux (ex: /home/user/projeto).")
):
    """Gera um README.md para o projeto de forma interativa."""
    if ctx.invoked_subcommand is not None:
        return

    typer.echo("🚀 Gerador de README - Iniciando...")

    if caminho:
        caminho_projeto = validar_caminho_linux(caminho)
    else:
        pasta_atual = Path.cwd()
        typer.echo(f"\n💡 Dica: Enter usa a pasta atual: {pasta_atual}")
        typer.echo("   Informe um caminho no formato Linux (ex: /home/usuario/projeto)")
        caminho_raw = typer.prompt("Informe o caminho do projeto alvo", default=str(pasta_atual))
        caminho_projeto = validar_caminho_linux(caminho_raw)

    if not caminho_projeto.exists():
        typer.echo(f"❌ Erro: O sistema não encontrou o caminho: {caminho_projeto}")
        raise typer.Exit(1)

    typer.echo(f"✅ Projeto localizado: {caminho_projeto}")

    # Coleta de dados
    typer.echo("🔍 Analisando arquivos...")
    deps_sug = detectar_dependencias(str(caminho_projeto))
    resumo_sug = sugerir_resumo_projeto(str(caminho_projeto))
    cmd_sug = sugerir_comando_execucao(str(caminho_projeto), deps_sug)
    env_vars = detectar_variaveis_ambiente(str(caminho_projeto))

    nome_projeto = caminho_projeto.name.replace('-', ' ').replace('_', ' ').title()
    titulo = typer.prompt("\nTítulo do Projeto", default=nome_projeto)
    subtitulo = typer.prompt("Subtítulo", default="Projeto de Desenvolvimento Python")
    objetivo = typer.prompt("Objetivo", default=resumo_sug)

    dependencias = ""
    if deps_sug and typer.confirm(f"Incluir dependências encontradas [{deps_sug}]?", default=True):
        dependencias = deps_sug

    decisoes = ""
    if typer.confirm("Adicionar decisões técnicas em tópicos?", default=True):
        qtd = typer.prompt("Quantos tópicos?", type=int, default=1)
        decisoes = "\n".join([f"- {typer.prompt(f'Tópico {i+1}')}" for i in range(qtd)])
    else:
        decisoes = typer.prompt("Decisões técnicas")

    # --- Coleta de Pré-requisitos (NOVO) ---
    typer.echo("\n📋 Configure os pré-requisitos necessários para rodar o projeto:")
    if typer.confirm("Deseja adicionar uma lista de pré-requisitos?", default=True):
        qtd_pre = typer.prompt("Quantos pré-requisitos deseja listar?", type=int, default=3)
        pre_requisitos = []
        for i in range(qtd_pre):
            pre = typer.prompt(f"Pré-requisito {i+1}")
            pre_requisitos.append(f"- {pre}")
        pre_requisitos_md = "\n".join(pre_requisitos)
    else:
        pre_requisitos_md = ""

    # --- Passo a passo de execução ---
    typer.echo("\n📖 Configure o passo a passo para executar o código (quem for usar seu projeto):")
    if typer.confirm("Deseja criar uma lista de passos numerados?", default=True):
        qtd_passos = typer.prompt("Quantos passos?", type=int, default=2)
        passos = []
        for i in range(qtd_passos):
            passo = typer.prompt(f"Passo {i+1}")
            passos.append(f"{i+1}. {passo}")
        execucao_md = "\n".join(passos)
    else:
        comando_unico = typer.prompt("Comando único de execução", default=cmd_sug)
        execucao_md = f"Execute o comando abaixo:\n```bash\n{comando_unico}\n```"

    licenca = typer.prompt("Licença", default="MIT")

    # Geração do conteúdo
    estrutura = capturar_estrutura_python(str(caminho_projeto))
    dados = {
        "titulo": titulo,
        "subtitulo": subtitulo,
        "objetivo": objetivo,
        "decisoes": decisoes,
        "pre_requisitos": pre_requisitos_md,
        "execucao": execucao_md,
        "licenca": licenca,
        "dependencias": dependencias,
        "variaveis_ambiente": env_vars,
        "versao_python": obter_versao_python()
    }

    conteudo = montar_template(dados, estrutura)

    saida = caminho_projeto / "README.md"
    try:
        saida.write_text(conteudo, encoding="utf-8", errors="replace")
        typer.echo(f"\n✨ Sucesso! README gerado em: {saida}")
    except Exception as e:
        typer.echo(f"❌ Erro ao salvar: {e}")

if __name__ == "__main__":
    app()