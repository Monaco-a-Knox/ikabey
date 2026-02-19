from subprocess import run
#from distutils.dir_util import copy_tree
import os, shutil, shlex
from sys import exit

# Nome da pasta onde os arquivos do patch serão enviados
patch_folder = "\"[KT] Kaziklu Bey ~Entrevista com o Vampiro~\""

def stringtool():
    try:
        run([r'dependencies/StringTool.exe', "exec.txt"])
    except:
        print("exec.dat not found?")

    shutil.move("dependencies/exec_New.dat", "patch/data/system/exec.dat")

def compile():
    # Define onde o arquivo tex para descompressão está, extrai e move para a pasta patch
    #tex_location = "outros/tex.7z"
    #run([r'dependencies/7za.exe', 'x'] + shlex.split(tex_location))
    #shutil.move('tex', 'patch/data/picture/event/tex')
    
    # Define onde está o arquivo data_pack.py e pasta patch, roda o script e move para a pasta de release
    packer_args = "dependencies/dat_pack.py patch"
    run([r'python'] + shlex.split(packer_args))
    shutil.move("data2.dat", "[KT] Kaziklu Bey ~Entrevista com o Vampiro~")
    
    # nome do arquivo de destino
    # IMPORTANTE: o nome do arquivo, caso modificado, precisa também ser modificado nos scripts do Github Actions, sob a pasta .github/workflows neste repositório
    zip_args = f"KT.Kaziklu.Bey.~Entrevista.com.o.Vampiro~.7z {patch_folder}"
    run([r'dependencies/7za.exe', 'a'] + shlex.split(zip_args))

stringtool()
compile()