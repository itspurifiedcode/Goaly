import os
import platform
import subprocess
import sys
import webbrowser

rootPath = os.path.dirname(os.path.abspath(__file__))
currentOS = platform.system()

if currentOS == "Linux":
    print("Linux")
else:
    print("Windows")
    aagayamPath = f"{rootPath}\\aagayam"
    print(aagayamPath)
    if os.path.exists(aagayamPath) and os.path.isdir(aagayamPath):
        command = f"cd {aagayamPath}/env/Scripts & activate & cd ../../ && uvicorn src.server:app --host 0.0.0.0 --port 8000 --reload"
        subprocess.Popen(f'cmd.exe /K {command}', creationflags=subprocess.CREATE_NEW_CONSOLE) 
        webbrowser.open('http://localhost:8000', new=2)
        subprocess.Popen(f'cmd.exe /K cd {rootPath}/kaatru && npm run serve', creationflags=subprocess.CREATE_NEW_CONSOLE) 
        webbrowser.open('http://localhost:8080', new=2)


        