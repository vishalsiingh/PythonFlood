from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure key

# Simulated database for user data
users = {}
period_data = {}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users:
            flash('Username already exists. Try a different one.')
        else:
            users[username] = password
            period_data[username] = []
            flash('Registration successful! Please log in.')
            return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if users.get(username) == password:
            return redirect(url_for('dashboard', username=username))
        else:
            flash('Invalid credentials. Please try again.')
    return render_template('login.html')

@app.route('/dashboard/<username>', methods=['GET', 'POST'])
def dashboard(username):
    if request.method == 'POST':
        last_period_date = request.form['last_period_date']
        cycle_length = int(request.form['cycle_length'])
        period_data[username] = [last_period_date, cycle_length]
        flash('Data updated successfully!')
    user_data = period_data.get(username, [])
    return render_template('dashboard.html', username=username, user_data=user_data)

@app.route('/tips')
def tips():
    tips_list = [
        "Stay hydrated to reduce bloating.",
        "Maintain a balanced diet rich in iron and vitamins.",
        "Exercise regularly to ease cramps.",
        "Track your cycle to anticipate symptoms.",
        "Consult a doctor if you experience irregular or painful cycles."
    ]
    return render_template('tips.html', tips=tips_list)

# HTML templates
home_html = """
<!DOCTYPE html>
<html>
<head><title>Period Tracker</title></head>
<body>
<h1>Welcome to the Period Tracker App</h1>
<a href="/register">Register</a> | <a href="/login">Login</a> | <a href="/tips">Health Tips</a>
</body>
</html>
"""

register_html = """
<!DOCTYPE html>
<html>
<head><title>Register</title></head>
<body>
<h1>Register</h1>
<form method="POST">
    Username: <input type="text" name="username"><br>
    Password: <input type="password" name="password"><br>
    <input type="submit" value="Register">
</form>
</body>
</html>
"""

login_html = """
<!DOCTYPE html>
<html>
<head><title>Login</title></head>
<body>
<h1>Login</h1>
<form method="POST">
    Username: <input type="text" name="username"><br>
    Password: <input type="password" name="password"><br>
    <input type="submit" value="Login">
</form>
</body>
</html>
"""

dashboard_html = """
<!DOCTYPE html>
<html>
<head><title>Dashboard</title></head>
<body>
<h1>Welcome, {{ username }}</h1>
<h2>Track Your Period</h2>
<form method="POST">
    Last Period Date (YYYY-MM-DD): <input type="text" name="last_period_date"><br>
    Cycle Length (days): <input type="number" name="cycle_length"><br>
    <input type="submit" value="Save">
</form>
{% if user_data %}
<p>Your Last Period: {{ user_data[0] }}</p>
<p>Your Cycle Length: {{ user_data[1] }} days</p>
{% endif %}
<a href="/">Home</a>
</body>
</html>
"""

tips_html = """
<!DOCTYPE html>
<html>
<head><title>Health Tips</title></head>
<body>
<h1>Menstrual Health Tips</h1>
<ul>
{% for tip in tips %}
    <li>{{ tip }}</li>
{% endfor %}
</ul>
<a href="/">Home</a>
</body>
</html>
"""

# Add templates
templates = {
    'home.html': home_html,
    'register.html': register_html,
    'login.html': login_html,
    'dashboard.html': dashboard_html,
    'tips.html': tips_html,
}

@app.route('/get_template/<template>')
def get_template(template):
    return templates.get(template, 'Template not found.')

if __name__ == '__main__':
    app.run(debug=True)
