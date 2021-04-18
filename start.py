import os
import platform
import subprocess
import sys
import webbrowser



rootPath = os.path.dirname(os.path.abspath(__file__))
print("initial path", rootPath)
currentOS = platform.system()

def my_subprocess(command,c='C:\here'):
     subprocess.call(['C:\\Windows\\System32\\Notepad.exe', 'C:\\openThisfile.txt'])


if currentOS == "Linux":
    print("Linux")
else:
    print("Windows")
    aagayamPath = f"{rootPath}\\aagayam"
    print(aagayamPath)
    if os.path.exists(aagayamPath) and os.path.isdir(aagayamPath):
        os.chdir(aagayamPath)
        os.chdir(f"{aagayamPath}\\env\\Scripts")
        command = f"cd {aagayamPath}/env/Scripts & activate & cd ../../ && uvicorn src.server:app --host 0.0.0.0 --port 8000 --reload"
        subprocess.Popen(f'cmd.exe /K {command}') 
        webbrowser.open('http://localhost:8000', new=2)
        subprocess.Popen(f'cmd.exe /K cd {rootPath}/kaatru && npm run serve') 
        webbrowser.open('http://localhost:8080', new=2)


        