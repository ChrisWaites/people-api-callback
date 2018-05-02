from flask import Flask, request
app = Flask(__name__)

@app.route("/", methods=['POST'])
def handler():
    print(request.args)
    print(request.data)
    print(request.text)
    return 'Success!'

if __name__ == "__main__":
    app.run()
