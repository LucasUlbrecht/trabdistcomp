from lib.models.profile import Profile

class ProfileService:
    def __init__(self, db):
        self.db = db

    def get_user_by_username(self, username):
        return self.db.session.query(Profile).filter_by(username=username).first()

    # Protect the Flask-Admin using username/password strings and SQLAlchemy
    def validate_authentication(self, username, password):  # Add self here
        user = self.db.session.query(Profile).filter(Profile.username == username).first()  # Make sure to use the db session

        if user:
            # Assuming password is stored hashed, you'd want to check hashes here
            if user.password == password:  # Consider using check_password_hash here for hashed passwords
                return True
        return False
