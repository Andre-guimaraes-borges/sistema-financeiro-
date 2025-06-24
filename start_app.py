import subprocess
import webbrowser
import time
import os
import sys

# Caminho para o main.py do Flask
# Ajusta o caminho para ser relativo ao executável do PyInstaller

if getattr(sys, 'frozen', False):
    # Se estiver rodando como executável PyInstaller
    base_path = sys._MEIPASS
    flask_app_path = os.path.join(base_path, 'src', 'main.py')
else:
    # Se estiver rodando como script Python normal
    flask_app_path = os.path.join(os.path.dirname(__file__), 'src', 'main.py')

# Comando para iniciar o servidor Flask
# Usamos pythonw para evitar que a janela do console apareça no Windows
python_executable = 'pythonw' if sys.platform == 'win32' else 'python'
command = [python_executable, flask_app_path]

# Iniciar o servidor Flask em um processo separado
# Usamos subprocess.Popen para não bloquear o script atual
print("Iniciando o servidor Flask...")
flask_process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Dar um tempo para o servidor iniciar
time.sleep(5) # Ajuste este tempo se o servidor demorar mais para iniciar

# Abrir o navegador
print("Abrindo o navegador...")
webbrowser.open("http://localhost:5000" )

print("Aplicação iniciada. O servidor Flask continuará rodando em segundo plano.")
print("Para fechar a aplicação, você precisará encerrar o processo do Python/Flask manualmente (via Gerenciador de Tarefas no Windows ou 'kill' no Linux/macOS).")

# Manter o processo principal vivo para que o Flask continue rodando
# Isso é um hack simples. Em uma aplicação real, você teria um loop de eventos ou um mecanismo de monitoramento.
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Encerrando aplicação...")
    flask_process.terminate()
    flask_process.wait()
    print("Servidor Flask encerrado.")
