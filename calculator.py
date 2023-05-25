from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/calculator", methods=['GET', 'POST'])
def addition():
    if request.method == "POST":
        num1 = request.form.get('num1')
        num2 = request.form.get('num2')
        add = int(num1) + int(num2)
        
        return render_template('calculator.html', result = add)

    
        #return render_template('results.html', add = add)  
        '''the above code will display results in the results.html file instead of the calculator.html
        It cannot be used along side with the calculator.html'''

    return render_template('calculator.html')

@app.route("/subtraction", methods=['GET', 'POST'])
def subtraction():
    if request.method == "POST":
        num1 = request.form.get('num1')
        num2 = request.form.get('num2')
        subtraction = int(num1) - int(num2)
       

        return render_template('calculator.html', result = subtraction)
    return render_template('calculator.html')


if __name__ == "__main__":
    app.run(debug=True)
