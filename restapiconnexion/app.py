from flask import Flask, render_template
import connexion

# create application instancse
# app = Flask(__name__, template_folder="templates")
app = connexion.App(__name__, specification_dir='./')

# read swagger.yml file for configuration
app.add_api('swagger.yml')


# Crate a URL route for "/"
@app.route('/')
def home():
    """
    This function just responds to the browser URL 
    localhost:5000/

    :return: the rendered template 'home.html'
    """
    return render_template('home.html')

# If we're running in stand alone mode, run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)