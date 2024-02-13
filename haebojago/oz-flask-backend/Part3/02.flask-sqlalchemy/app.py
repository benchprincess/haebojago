from flask import Flask
from flask_smorest import Api 
from db import db
from models import User, Board

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:900326@localhost/02.flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# 메모리영역에서 객체가 바뀔 때 마다 트래킹할거냐
# ㄴ-> 메모리에 굉장한 부하를 주는 거기 때문에 웬만하면 False 로 한다고 함

db.init_app(app)
# 앱 객체를 전달


# blueprint 설정
app.config["API_TITLE"] = "My API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.1.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"


from routes.board import board_blp
from routes.user import user_blp

api = Api(app)
api.register_blueprint(board_blp)
api.register_blueprint(user_blp)
# 블루프린트 등록 코드 작성

from flask import render_template
@app.route('/manage-boards')
def manage_boards():
    return render_template('boards.html')

@app.route('/manage-users')
def manage_users():
    return render_template('users.html')


# 이미 db가 생성되어 있고, 원하는대로 모델이 반영되어 있으면 그대로, 아니면 pass 하는 코드
if __name__ == "__main__":
    with app.app_context():
        print("here")
        db.create_all()

    app.run(debug=True)
