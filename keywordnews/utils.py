
from sys import argv
import yaml

help = '''
<option>: select the menu. is integer.
  1: run yamlbuilder for host_info.yaml
'''

def main():
    if len(argv) != 2:
        print("usage: utils.py <option>")
        exit(1)
    else:
        if argv[1] == "-h" or argv[1] == "help":
            print(help)
        if int(argv[1]) == 1:
            yamlbuilder()
        elif int(argv[1]) == 2:
            print("option 2!")
        else:
            print("unexpected option! if u see the help, utils.py -h or utils.py help")
            exit(1)

def yamlbuilder():
    pass

if __name__ == '__main__':
    main()