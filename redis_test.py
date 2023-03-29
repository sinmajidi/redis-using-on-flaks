#it's a simple test of redis
#you should pull and un redis on linux or docker and get a port
from flask import Flask
from redis import Redis
app = Flask(__name__)
#it means redis runs on localhost:6379
redis = Redis(host='localhost',port=6379)

@app.route('/')
def home():
    redis.set('name', 'sina')
    redis.incr('hits')
    counter = str(redis.get('hits'),'utf-8')
    return "Welcome to this webpage!, This webpage has been viewed "+counter+" time(s)"
@app.route('/get_name')
def get_name():
    redis.get('name')
    return "Welcome to this webpage "+str(redis.get('name'),'utf-8')+", This webpage has been viewed "+str(redis.get('hits'),'utf-8')+" time(s)"
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

# make a key-value in redis
redis.set('KEY', 'VALUE')
# get a value of a key
redis.get('KEY')