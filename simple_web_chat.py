from bottle import route, post, request, run, template, view
import sqlite3
import dataclasses

@dataclasses.dataclass
class Message:
    username: str
    message: str

msglist = [Message(username="bob", message="hello. my name is bob.")]

@route('/chat')
def hello():
    return template('chat', msglist=msglist, username='')


@route('/chat/<username>')
def reload(username):
    return template('chat', msglist=msglist, username=username)


@post('/chat')
def send_message():
    username = request.forms.username
    message = request.forms.message
    msglist.append(Message(username, message))

    return template('chat', msglist=msglist, username=username)


run(host='localhost', port=29090, reloader=True, debug=True)