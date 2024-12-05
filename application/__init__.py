
from flask import Flask, render_template, request
from markupsafe import escape

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('base.html')


@app.route('/login', methods=['GET', 'POST'])
def showLogin():
    email_address = None
    password = None
    varia = None
    if request.method == 'POST':
        

        email_address = request.form.get('email_address') or 'No email provided'
        password = request.form.get('password') or 'No password provided'
        varia = 'POST'
    else:
        varia = 'Get'


    names = ['lesther', 'john', 'greco', 'elijah', 'bobz', 'clay', 'cody', 'chuchay', 'frodo', 'chibi', 'nabi']

    return render_template('login.html', varia = varia, array_names = names, email_address = email_address, password = password)


@app.route('/signup', methods=['GET', 'POST'])
def showSignup():
    return render_template('signup.html')

@app.route('/super')
def showSuper():
    return render_template('super.html')


if __name__ == "__main__":
    app.run(debug=True)