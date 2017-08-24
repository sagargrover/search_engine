#!flask/bin/python
from flask import Flask, request
from query import Query
import json

app = Flask(__name__)
q = Query()

@app.route('/search', methods=['POST'])
def index():
    query = json.loads(request.data)
    results = q.execute_query(query["tokens"], int(query["K"]))
    results = json.dumps(results)
    return  results

if __name__ == '__main__':
    app.run(debug=True)