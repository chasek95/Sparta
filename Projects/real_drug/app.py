from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb://chaser:chaser@AWS13.125.187.219',27017)
db = client.dbsparta


# HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')

# API 역할을 하는 부분
@app.route('/search', methods=['GET'])
def stars_list():
   want_name = request.args.get('drug_name')
   drug=db.drug.find_one({'name':want_name}),{'_id':False}
   print(drug)
   return jsonify({'result':'success', 'search_result':drug})   
   

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)