@route('/chat')
def hello():
    # /chatというURLにアクセスしたとき、chat.htmlに遷移する
    return template('chat', msglist=msglist, username='')
