import sys
import yaml
from smtplib import SMTP, SMTPAuthenticationError, SMTPConnectError
from email.mime.text import MIMEText
from datetime import datetime

class sender:
    @staticmethod
    def send(text: MIMEText, _to: str) -> None :
        try:
            with open('./keywordnews/host_info.yaml', 'r') as f:
                conf = (dict(yaml.safe_load(f)))['info']
        except FileNotFoundError:
            print("[!] 호스트 정보를 담은 yaml 파일이 존재하지 않습니다.utils.py에 있는 경로에서 utils.py를 실행하여 host_info.yaml을 생성하여 주세요.")
            exit(1)

        try:
            smtp = SMTP(conf['host'], conf['port'])
            smtp.starttls()
            smtp.login(conf['login']['id'], conf['login']['pw'])

            smtp.sendmail(sender.get_host_mail(), _to, text.as_string())
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

    @staticmethod
    def get_host_mail() -> str :
        try:
            with open('./keywordnews/host_info.yaml', 'r') as f:
                host_mail = (dict(yaml.safe_load(f)))['info']['mailsource']
                return host_mail
        except FileNotFoundError:
            print("[!] 호스트 정보를 담은 yaml 파일이 존재하지 않습니다. 프로젝트에 위치한 utils.py를 실행하여 host_info.yaml을 생성하여 주세요.")
            exit(1)