from bottle import static_file


@route('/static:path#.+#', name='static')
def static(path):
    return static_file(path, root='static'
