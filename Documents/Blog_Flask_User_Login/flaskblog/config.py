import os


class Config:
    SECRET_KEY='0a0df3d2d331696e8f8bf7fb5afad9ed4e58cf913dd524b19642a247a6ee4957'
    SQLALCHEMY_DATABASE_URI='sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')