from pymongo import MongoClient

# MongoDB에 접속
client = MongoClient('mongodb://admin:admin@localhost:27017')

# 데이터베이스 생성
db = client['testdb']

# 컬렉션 선택
collection = db['users']

# 사용자 데이터 삽입
user_data = {
    'name': 'John',
    'age': 30,
    'email': 'john@example.com'
}
# insert_result = collection.insert_one(user_data)
# print(f"Inserted user with ID: {insert_result.inserted_id}")

result = collection.find()
for document in result:
    print(document['name'])
# 연결 종료
client.close()
