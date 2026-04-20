# Assistente de Geração de Readme.md
> Ferramenta CLI interativa para criação profissional de documentação

## 🎯 Objetivo
Automatizar a geração de README.md para projetos Python, aplicando boas práticas de documentação, extraindo automaticamente dependências, estrutura de diretórios e variáveis de ambiente, além de permitir inclusão de evidências visuais.

## 🛠 Tecnologias e Dependências
- **Python:** `3.12+`

## 🧠 Decisões Técnicas
- Uso exclusivo de caminhos no formato Linux (Unix) para simplificar a lógica e evitar conversões complexas
- Arquitetura modular com separação entre análise (analisador.py), geração de template (gerador.py) e interface CLI (cli.py)
- Integração com entry point via pyproject.toml, permitindo instalação global e comando único 'gen-readme'
- Validação de regras de negócio: pasta de evidências ('evidencias/') e extensões de imagem suportadas

## 📂 Estrutura do Projeto
```text
|-- meu_gerador_readme.egg-info/
|-- src/
        |-- __init__.py
        |-- analisador.py
        |-- cli.py
        |-- gerador.py
```

## Guia de execução
```bash
y
```


## Licença
Distribuído sob a licença MIT.
