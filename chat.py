from bottle import route, post, request, run, template, view
import dataclasses


@dataclasses.dataclass
class Message:
    # メッセージ情報

    # ユーザ名
    username: str
    # メッセージ
    message: str


# メッセージリスト(1件目の情報あり)
msglist = [Message(username="bob", message="hello. my name is bob.")]


@route('/')
def index():
    # ルートのURLにアクセスしたとき、index.htmlに遷移する
    return template('index')


@route('/chat')
def hello():
    # /chatというURLにアクセスしたとき、chat.htmlに遷移する
    return template('chat', msglist=msglist, username='')


@route('/chat/<username>')
def reload(username):
    # /chat/ユーザ名というURLにアクセスしたとき、chat.htmlに遷移する
    return template('chat', msglist=msglist, username=username)


@post('/chat')
def send_message():
    # /chatというURLに情報を送ったとき

    # 情報名 username を受け取る
    username = request.forms.username
    # 情報名 message を受け取る
    message = request.forms.message
    # メッセージリストに追加する
    msglist.append(Message(username, message))

    return template('chat', msglist=msglist, username=username)


run(host='localhost', port=29090, reloader=True, debug=True)