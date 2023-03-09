import os

basedir = os.path.abspath(os.path.dirname(__name__))

class config():
    FLASK_APP = os.environ.get('FLASK_APP')
    FLASK_ENV = os.environ.get('FLASK_ENV')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class headers():
    API_Key = "d62c7e9f0bmsh703884992d27023p1153acjsn554022fd80fe"
    API_Host = "workout-planner1.p.rapidapi.com"
