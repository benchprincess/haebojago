from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB 연결
client = MongoClient('mongodb://localhost:27017/')
db = client['kreamadmin']
products = db['products']

# 검색 로직을 함수로 분리
def query_data(search_filter=None):
    try:
        query = {}
        if search_filter:
            if search_filter.lower() == 'adidas':
                # 아디다스 검색 시 브랜드로 검색
                query['brand'] = {'$regex': 'adidas', '$options': 'i'}
            else:
                # 다른 검색어일 경우 제품명으로 검색
                query['name'] = {'$regex': f'.*{search_filter}.*', '$options': 'i'}
        return products.find(query)
    except Exception as e:
        return str(e)

# 홈 페이지 라우팅
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        search_filter = sanitize_input(request.form.get('productNameInput'))
        cursor = query_data(search_filter)
        data = list(cursor)
        return render_template('index.html', data=data)
    else:
        cursor = query_data()
        data = list(cursor)
        return render_template('index.html', data=data)

# 검색 결과 페이지 라우팅
@app.route('/search', methods=['POST'])
def search():
    search_query = sanitize_input(request.form.get('search_query'))
    cursor = query_data(search_query)
    search_results = list(cursor)
    return render_template('search.html', search_results=search_results, search_query=search_query)

# API 엔드포인트 구성
@app.route('/get_data_endpoint')
def get_data_endpoint():
    search_filter = sanitize_input(request.args.get('search_keyword'))
    cursor = query_data(search_filter)
    data = list(cursor)
    return jsonify(data)

# 보안 강화: 사용자 입력 검증 또는 이스케이핑 함수 추가
def sanitize_input(input_str):
    # 원하는 검증 및 이스케이핑 로직을 적용
    return input_str

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