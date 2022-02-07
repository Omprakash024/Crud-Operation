from app import create_app,db
from app.auth.models import UserCredential

if __name__ == "__main__":
    flask_app = create_app('prod')
    """
        This code will tell the app which context to be used
        to create the database
    """
    with flask_app.app_context():
        db.create_all()

        if not UserCredential.query.filter_by(user_name="harry").first():
            UserCredential.create_user(
                user="harry",
                email ="harry@gmail.com",
                password="harry123"

            )


    flask_app.run()
