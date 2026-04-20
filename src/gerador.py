def montar_template(dados, estrutura):
    """Formata o dicionário de dados em um README.md profissional."""
    
    # Limpeza de caracteres que podem bugar no Windows/WSL
    for k, v in dados.items():
        if isinstance(v, str):
            dados[k] = v.replace('\udcc2', '').strip()

    secao_tecnologias = f"## 🛠 Tecnologias e Dependências\n- **Python:** `{dados['versao_python']}+`"
    if dados.get('dependencias'):
        secao_tecnologias += f"\n- **Pacotes Principais:** {dados['dependencias']}"

    secao_env = ""
    if dados.get('variaveis_ambiente'):
        secao_env = "## ⚙️ Configuração de Ambiente\nCrie um `.env` com:\n```text\n"
        secao_env += "\n".join([f"{v}=" for v in dados['variaveis_ambiente']])
        secao_env += "\n```\n\n"

    return f"""# {dados['titulo']}
> {dados['subtitulo']}

## 🎯 Objetivo
{dados['objetivo']}

{secao_tecnologias}

{secao_env}## 🧠 Decisões Técnicas
{dados['decisoes']}

## 📂 Estrutura do Projeto
```text
{estrutura}
```
## Passo a passo para executar o código
{dados['execucao']}

## Licença
Distribuído sob a licença {dados['licenca']}.
"""