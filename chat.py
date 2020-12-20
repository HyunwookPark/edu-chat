from bottle import route, post, request, run, template, view


@route('/')
def index():
    # ルートのURLにアクセスしたとき、index.htmlに遷移する
    return template('index')


run(host='localhost', port=29090, reloader=True, debug=True)