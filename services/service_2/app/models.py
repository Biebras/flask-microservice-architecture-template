from app import db

class Service2Model(db.Model):
    __tablename__ = 'table_name'
    id = db.Column(db.Integer, primary_key=True)