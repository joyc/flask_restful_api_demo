class Config:
    #SQLALCHEMY_DATABASE_URI = "sqlite:///demo.db"
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@10.211.55.4:3306/api_demo'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET = "flask124"
