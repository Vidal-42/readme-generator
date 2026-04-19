import os
import sys
import re

try:
    import tomllib
except ImportError:
    tomllib = None

def capturar_estrutura_python(diretorio_alvo="."):
    tree = []
    ignorar = {'.git', '__pycache__', '.venv', 'venv', '.pytest_cache', '.vscode', '.amazonq'}
    for raiz, diretorios, arquivos in os.walk(diretorio_alvo):
        diretorios[:] = [d for d in diretorios if d not in ignorar]
        nivel = raiz.replace(diretorio_alvo, '').count(os.sep)
        indentacao = '    ' * nivel
        nome_pasta = os.path.basename(raiz) or diretorio_alvo
        tree.append(f"{indentacao}|-- {nome_pasta}/")
        sub_indentacao = '    ' * (nivel + 1)
        for arq in arquivos:
            if arq.endswith('.py'):
                tree.append(f"{sub_indentacao}|-- {arq}")
    return "\n".join(tree)

def detectar_dependencias(diretorio_alvo="."):
    caminho_req = os.path.join(diretorio_alvo, "requirements.txt")
    if os.path.exists(caminho_req):
        try:
            with open(caminho_req, "r", encoding="utf-8") as f:
                deps = [re.split(r'[=<>~]', line)[0].strip() for line in f if line.strip() and not line.startswith('#')]
                return ", ".join(deps)
        except: pass
    return ""

def sugerir_resumo_projeto(diretorio_alvo="."):
    caminho_toml = os.path.join(diretorio_alvo, "pyproject.toml")
    if tomllib and os.path.exists(caminho_toml):
        try:
            with open(caminho_toml, "rb") as f:
                data = tomllib.load(f)
                desc = data.get("project", {}).get("description")
                if desc: return desc
        except: pass
    nome = os.path.basename(os.path.abspath(diretorio_alvo))
    return f"Projeto focado em {nome.replace('-', ' ').replace('_', ' ').capitalize()}."

def detectar_variaveis_ambiente(diretorio_alvo="."):
    for nome_arq in [".env.example", ".env"]:
        caminho_env = os.path.join(diretorio_alvo, nome_arq)
        if os.path.exists(caminho_env):
            try:
                with open(caminho_env, "r", encoding="utf-8") as f:
                    return [line.split('=')[0].strip() for line in f if '=' in line and not line.startswith('#')]
            except: pass
    return []

def sugerir_comando_execucao(diretorio_alvo, dependencias):
    deps = dependencias.lower()
    if "pytest" in deps: return "pytest"
    if os.path.exists(os.path.join(diretorio_alvo, "Makefile")): return "make run"
    return "python main.py"

def obter_versao_python():
    return f"{sys.version_info.major}.{sys.version_info.minor}"