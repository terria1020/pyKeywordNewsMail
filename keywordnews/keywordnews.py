
from mailhandler.textbuilder import set_text
from mailhandler.sender import sender

def main():
    _from = "any991020@naver.com"
    _to = "jaehan1346@gmail.com"
    content = '''
        이메일 전송 테스트하는 이메일입니다.
        이것은 내용입니다.
        lorem ipsum을 이용해서 내용을 채워야겠습니다.
        Ipsum culpa et anim est non ut eu excepteur duis esse elit aliqua nulla ad. Ullamco sunt pariatur reprehenderit enim in adipisicing voluptate incididunt. Aliquip commodo qui cillum nostrud excepteur magna magna Lorem irure nostrud nulla minim qui. Aliqua reprehenderit consectetur Lorem culpa minim eu consectetur.

Cillum et consequat voluptate mollit reprehenderit est Lorem anim voluptate dolore. Id excepteur qui ex culpa sunt consequat laboris dolore in. Nostrud voluptate incididunt voluptate laboris proident aute magna enim do dolor tempor nostrud incididunt.

Est sint anim laboris veniam in labore labore cupidatat cupidatat enim duis officia. Elit voluptate sunt commodo do mollit aliqua qui sint officia magna adipisicing non sint Lorem. Amet id aliqua ex cupidatat mollit aute velit. Ex laborum magna laboris sunt laborum cillum culpa dolore amet eu. Nisi commodo eu et dolor occaecat et sint labore non reprehenderit exercitation. Ut Lorem nisi exercitation cupidatat ad enim. Ut ullamco sint ad laborum ipsum fugiat consequat laborum aute esse ea deserunt eiusmod.

Esse elit pariatur laborum exercitation aliquip do non ipsum duis cupidatat. Proident nulla sit in velit labore dolore commodo. Culpa ullamco enim Lorem laboris laborum anim et sunt cillum et mollit tempor occaecat. Amet velit officia consequat Lorem enim dolor qui ex laborum sunt commodo.
    '''
    message = set_text(_from, _to, contents=content)
    sender.send(message, _from, _to)
    
if __name__ == '__main__':
    main()