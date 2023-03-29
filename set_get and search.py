# you can see the redis like a dictionary,in fact it's a dictionary
#for example you can make a dictionary of capitals
from flask import Flask
from redis import Redis
app = Flask(__name__)
capitals = Redis(host='localhost',port=6379)

@app.route('/')
def home():
    #you can set key-values
    capitals.set('iran', 'tehran')
    capitals.set('USA', 'washangton')
    capitals.set('india', 'dehli')
    #or you can set group
    capitals.mset({"japan": "tokiyo", "china": "pecan"})
    return "saved"
@app.route('/get_capitals')
def get_capitals():
    #using below command you can access all database and you can search in it
    for key in capitals.keys():
        print(key,' : ',capitals.get(key))
        if 'tehran'==str(capitals.get(key),'utf-8'):
            print('tehran is capital of ',str(key,'utf-8'))
    return capitals.get('USA')
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)