@route('/chat/<username>')
def reload(username):
    # /chat/ユーザ名というURLにアクセスしたとき、chat.htmlに遷移する
    return template('chat', msglist=msglist, username=username)
