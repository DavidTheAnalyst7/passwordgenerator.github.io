from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

def password_generator(min_length, numbers=True, special_character=True):
    letters = string.ascii_letters
    digits = string.digits
    specials = string.punctuation
    words = letters
    
    if numbers:
        words += digits
    if special_character:
        words += specials
        
    pwd = ''
    
    while len(pwd) < min_length:
        new_pass = random.choice(words)
        pwd += new_pass
        
        if numbers:
            new_pass += digits
        elif special_character:
            new_pass += specials
        
    return pwd

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_password():
    min_length = int(request.form['passwordLength'])
    numbers = 'numbers' in request.form
    special_character = 'special_character' in request.form

    generated_password = password_generator(min_length, numbers, special_character)

    return render_template('generate.html', generated_password=generated_password)

if __name__ == '__main__':
    app.run(debug=True)
