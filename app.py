from bottle import *

application = default_app()
app = application

BaseTemplate.defaults['get_url'] = app.get_url

@route('/static/:filename#.*#', name='static')
def server_static(filename):
    return static_file(filename, root='static')

@route('/')
@view('home')
def index(title=''):
    return { 'title': 'Raspberry Pi Monitor' }


@route('/specs')
@view('specs')
def get_specs(title=''):
    return {'title': 'Specifications Raspberry Pi'}



debug(True)
