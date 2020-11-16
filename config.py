import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'this is the best travel Agent in africa'
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.gmail.com')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', '587'))
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() in ['true', 'on', '1']
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    BT_MAIL_SUBJECT_PREFIX = '[Travel Blitz Portal Feedback]'
    BT_MAIL_SENDER = 'Travel Blitz Admin <agrib.excellency@gmail.com>'
    BT_MAIL_RECEIVER = 'Client Receiver <ckiwabs@gmail.com>'
    BT_ADMIN = os.environ.get('BT_ADMIN') or 'ckiwabs@gmail.com'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class ProductionConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'mysql://bdefb74d1922e4:9d35dcb4@us-cdbr-east-02.cleardb.com/heroku_17fc59ae35a5292'


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'mysql://CharleiThorin:210022841@localhost/braintreesesaw'


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
