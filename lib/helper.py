import bottle

def url(url):
    return bottle.request.get('SCRIPT_NAME')# + url
