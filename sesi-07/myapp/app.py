from flask import Flask, render_template, request
from markupsafe import escape
import webbrowser

from author_book import author_books

app = Flask(__name__, template_folder='templates')


# @app.route('/user/<username>')
# def show_user_profile(username):    
#     # show the user profile for that user    
#     return f'User {escape(username)}'

# @app.route('/post/<int:post_id>')
# def show_post(post_id):    
#     # show the user profile for that user    
#     return f'Post {post_id}'

# @app.route('/path/<path:subpath>')
# def show_subpath(subpath):    
#     # show the subpath after /path/    
#     return f'Subpath {escape(subpath)}'

# @app.route('/hello/')
# @app.route('/hello/<name>')
# def hello(name=None):    
#     return render_template('hello.html', name=name)

# @app.route('/<name>')
# def hello_name(name):
#     # number = 10
#     return f'Hello, {escape(name)}!'

@app.route('/home')
# @app.route('/')
def home():
    return 'Welcome'



@app.route('/author', methods=['GET', 'POST'])
def author():
    if 'author_id' in request.form:
        author_books[request.form['author_id']] = []

    return render_template('author.html', author_books = author_books)
    






@app.route('/books/<int:author_id>')
def books(author_id):
    if len(author_books[author_id]) == 0:
        return render_template('book.html', author_id = author_id)
    return render_template('book.html', author_id = author_id, list_books=author_books[author_id])



# dijalankan sebagai standalone script, nilai == main
if __name__ == '__main__':
    # webbrowser.open_new('http://127.0.0.1:5000/')
    app.run(debug=True) 