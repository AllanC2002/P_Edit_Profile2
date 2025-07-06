from models.models import User, Profile
from conections.mysql import conection_accounts, conection_userprofile
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode("utf-8")).hexdigest()

def edit_user(Id_User, Name=None, Lastname=None, Password=None):
    session_accounts = conection_accounts()
    session_userprofile = conection_userprofile()

    user = session_accounts.query(User).filter_by(Id_User=Id_User, Status=1).first()
    profile = session_userprofile.query(Profile).filter_by(Id_User=Id_User, Status_account=1).first()

    if not user or not profile:
        session_accounts.close()
        session_userprofile.close()
        return {"error": "Active user/profile not found"}, 404

    if Name is not None:
        user.Name = Name
        profile.Name = Name
    if Lastname is not None:
        user.Lastname = Lastname
        profile.Lastname = Lastname
    if Password is not None:
        user.Password = hash_password(Password)

    session_accounts.commit()
    session_userprofile.commit()
    session_accounts.close()
    session_userprofile.close()

    return {"message": "User data updated successfull"}, 200
