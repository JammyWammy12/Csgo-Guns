from flask import Flask, render_template

app = Flask(__name__)
DATABASE = "csgoguns.db"
import sqlite3
from sqlite3 import Error
def create_connect(db_filename):
    try:
        conn = sqlite3.connect(db_filename)
        return conn
    except Error as e:
        print(e)
        return None



@app.route('/')
def render_home_page():  # put application's code here
    return render_template('home.html')


@app.route('/t_guns')
def render_terrorist_page():  # put application's code here

    query = "SELECT name FROM csgo_guns WHERE terrorist = TRUE"
    conn = create_connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute(query, )

    data_list = cursor.fetchall()
    print(data_list)

    return render_template('t_guns.html', data=data_list)




@app.route('/ct_guns')
def render_counter_terrorist_page():  # put application's code here

    query = "SELECT name FROM csgo_guns WHERE counter_terrorist = TRUE"
    conn = create_connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute(query, )

    data_list = cursor.fetchall()
    print(data_list)


    return render_template('ct_guns.html', data=data_list)



if __name__ == '__main__':
    app.run()
