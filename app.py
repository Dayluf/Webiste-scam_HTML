from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('webiste.html')



@app.route('/signup', methods=['POST'])
def signup():
    # Retrieve form data
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')

# Basic validation (you can add more complex validation)
    if not username or not email or not password:
        return "All fields are required. Please go back and fill out the form."

# If validation passes, you might store the data in a database
    # For simplicity, let's just print the data for now
    print(f"Username: {username}, Email: {email}, Password: {password}")

    return "Signup successful!"

if __name__ == '__main__':
    app.run(debug='True', port=100, host='0.0.0.0')
