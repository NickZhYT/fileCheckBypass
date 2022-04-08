import psutil, os
while True:
    for proc in psutil.process_iter():
        try:
            processName = proc.name()
            if processName == "java.exe" and len(proc.children())>1:
                print(processName, proc.children())
                os.system(r"copy C:\Users\Admin\Downloads\baritone-api-forge-1.2.5.jar C:\Users\Admin\AppData\Roaming\McSkill\updates\Magic112\mods")
                print("injected!")
                exit()
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass