import os
import cloudinary
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

class ProductionConfig(Config):
    DEBUG = False
    TESTING = False

class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/copwatch_test'
    DEBUG = True

cloudinary.config = ({
    'cloud_name': os.environ['CLOUDINARY_NAME'],
    'api_key': os.environ['CLOUDINARY_API_KEY'],
    'api_secret': os.environ['CLOUDINARY_API_SECRET']
    })

# app_config = {
#     'development': DevelopmentConfig,
#     'production': ProductionConfig
# }
