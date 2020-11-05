from . import auth

@auth.route('/',methods=['POST'])
def auth():
    return ''