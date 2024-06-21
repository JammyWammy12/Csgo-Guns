from flask import Flask, render_template, request

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


@app.route('/guns/<table_type>')
def render_guns_page(table_type):  # put application's code here

    query = "SELECT id, name, kill_award, kills_to_rebuy, damage, clip_size, max_ammo FROM csgo_guns WHERE team = ? OR all_guns = ?"

    conn = create_connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute(query, (table_type, table_type, ))

    data_list = cursor.fetchall()
    print(data_list)

    return render_template('guns.html', data=data_list, table_type=table_type)


@app.route('/search', methods=['GET', 'POST'])
def render_search_page():
    look_up = request.form['Search']
    title = "Search for: '" + look_up + "' "
    look_up = "%" + look_up + "%"

    query = "SELECT id, name, kill_award, kills_to_rebuy, damage, clip_size, max_ammo FROM csgo_guns WHERE name LIKE ?"

    conn = create_connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute(query, (look_up, ))

    data_list = cursor.fetchall()
    print(data_list)

    return render_template('guns.html', data=data_list, table_type=title)
















if __name__ == '__main__':
    app.run()
