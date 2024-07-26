from flask import Flask, request, render_template, redirect
from password_generator import generate_password
from datetime import datetime


app = Flask(__name__)

Date = datetime.now().strftime("%d-%B-%Y | %H:%M:%S")

@app.route('/')
def index():
    return render_template('index.html', password = ' ', date = Date)

@app.route('/generate', methods = ['GET', 'POST'])
def generate() :
    if request.method == 'POST' :
        try :
            length = int(request.form['length'])

            spaces = 'spaces' in request.form
            digits = 'numbers' in request.form
            symbols = 'symbols' in request.form
            upperCase = 'upper' in request.form

            password = generate_password(length, spaces, digits, symbols, upperCase)

            return render_template('index.html', password = password, date = Date)
        
        except Exception as e :
            return redirect('/')
    else :
        return redirect('/')
    
if __name__ == '__main__' :
    app.run(debug = True)