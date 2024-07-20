from flask import Flask, request, render_template_string
import random
import string

app = Flask(__name__)

def generate_password(length=12, complexity='medium'):
    if complexity == 'low':
        charset = string.ascii_letters + string.digits
    elif complexity == 'medium':
        charset = string.ascii_letters + string.digits + string.punctuation
    elif complexity == 'high':
        charset = string.ascii_letters + string.digits + string.punctuation + '£€¥§©®'
    else:
        raise ValueError("Invalid complexity level. Please choose from 'low', 'medium', or 'high'.")
        
    password = ''.join(random.choice(charset) for _ in range(length))
    return password

@app.route('/', methods=['GET', 'POST'])
def index():
    password = ''
    length = 12
    complexity = 'medium'
    if request.method == 'POST':
        length = int(request.form.get('length', 12))
        complexity = request.form.get('complexity', 'medium')
        password = generate_password(length, complexity)
    
    return render_template_string('''
        <!doctype html>
        <html lang="en">
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <title>Password Generator</title>
            <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background: url('{{ url_for('static', filename='background.png') }}') no-repeat center center fixed;
                    background-size: cover;
                    margin: 0;
                    padding: 0;
                }
                .container {
                    max-width: 600px;
                    margin: 250px auto;
                    text-align: center;
                    background-color: rgba(255, 255, 255, 0.8);
                    padding: 40px;
                    border-radius: 10px;
                    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
                }
                .form-group {
                    margin-bottom: 20px;
                }
                label {
                    display: block;
                    margin-bottom: 5px;
                    font-weight: bold;
                }
                input[type="text"], select {
                    width: calc(100% - 22px);
                    padding: 10px;
                    margin: 10px 0;
                    border: 1px solid #ccc;
                    border-radius: 4px;
                }
                input[type="submit"] {
                    background-color: rgba(0, 123, 255, 0.8);
                    color: white;
                    border: none;
                    padding: 10px 20px;
                    border-radius: 4px;
                    cursor: pointer;
                    font-size: 16px;
                }
                input[type="submit"]:hover {
                    background-color: rgba(0, 123, 255, 1);
                }
                h2 {
                    margin-top: 20px;
                    color: #333;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Password Generator</h1>
                <form method="post">
                    <div class="form-group">
                        <label for="length">Length:</label>
                        <input type="text" id="length" name="length" value="{{ length }}">
                    </div>
                    <div class="form-group">
                        <label for="complexity">Complexity:</label>
                        <select id="complexity" name="complexity">
                            <option value="low" {% if complexity == 'low' %}selected{% endif %}>Low</option>
                            <option value="medium" {% if complexity == 'medium' %}selected{% endif %}>Medium</option>
                            <option value="high" {% if complexity == 'high' %}selected{% endif %}>High</option>
                        </select>
                    </div>
                    <input type="submit" value="Generate Password">
                </form>
                {% if password %}
                    <h2>Generated Password: <span id="passwordDisplay">{{ password }}</span></h2>
                {% endif %}
            </div>
        </body>
        </html>
    ''', password=password, length=length, complexity=complexity)

if __name__ == '__main__':
    app.run(debug=True)
