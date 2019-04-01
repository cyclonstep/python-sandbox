from flask import Flask, Response
from flask_principal import Principal, Permission, RoleNeed
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask_wtf import Form, TextField, PasswordField, Required, Email


app = Flask(__name__)

# load the extension
principals = Principal(app)
login_manager = LoginManager(app)

# Create a permission with a single Need, in this case a RoleNeed.
admin_permission = Permission(RoleNeed('admin'))

# User loader 
@login_manager.user_loader
def load_user(userid):
        # Return an instance of the User model
        return datastore.find_user(id=userid)

class LoginForm(Form):
        email = TextField()
        password = PasswordField()

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#         # A hypothetical login form that uses Flask-WTF
#         form = LoginForm()

#         # Validate form input 
#         if form.validate_on_submit():
#                 # Retrieve the user from the hypothetical datastore
#                 user = datastore.find_user(email=form.email.data)


# Protect a view with a principal for that need
@app.route('/admin')
@admin_permission.require(http_exception=403)
def do_admin_index():
    return Response('Only if you are an admin')

# This time  protect with a context manager
@app.route('/articles')
def do_articles():
    with admin_permission.require():
        return Response('Only if you are admin')


