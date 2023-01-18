from flask import Flask , render_template , request , jsonify
app=Flask(__name__)

@app.route('/sudd_function')
def url_test():

    test1=request.args.get('val1')
    test2=request.args.get('val2')
    test3= int(test1) + int(test2)


    return ''' <h1>my result is : {}</h1> '''.format(test3)



if __name__ == '__main__':
    app.run()