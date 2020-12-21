from bottle import route, run


@route('/')
def hello():
    return 'Hello World'


run(host='localhost', port=29090, reloader=True, debug=True)
