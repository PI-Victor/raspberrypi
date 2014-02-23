from bottle import route, template, debug


@route('/login')
def main():
    return template ('login')
    
@route('/')
def index():
    return template ('main')



debug(True)
