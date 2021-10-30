
from sys import argv
import getpass
import yaml

help = '''
<option>: select the menu. is integer.
  1: run yamlbuilder for host_info.yaml
'''

def main():
    yamlbuilder()
    # if len(argv) != 2:
    #     print("usage: utils.py <option>")
    #     exit(1)
    # else:
    #     if argv[1] == "-h" or argv[1] == "help":
    #         print(help)
    #     if int(argv[1]) == 1:
    #         yamlbuilder()
    #     elif int(argv[1]) == 2:
    #         print("option 2!")
    #     else:
    #         print("unexpected option! if u see the help, utils.py -h or utils.py help")
    #         exit(1)

def yamlbuilder():
    host = input("smtp 서버의 정보를 입력해주세요(예시: smtp.sample.com): ")
    port = int(input("smtp 서버의 포트를 입력해주세요(예시: 587): "))
    mailsource = input("smtp 사용을 허용한 호스트의 이메일 주소를 입력해주세요(예시: sample@sample.com): ")
    id = input("호스트의 smtp 서버 로그인 아이디를 입력해주세요: ")
    pw = getpass.getpass("호스트의 smtp 서버 로그인 비밀번호를 입력해주세요: ")

    yaml_data = {
        'info': {
            'host': host,
            'port': port,
            'mailsource': mailsource,
            'login': {
                'id': id,
                'pw': pw
            }
        }
    }
    with open("host_info.yaml", 'w') as f:
        yaml.dump(yaml_data, f, sort_keys=False)
    print(yaml_data)

if __name__ == '__main__':
    main()