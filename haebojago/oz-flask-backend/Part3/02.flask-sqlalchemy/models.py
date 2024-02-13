# Model -> Table 생성
# 게시글 - board
# 유저 - user

from db import db

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), unique = True, nullable = False)
    email = db.Column(db.String(100), unique = True, nullable = False)
    # lazy = 'dynamic' : 유저가 쓴 게시글을 다 보여주는게 아니라 특정 게시글을 보여줄 수 있는 코드
    # back_populates = 'author' : Board 모델의 author 필드와 이 관계를 양방향으로 연결 #
    boards = db.relationship('Board', back_populates='author', lazy = 'dynamic')

class Board(db.Model):
    __tablename__ = "boards"

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    content = db.Column(db.String(300))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable = False)
    # back_populates = 'boards' : User 모델의 boards 필드와 이 관계를 양방향으로 연결
    author = db.relationship('User', back_populates = 'boards')
