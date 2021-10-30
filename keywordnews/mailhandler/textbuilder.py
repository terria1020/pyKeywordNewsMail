from email.mime.text import MIMEText

keyword = "애플페이"

def set_text(_from: str, _to: str, contents: str) -> MIMEText :
    message = MIMEText(contents)
    message['From'] = _from
    message['To'] = _to
    message['Subject'] = f"[BOT] 키워드 [{keyword}]에 대한 새 기사가 있습니다."
    return message