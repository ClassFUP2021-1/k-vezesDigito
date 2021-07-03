import os
import copy
import subprocess
import casosDeTeste.py

def command(command):
    env = copy.deepcopy(os.environ)
    proc = subprocess.Popen(command,
                shell=True, env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    result = proc.stdout.read()
    return result

erros = 0

for key, value in casosDeTeste.py.casosDeTeste.items():
  entradas = key.split('-')
  ret = command("python teste.py {0} {1}".format(entradas[0], entradas[1]))
  # print(ret.decode("utf-8").replace('\n', '') == value)
  if ret.decode("utf-8").replace('\n', '') != value:
    erros += 1
    print("Erro no caso: ", key, value)

if erros == 0:
  print("Passou nos testes!")

