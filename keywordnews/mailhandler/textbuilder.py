from email.mime.text import MIMEText
from keywordnews.mailhandler.sender import sender

def set_text(_to: str, contents: str, keyword) -> MIMEText :
    message = MIMEText(contents)
    message['From'] = sender.get_host_mail()
    message['To'] = _to
    message['Subject'] = f"[BOT] 키워드 [{keyword}]에 대한 새 기사가 있습니다."
    return message