import shutil
import psutil
du = shutil.disk_usage('/')
cpu = psutil.cpu_percent(0.5)
print(du)
print(cpu)


