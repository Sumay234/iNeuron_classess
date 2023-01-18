from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/via_postman', methods=['POST']) # To render Homepage


def math_operation():
    if (request.method == 'POST'):
        operation=request.json['operation']
        num1=int(request.json['num1'])
        num2=int(request.json['num2'])


    if (operation == 'add'):
        r = num1 + num2
        result = 'the sum of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
    if (operation == 'subtract'):
        r = num1 - num2
        result = 'the difference of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
    if (operation == 'multiply'):
        r = num1 * num2
        result = 'the product of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
    if (operation == 'divide'):
        r = num1 / num2
        result = 'the quotient when ' + str(num1) + ' is divided by ' + str(num2) + ' is ' + str(r)

    return jsonify(result)


@app.route('/sumay',methods=['POST'])
def sumay():
    if (request.method == 'POST'):
        num0=request.json['num0']
        num1=request.json["num1"]
        num2=request.json["give no.2"]

    result=num0*num1*num2
    return jsonify(result)

@app.route('/sumay1',methods=['POST'])
def sam():
    if (request.method == 'POST'):
        name=request.json['name']
        email=request.json['email']
        phone=request.json['phone']

    return jsonify(name + email + str(phone))


if __name__ == '__main__':
    app.run()