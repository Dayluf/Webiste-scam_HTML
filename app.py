from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == 'POST':
    # Retrieve form data
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

    # Basic validation (you can add more complex validation)
        if not username or not email or not password:
            return "All fields are required. Please go back and fill out the form."

    # If validation passes, you might store the data in a database
        # For simplicity, let's just print the data for now
        print(f"Username: {username}, Email: {email}, Password: {password}")

        # Render a page displaying the entered information
        return render_template('signup_info.html', username=username, email=email, password=password)

    return render_template('signup_form.html')

if __name__ == '__main__':
    app.run(debug='True', port=100, host='0.0.0.0')
