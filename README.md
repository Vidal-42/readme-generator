# Assistente de Geração de Readme.md
> Ferramenta CLI interativa para criação profissional de documentação

## 🎯 Objetivo
Auxiliar o desenvolvimento de documentação de códigos em README's do Github, levando em consideração a linguagem de marcação Markdown para a edição do mesmo. A ferramenta visa aplicar boas práticas de documentação, extraindo automaticamente dependências, estrutura de diretórios e variáveis de ambiente e, a partir de algumas informações fornecidas pelo usuário, preencher o README no modelo Markdown e padronizado com Título, subtítulo, objetivo, tecnologias e dependências, passo a passo para executar o código e o tipo de licença do projeto.

## 🛠 Tecnologias e Dependências
- **Python:** `3.12+`

## 🧠 Decisões Técnicas
- Uso exclusivo de caminhos no formato Linux (Unix) para simplificar a lógica e evitar conversões complexas
- Arquitetura modular com separação entre análise (analisador.py), geração de template (gerador.py) e interface CLI (cli.py)
- Integração com entry point via pyproject.toml, permitindo instalação global e comando único 'gen-readme'

## 📋 Pré-requisitos

Antes de começar, certifique-se de ter as seguintes ferramentas instaladas e configuradas no seu ambiente:

* **Sistema Operacional:** Linux ou Windows com o **[WSL](https://learn.microsoft.com/pt-br/windows/wsl/install)** (Windows Subsystem for Linux) ativado. Recomendamos a distribuição **Ubuntu**.
* **[Git](https://git-scm.com/):** Para conseguir clonar o repositório.
* **[Python 3](https://www.python.org/):** A linguagem base do projeto. (Nota: o Ubuntu no WSL geralmente já vem com o Python, mas você precisará instalar o gerenciador de pacotes `pip` e o criador de ambientes virtuais `venv`).
* **Editor de Código (Recomendado):** **[VS Code](https://code.visualstudio.com/)** com a extensão oficial **WSL** instalada, para facilitar a integração entre o Windows e o terminal Linux.

## 📂 Estrutura do Projeto
```text
|-- meu_gerador_readme.egg-info/
|-- src/
        |-- __init__.py
        |-- analisador.py
        |-- cli.py
        |-- gerador.py
```
## Passo a passo para executar o código
1. Clone o repositório e entre na pasta: git clone https://github.com/Vidal-42/readme-generator.git && cd readme-generator
2. Crie e ative um ambiente virtual: python3 -m venv .venv && source .venv/bin/activate
3. Instale a ferramenta em modo editável: pip install -e .
4. Execute o gerador com o comando 'gen-readme .', com um ponto se quiser gerar um README.md na pasta que está atualmente ou informe o caminho de outro projeto no lugar do ponto.

## Licença
Distribuído sob a licença MIT.
