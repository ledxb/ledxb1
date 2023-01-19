# ledxb1 Name :- ledxb1
# Author :- Rajkumar dusad
# Date :- 19/1/2023

import os
import sys
from time import sleep
from modules.logo import *
from modules.system import *

class ledxb1:
  @classmethod
  def install(self):
    while True:
      system=sys()
      os.system("clear")
      logo.ins_tnc()
      inp=input("\033[1;33m Do you want to install ledxb1 [Y/n]> \033[00m")
      if inp=="y" or inp=="Y":
        os.system("clear")
        logo.installing()
        if system.sudo is not None:
          #require root permission
          if os.path.exists(system.conf_dir+"/ledxb1"):
            pass
          else:
            os.system(system.sudo+" mkdir "+system.conf_dir+"/ledxb1")
          os.system(system.sudo+" cp -r modules core ledxb1.py "+system.conf_dir+"/ledxb1")
          os.system(system.sudo+" cp -r core/ledxb1 "+system.bin)
          os.system(system.sudo+" cp -r core/ledxb1 "+system.bin)
          os.system(system.sudo+" chmod +x "+system.bin+"/ledxb1")
          os.system(system.sudo+" chmod +x "+system.bin+"/ledxb1")
          os.system("cd .. && "+system.sudo+" rm -rf ledxb1")
          if os.path.exists(system.bin+"/ledxb1") and os.path.exists(system.conf_dir+"/ledxb1"):
            os.system("clear")
            logo.ins_sc()
            tmp=input("\033[1;36m ##> \033[00m")
            break
          else:
            os.system("clear")
            logo.not_ins()
            tmp=input("\033[1;36m ##> \033[00m")
            break
        else:
          if os.path.exists(system.conf_dir+"/ledxb1"):
            pass
          else:
            os.system("mkdir "+system.conf_dir+"/ledxb1")
          os.system("cp -r modules core ledxb1.py "+system.conf_dir+"/ledxb1")
          os.system("cp -r core/ledxb1 "+system.bin)
          os.system("cp -r core/ledxb1 "+system.bin)
          os.system("chmod +x "+system.bin+"/ledxb1")
          os.system("chmod +x "+system.bin+"/ledzb1")
          os.system("cd .. && rm -rf ledxb1")
          if os.path.exists(system.bin+"/ledxb1") and os.path.exists(system.conf_dir+"/ledxb1"):
            os.system("clear")
            logo.ins_sc()
            tmp=input("\033[1;36m ##> \033[00m")
            break
          else:
            os.system("clear")
            logo.not_ins()
            tmp=input("\033[1;36m ##> \033[00m")
            break
      else:
        break

if __name__=="__main__":
  try:
    tool.install()
  except KeyboardInterrupt:
    os.system("clear")
    logo.exit()
