import subprocess
import os

frontend = os.path.join(os.getcwd(), "typing-champion")
backend = os.path.join(os.getcwd(), "typing-backend")

FrontendCommand = "pnpm run dev"
BackendCommand = "python -m uvicorn main:server --reload"

ProcessFrontend = subprocess.Popen(FrontendCommand, cwd=frontend, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
ProcessBackend = subprocess.Popen(BackendCommand, cwd=backend, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

for process, name in [(ProcessFrontend, "Vue Server"), (ProcessBackend, "FastAPI Server")]:
    for line in process.stdout:
        print(f"[{name}] {line.decode().strip()}")