from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 장바구니를 저장할 전역 변수
cart_items = []

# 홈 페이지 라우팅
@app.route('/')
def index():
    return render_template('index.html', cart_items=cart_items)

# 상품 목록 페이지 라우팅
@app.route('/products')
def products():
    # 여기에서 상품 목록을 가져오는 로직을 추가할 수 있습니다.
    product_list = [
        {'id': 1, 'name': '상품 1', 'price': 10},
        {'id': 2, 'name': '상품 2', 'price': 20},
        {'id': 3, 'name': '상품 3', 'price': 30},
    ]
    return render_template('products.html', products=product_list)

# 장바구니에 상품 추가
@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    # 여기에서 상품 정보를 가져오는 로직을 추가할 수 있습니다.
    product = {'id': product_id, 'name': f'상품 {product_id}', 'price': product_id * 10}
    
    # 장바구니에 상품 추가
    cart_items.append(product)
    
    # 상품 목록 페이지로 리다이렉트
    return redirect(url_for('products'))

if __name__ == '__main__':
    app.run(debug=True)