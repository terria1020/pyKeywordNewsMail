import sys
import yaml
from smtplib import SMTP, SMTP_SSL, SMTPAuthenticationError, SMTPConnectError
from email.mime.text import MIMEText
from datetime import datetime

yaml_sample = '''
info:
    host: smtp.sample.com # <SMTP_SERVER_ADDR_HERE>
    port: 587 # <SMTP_SERVER_PORT_HERE>
    login:
        id: sampleid # <HOST_ID_EDIT_HERE>
        pw: samplepw # <HOST_PASSWORD_EDIT_HERE>
'''

class sender:
    @staticmethod
    def send(text: MIMEText, _from: str, _to: str) -> None :
        try:
            with open('./host_info.yaml', 'r') as f:
                if f is None:
                    exit(1)
                conf = (dict(yaml.safe_load(f)))['info']
        except FileNotFoundError:
            print("[!] 호스트 정보를 담은 yaml 파일이 존재하지 않습니다.")
            print(yaml_sample)
            print("이 구조로 된 'host_info.yaml을 생성하여 프로젝트의 최상단에 위치할 수 있도록 해 주세요.")
            print("host와 port에는 smtp 서버 주소를 기입해주시고, id와 pw는 smtp호스트의 로그인 정보를 기입허여 주세요.")
            exit(1)

        try:
            smtp = SMTP(conf['host'], conf['port'])
            smtp.starttls()
            smtp.login(conf['login']['id'], conf['login']['pw'])

            smtp.sendmail(_from, _to, text.as_string())
        except SMTPConnectError as e:
            print("[!] 전송서버의 연결상태가 올비르지 않습니다.")
        except SMTPAuthenticationError as e:
            print("[!] 호스트 로그인 정보가 일치하지 않습니다.")
            print(e)
        else:
            timestamp = datetime.now().strftime('%Y-%M-%D %H:%M:%S')
            print(f"# {timestamp} 이메일이 전송되었습니다. [TO: {_to}]")
        finally:
            smtp.quit()