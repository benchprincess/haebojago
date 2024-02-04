from flask import Flask, render_template
import pymysql

app = Flask(__name__)

conn = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = '900326',
    db = 'kream',
    charset = 'utf8mb4'
)

cur = conn.cursor()
sql = "SELECT * FROM product"
cur.execute(sql)

kream_data = cur.fetchall()

@app.route('/')
def index():
    return render_template('index.html', data_list=kream_data)


# @app.route('/carts')
# def cart():
#     return render_template('cart.html', cart_list = kream_data)

# @app.route('/carts/<pay>')
# def cart(pay):
#     return render_template('pay.html',pay_info = cart)


if __name__ == '__main__':
    app.run(debug=True)