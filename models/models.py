from sqlalchemy import Column, Integer, String, ForeignKey, CheckConstraint
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# DB Accounts
class User(Base):
    __tablename__ = 'users'
    Id_User = Column(Integer, primary_key=True, autoincrement=True)
    Name = Column(String(100))
    Lastname = Column(String(100))
    User_mail = Column(String(100), unique=True)
    Password = Column(String(100))
    Status = Column(Integer, CheckConstraint('Status IN (0, 1)'))

# DB UserProfile
class Type(Base):
    __tablename__ = 'Types'
    Id_type = Column(Integer, primary_key=True, autoincrement=True)
    Description = Column(String(50))

class Preference(Base):
    __tablename__ = 'Preferences'
    Id_preferences = Column(Integer, primary_key=True, autoincrement=True)
    Description = Column(String(50))

class Profile(Base):
    __tablename__ = 'Profile'
    Id_User = Column(Integer, primary_key=True)
    User_mail = Column(String(100), unique=True)
    Name = Column(String(100))
    Lastname = Column(String(100))
    Description = Column(String(255))
    Id_preferences = Column(Integer, ForeignKey("Preferences.Id_preferences"))
    Id_type = Column(Integer, ForeignKey("Types.Id_type"))
    Status_account = Column(Integer, CheckConstraint("Status_account IN (0, 1)"))
