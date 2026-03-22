# Gerador de README usando Python
> Projeto - Flisol

## 🎯 Objetivo 
O objetivo deste projeto é automatizar a criação de arquivos README.md para repositórios do GitHub. Por meio de uma interface de linha de comando (CLI), o sistema coleta informações essenciais do desenvolvedor e analisa automaticamente a estrutura de pastas do projeto (utilizando o comando tree). O resultado final é um arquivo de documentação padronizado, profissional e pronto para uso, eliminando o trabalho repetitivo de formatação manual e garantindo que as boas práticas de documentação sejam seguidas desde o início do desenvolvimento.

## 🎲 Decisões Técnicas e Implementação
- *Estrutura Simplificada:* O projeto foi desenvolvido em uma estrutura plana (flat structure), onde toda a lógica residia na raiz do diretório. Isso permitiu um ciclo de desenvolvimento rápido para validação da prova de conceito. <br> *Acoplamento Direto:* O main.py atuava como controlador central (Typer, Markdown e persistência) e o analisador.py funcionava como módulo utilitário auxiliar para o sistema de arquivos. <br> *Integração via Subprocess:* Uso da biblioteca subprocess para execução do tree e captura de stdout. <br> *Gerenciamento:* Uso de .venv isolado e requirements.txt para reprodutibilidade.

## 📂 Estrutura 
```bash
.
├── analisador.py
├── main.py
└── requirements.txt

1 directory, 3 files

```

## ⚙️ Guia de Configuração
1. **Ambiente:** `python3 -m venv .venv && source .venv/bin/activate`
2. **Dependências:** `pip install -r requirements.txt`

## 🚀 Execução
```bash
python main.py
```

## 📊 6. Visualização de Evidências
> [!TIP]
> Use python3 main.py --help para ver os comandos

## 📄 8. Licença
Distribuído sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
