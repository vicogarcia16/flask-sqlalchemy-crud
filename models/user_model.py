from models.user import User


class ModelUser():

    @classmethod
    def login(self, db, user):
        try:
            usuario = db.session.query(User.id, User.username, User.password, User.fullname).filter(User.username==user.username).first()
            # cursor = db.connection.cursor()
            # sql = """SELECT id, username, password, fullname FROM user 
            #         WHERE username = '{}'""".format(user.username)
            # cursor.execute(sql)
            # row = cursor.fetchone()
            print(usuario)
            if usuario != None:
                user = User(usuario[0], usuario[1], User.check_password(usuario[2], user.password), usuario[3])
                return user
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_by_id(self, db, id):
        try:
            usuario = db.session.query(User.id, User.username, User.fullname).filter(User.id==id).first()
            # cursor = db.connection.cursor()
            # sql = "SELECT id, username, fullname FROM user WHERE id = {}".format(id)
            # cursor.execute(sql)
            # row = cursor.fetchone()
            print(usuario)
            if usuario != None:
                return User(usuario[0], usuario[1], None, usuario[2])
            else:
                return None
        except Exception as ex:
            raise Exception(ex)