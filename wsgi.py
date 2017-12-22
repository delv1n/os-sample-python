from flask import Flask, request
application = Flask(__name__)

all_data=[]

@application.route("/", methods=['GET', 'POST'])
def hello():
    if request.method == 'GET':
        return all_data
    else:
      data = request.json
      all_data.append(data)
      return all_data

if __name__ == "__main__":
    application.run()
