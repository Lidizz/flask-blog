from flask import Flask,render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Lidor Shachar',
        'title': 'Blog Post 1',
        'content': 'Content for the first post',
        'date_posted': 'October 13, 2025'
    },
    {
        'author': 'Kari Karlsen',
        'title': 'Blog Post 2',
        'content': 'Content for the second post',
        'date_posted': 'October 13, 2025'
    }
]
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=True)

# Flask is a lightweight WSGI web application framework in Python.
# It is designed to make getting started quick and easy, with the ability to scale up to complex applications.
# To run the application, use the command: python flaskblog.py or python flaskblog.py
# Then open your web browser and go to http://127.0.0.1:5000 or http://localhost:5000
# Make sure you have Flask installed in your Python environment.
# You can install it using pip:
# pip install Flask

# Flask uses the Jinja2 template engine to render HTML templates.
# The render_template function looks for templates in the "templates" folder by default.
# Make sure you have the following folder structure:
# /your_project
#     /templates
#         home.html
#         about.html
#     flaskblog.py
