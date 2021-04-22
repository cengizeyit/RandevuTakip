import os

basedir=os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_DATABASE_URI='mssql+pyodbc://sa:rana2004@CENGIZEYITPC1/RandevuTakipDB'
    SQLALCHEMY_TRACK_NOTIFICATION=False
