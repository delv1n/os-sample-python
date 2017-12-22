from flask import Flask
application = Flask(__name__)

all_data=[]

@application.route("/", methods=['POST'])
def hello():
    data = request.form
    all_data.append(data)
    return all_data

if __name__ == "__main__":
    application.run()
