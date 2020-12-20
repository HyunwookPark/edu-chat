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
