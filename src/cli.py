import typer
import os
import re
from analisador import (
    capturar_estrutura_python, detectar_dependencias, 
    sugerir_resumo_projeto, detectar_variaveis_ambiente, 
    sugerir_comando_execucao, obter_versao_python
)
from gerador import montar_template

app = typer.Typer()

def corrigir_caminho_wsl(caminho_cru):
    r"""
    Converte caminhos do Windows Explorer (C:\...) para o formato WSL (/mnt/c/...).
    Se o caminho já estiver no formato Linux, ele apenas limpa as aspas.
    """
    caminho = caminho_cru.strip().strip('"').strip("'")
    
    # Se começa com C:\ ou c:\
    if re.match(r'^[a-zA-Z]:\\', caminho):
        letra_drive = caminho[0].lower()
        caminho_convertido = caminho[2:].replace('\\', '/')
        return f"/mnt/{letra_drive}{caminho_convertido}"
    
    # Se apenas tem barras invertidas, mas não é drive (ex: \pasta\sub)
    return caminho.replace('\\', '/')

@app.command()
def gerar(
    caminho: str = typer.Argument(None, help="Caminho do projeto (opcional). Se não informado, usa a pasta atual.")
):
    """
    Gera um README.md para o projeto.
    Se não passar o caminho, pergunta com o diretório atual como sugestão.
    """
    typer.echo("🚀 Gerador de README - Iniciando...")
    
    # Se o usuário passou o caminho como argumento, usa ele
    if caminho:
        caminho_projeto = os.path.abspath(corrigir_caminho_wsl(caminho))
    else:
        # Pergunta com valor padrão = diretório atual
        pasta_atual = os.getcwd()
        typer.echo(f"\n💡 Dica: Enter usa a pasta atual: {pasta_atual}")
        typer.echo("   Ou cole um caminho do Windows (C:\\...\\pasta)")
        caminho_raw = typer.prompt("Informe o caminho do projeto alvo", default=pasta_atual)
        caminho_projeto = os.path.abspath(corrigir_caminho_wsl(caminho_raw))
    
    if not os.path.exists(caminho_projeto):
        typer.echo(f"❌ Erro: O sistema não encontrou o caminho: {caminho_projeto}")
        raise typer.Exit()

    typer.echo(f"✅ Projeto localizado: {caminho_projeto}")

    # Coleta de dados (Análise)
    typer.echo("🔍 Analisando arquivos...")
    deps_sug = detectar_dependencias(caminho_projeto)
    resumo_sug = sugerir_resumo_projeto(caminho_projeto)
    cmd_sug = sugerir_comando_execucao(caminho_projeto, deps_sug)
    env_vars = detectar_variaveis_ambiente(caminho_projeto)
    
    # Interface de Preenchimento
    nome_projeto = os.path.basename(caminho_projeto).replace('-', ' ').replace('_', ' ').title()
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

    uso = typer.prompt("Comando de execução", default=cmd_sug)
    licenca = typer.prompt("Licença", default="MIT")

    # Geração do Conteúdo
    estrutura = capturar_estrutura_python(caminho_projeto)
    dados = {
        "titulo": titulo, "subtitulo": subtitulo, "objetivo": objetivo,
        "decisoes": decisoes, "uso": uso, "licenca": licenca,
        "evidencias": "", "dependencias": dependencias,
        "variaveis_ambiente": env_vars, "versao_python": obter_versao_python()
    }

    conteudo = montar_template(dados, estrutura)
    
    # Escrita final
    saida = os.path.join(caminho_projeto, "README.md")
    try:
        with open(saida, "w", encoding="utf-8", errors="replace") as f:
            f.write(conteudo)
        typer.echo(f"\n✨ Sucesso! README gerado em: {saida}")
    except Exception as e:
        typer.echo(f"❌ Erro ao salvar: {e}")

if __name__ == "__main__":
    app()
