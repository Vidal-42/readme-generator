# Gerador de README usando Python e WSL (Subsistema do Windows para Windows)
> Projeto Tech - Flisol

## 🎯 Objetivo 
O objetivo deste projeto é automatizar a criação de arquivos README.md para repositórios do GitHub. Por meio de uma interface de linha de comando (CLI), o sistema coleta informações essenciais do desenvolvedor e analisa automaticamente a estrutura de pastas do projeto (utilizando o comando tree). O resultado final é um arquivo de documentação padronizado, profissional e pronto para uso, eliminando o trabalho repetitivo de formatação manual e garantindo que as boas práticas de documentação sejam seguidas desde o início do desenvolvimento.

## 🎲 Decisões Técnicas e Implementação
- *Estrutura Simplificada:* O projeto foi desenvolvido em uma estrutura plana (flat structure), onde toda a lógica residia na raiz do diretório. Isso permitiu um ciclo de desenvolvimento rápido para validação da prova de conceito.
- *Acoplamento Direto:* O main.py atuava como controlador central (Typer, Markdown e persistência) e o analisador.py funcionava como módulo utilitário auxiliar para o sistema de arquivos.
- *Integração via Subprocess:* Uso da biblioteca subprocess para execução do tree e captura de stdout.
- *Gerenciamento:* Uso de .venv isolado e requirements.txt para reprodutibilidade.

## 📂 Estrutura 
```bash
.
├── analisador.py
├── main.py
└── requirements.txt

1 directory, 3 files

```

## 📋 Pré-requisitos

Antes de começar, certifique-se de ter as seguintes ferramentas instaladas e configuradas no seu ambiente:

* **Sistema Operacional:** Linux ou Windows com o **[WSL](https://learn.microsoft.com/pt-br/windows/wsl/install)** (Windows Subsystem for Linux) ativado. Recomendamos a distribuição **Ubuntu**.
* **[Git](https://git-scm.com/):** Para conseguir clonar o repositório.
* **[Python 3](https://www.python.org/):** A linguagem base do projeto. (Nota: o Ubuntu no WSL geralmente já vem com o Python, mas você precisará instalar o gerenciador de pacotes `pip` e o criador de ambientes virtuais `venv`).
* **Editor de Código (Recomendado):** **[VS Code](https://code.visualstudio.com/)** com a extensão oficial **WSL** instalada, para facilitar a integração entre o Windows e o terminal Linux.


## 🖥️ Instalação e Execução 

1. **Clone o repositório e entre no diretório:** 
```bash
git clone https://github.com/Vidal-42/readme-generator.git
cd readme-generator/projeto-flisol
```

2. **Garanta que o utilitário tree está no seu Linux com o comando:**
```bash
sudo apt install tree -y
```

2. **Configure o ambiente virtual (criação e ativação do ambiente):** 
```bash
python3 -m venv .venv
source .venv/bin/activate
```
3. **Instale as dependências:** 
```bash
pip install -r requirements.txt
```

4. **Execute o gerador de README's:** 
```bash
python3 main.py
```


## ⚙️ Passo a Passo para Configuração do Ambiente (Teste inicial)
1. **Instalação das dependências do sistema:**
```bash
sudo apt install python3-pip python3-venv tree -y
```
2. **Criação do diretório do projeto:**
```bash
mkdir gerador-readme-GitHub
```
3. **Acesso ao diretório:**
```bash
cd gerador-readme-Git
```
4. **Criação do ambiente virtual:**
```bash
python3 -m venv .venv
```
5. **Ativação do ambiente virtual:**
```bash
source .venv/bin/activate
```
6. **Instalação do framework de CLI:**
```bash
pip install "typer[all]"
```  
7. **No terminal do VS Code, execute:**
```bash
code .
```
8. **Aperte a tecla F1 (ou Ctrl + Shift + P).**
9. **Digite e selecione: WSL: Open Folder in WSL[...] e selecione o caminho desejado**
10. **Validação da instalação** - Crie um arquivo main.py e execute o código abaixo para testar o funcionamento do Typer:
```bash
import typer

app = typer.Typer()

@app.command()
def teste_saudacao(nome: str):
    #Comando para testar o ambiente.
    print(f"Oi, nome! O Typer está funcionando no seu WSL.")

if __name__ == "__main__":
    app() 
```

11.**Execute o comando:**
```bash
python3 main.py <SeuNome>
```

## 📊 Dica
> [!TIP]
> Use python3 main.py --help para ver os comandos

## 📄 8. Licença
Distribuído sob a licença MIT. 
