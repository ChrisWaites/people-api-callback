from flask import Flask, request
app = Flask(__name__)

@app.route("/", methods=['POST'])
def handler():
    print(request.get_json())
    print(request.form)
    return 'Success!'

if __name__ == "__main__":
    app.run()
