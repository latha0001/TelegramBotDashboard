from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def dashboard():
    return render_template('dashboard.html')  # Render the dashboard HTML
@app.route('/')
def home():
    return render_template('home.html')  # Render the home page

@app.route('/analytics')
def analytics():
    return render_template('analytics.html')  # Render the analytics page

@app.route('/settings')
def settings():
    return render_template('settings.html')  # Render the settings page

@app.route('/help')
def help_page():
    return render_template('help.html')  # Render the help page
if __name__ == '__main__':
    app.run(debug=True)