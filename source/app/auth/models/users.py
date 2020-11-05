from flask_login import UserMixin


class Users(UserMixin):
    def __init__(self, nickname: str, password: str):
        super()
        self.id = nickname
        self.password = password

    @staticmethod
    def getUser(nickname:str):
        return ''
