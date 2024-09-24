from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello, World"


@app.route("/getcode", methods=["GET"])
def getcode():
    return "0.0 ---- yeyyyyyy ---- >.< ---- wooooooo ---- 0.o ---- wowwwwww ---- T.T"


@app.route("/plus/<num1>/<num2>", methods=["GET"])
def calculate(num1, num2):
    try:
        num1 = eval(num1)
        num2 = int(num2)

        results = f"{num1} + {num2} = {num1 + num2}"
    except:
        results = {"error_msg": "inputs must be numbers ka"}

    return results


if __name__ == "__main__":
    app.run()
