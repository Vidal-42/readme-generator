import subprocess

def capturar_estrutura():
    """Roda o comando tree no WSL e retorna o texto formatado."""
    try:
        # -I '.venv|__pycache__' ignora pastas irrelevantes
        resultado = subprocess.run(
            ['tree', '-I', '.venv|__pycache__'], 
            capture_output=True, 
            text=True, 
            encoding='utf-8'
        )
        return f"```bash\n{resultado.stdout}\n```"
    except FileNotFoundError:
        return "```bash\n# Comando 'tree' não encontrado no WSL.\n. \n├── main.py\n└── ...\n```"