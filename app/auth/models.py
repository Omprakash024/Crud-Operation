from datetime import datetime
from app import db,bcrypt
from app import login_manger
from flask_login import UserMixin

class UserCredential(UserMixin, db.Model):
    __tablename__ = 'usercred'

    id = db.Column(db.Integer,primary_key=True)
    user_name = db.Column(db.String(30))
    user_email = db.Column(db.String(60),unique=True)
    user_pass = db.Column(db.String(100))
    registration_date = db.Column(db.DateTime,default=datetime.utcnow())

    def check_password(self,password):
        return bcrypt.check_password_hash(self.user_pass, password)


    @classmethod
    def create_user(cls, name, email, password):
        users = cls(
            user_name = name,
            user_email =email,
            user_pass = bcrypt.generate_password_hash(password).decode('utf-8')
        )

        db.session.add(users)
        db.session.commit()
        return users


@login_manger.user_loader
def load_user(id):
    return UserCredential.query.get(int(id))