from memcache import db
from memcache import webapp

class CacheConfig(db.Model):
    # table name
    __tablename__ = 'cache_config'
    # columns
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    capacity = db.Column(db.Integer)
    policy = db.Column(db.Integer)

class CacheStat(db.Model):
    __tablename__ = 'cache_stat'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    num_item = db.Column(db.Integer)
    total_size = db.Column(db.Integer)
    num_req = db.Column(db.Integer)
    num_hit = db.Column(db.Integer)
    time = db.Column(db.Time)

def creat_tables():
    with webapp.app_context():
        db.create_all()

def get_config():
    with webapp.app_context():
        query = db.select(CacheConfig).limit(1)
        config = db.session.scalar(query)

    return config
