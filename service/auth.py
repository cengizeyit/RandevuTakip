from flask import session

class AuthService:
    def is_logged():
        if 'logged' in session:
            return True
        else:
            return False


auth_service=AuthService()