from os import system,name
from os.path import exists,isfile
from termcolor import colored,cprint
from pyfiglet import Figlet
from Helper import convertTreeToListOfFilesAndFolders

fileName = 'struct.txt'

f = Figlet(width=120)

print_red = lambda x:cprint(x,'red')    

print_green = lambda x:cprint(x,'green')

print_blue = lambda x:cprint(x,'blue')

file = open(fileName,'r')


if __name__=='__main__':
    system('cls' if name=='nt' else 'clear')
    print_red(f.renderText("Tree To Zip"))
    if(not exists(fileName) or not isfile(fileName)):
        print_red("struct.txt File Not Exist.")
        exit()
    print_green('File found.')
    print_green('Reading Structure File...')
    lines = file.readlines()
    if(len(lines)<=0):
        print_red("Structure File Is Empty.")
        exit()
    print_blue("Converting...")
    convertTreeToListOfFilesAndFolders(lines)
    print_green("Converted Successfully.")
