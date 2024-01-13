import mysql.connector
from faker import Faker
import random # 파이썬 기본 모듈

# (1) MYSQL 연결 설정
db_connector = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'oz-password',
    database = 'testdatabase'
)

# (2) MYSQL 연결
cursor = db_connection.cursor()
faker = Faker()

# users 데이터 생성 (user 데이터를 만들어야 orders 데이터와 연결시켜서 만들 수 있음)

for _ in range(100): # _ 를 쓰는 이유는 _ 값을 쓴다는게 아니고 단지 100번을 반복해서 쓸거야 라는 말
    username = faker.user_name() # 지금 하고 있는 작업: data를 join하기 위해사 두 개의 테이블에 데이터를 생성해주는 작업
    email = faker.email()

    sql = "INSERT INTO users(username, email) VALUES(%s, %s)"
    values = (username, email)
    cursor.execute(sql)

# user_id 불러오기
cursor.execute("SELECT user_id FROM users")
valid_user_id = [row[0] for row in cursor.fetchall()]

# 100개의 주문 더미 데이터 생성(orders)
for _ in range(100):
    user_id = random.choice(valid_user_id)
    product_name = faker.word()
    quantity = random.randint(1,10)

    try:
        sql = "INSERT INTO users(user_id, product_name, quantity) VALUES(%s, %s)"
        values = (user_id, product_name, quantity)
        cursor.execute(sql, values)
    except:
        pass

db_connection.commit()
cursor.close()
db_connection.close()