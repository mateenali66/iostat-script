import subprocess
proc = subprocess.Popen(["iostat | grep 'xvda'"], stdout=subprocess.PIPE, shell=True)
stdout = proc.communicate()[0]
iops = stdout.split()[2]
print(iops)
