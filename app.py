from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def render_home_page():  # put application's code here
    return render_template('home.html')


@app.route('/t_guns')
def render_terrorist_page():  # put application's code here
    return render_template('ct_guns.html')



@app.route('/ct_guns')
def render_counter_terrorist_page():  # put application's code here
    return render_template('t_guns.html')



if __name__ == '__main__':
    app.run()
