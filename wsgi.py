from flask import Flask, request
import json
application = Flask(__name__)

all_data=[]

@application.route("/", methods=['GET', 'POST'])
def hello():
    if request.method == 'GET':
      return str(json.dumps(all_data))
    else:
      data = request.data
      all_data.append(data)
      return str(json.dumps(all_data))

if __name__ == "__main__":
    application.run()
