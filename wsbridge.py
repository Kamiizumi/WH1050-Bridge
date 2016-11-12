import subprocess
import shlex

cmdtorun = shlex.split("rtl_433 -R 68 -F json -U -q")
process = subprocess.Popen(cmdtorun, stdout=subprocess.PIPE)
while True:
    output = process.stdout.readline()
    