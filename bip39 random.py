import random
import subprocess
def random_line(afile):
    line = next(afile)
    for num, aline in enumerate(afile):
      if random.randrange(num + 2): continue
      line = aline
    return line
def copy2clip(txt):
    cmd='echo '+txt.strip()+'|clip'
    return subprocess.check_call(cmd, shell=True)

def masterrun():
    line1 = random_line(f), f.seek(0)
    #print(random_line(f), sep=' ', end='', flush=True), f.seek(0)
    return line1


f = open("english.txt", 'r')
print(random_line(f), sep=' ', end='', flush=True), f.seek(0),print(random_line(f), sep=' ', end='', flush=True), f.seek(0),print(random_line(f), sep=' ', end='', flush=True), f.seek(0),print(random_line(f), sep=' ', end='', flush=True), f.seek(0),print(random_line(f), sep=' ', end='', flush=True), f.seek(0),print(random_line(f), sep=' ', end='', flush=True), f.seek(0),print(random_line(f), sep=' ', end='', flush=True), f.seek(0),print(random_line(f), sep=' ', end='', flush=True), f.seek(0),print(random_line(f), sep=' ', end='', flush=True), f.seek(0),print(random_line(f), sep=' ', end='', flush=True), f.seek(0),print(random_line(f), sep=' ', end='', flush=True), f.seek(0),print(random_line(f), sep=' ', end='', flush=True), f.seek(0)
#print(masterrun)
f.close()