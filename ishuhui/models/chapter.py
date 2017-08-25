from ishuhui.extensions.flasksqlalchemy import db


class Chapter(db.Model):
    __tablename__ = 'chapters'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    title = db.Column(db.String(256), nullable=False)
    comic_id = db.Column(db.Integer, nullable=False)
    chapter_number = db.Column(db.Integer, nullable=False)
    author = db.Column(db.String(256), nullable=True)
    front_cover = db.Column(db.String(256), nullable=True)
    refresh_time = db.Column(db.String(256), nullable=True)
    images = db.Column(db.Text, nullable=True)
