from flask import Flask, render_template
import secrets

app = Flask(__name__)

@app.route('/')
def home():
    # Generate a secure random token
    secure_token = secrets.token_hex(16)  # Generates a 32-character hexadecimal token
    return render_template('index.html', token=secure_token)

if __name__ == '__main__':
    app.run(debug=True)
