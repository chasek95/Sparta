from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb://test:test@localhost',27017)
db = client.dbsparta


# HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')

# API 역할을 하는 부분
@app.route('/search', methods=['GET'])
def stars_list():
    # 1. mystar 목록 전체를 검색합니다. ID는 제외하고 like 가 많은 순으로 정렬합니다.
    # 참고) find({},{'_id':False}), sort()를 활용하면 굿!
    # 2. 성공하면 success 메시지와 함께 stars_list 목록을 클라이언트에 전달합니다.
   want_name = request.args.get('drug_name')
   drug=db.drugs.find_one({'name':want_name}),{'_id':False}
   print(drug)
   return jsonify({'result':'success', 'search_result':drug})   
   

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)