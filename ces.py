from flask import Flask,render_template,redirect,request, session, g
import sqlite3
app = Flask(__name__)

app.config['SECRET_KEY'] = "Thisisasecret!!!"


# database connection code
def connect_db():
    sql = sqlite3.connect('data.db')
    sql.row_factory = sqlite3.Row
    return sql

def get_db():
    if not hasattr(g,'sqlite_db'):
        g.sqlite_db=connect_db()
    return g.sqlite_db
@app.teardown_appcontext
def close_db(error):
    if hasattr(g,'sqlite_db'):
        g.sqlite_db.close()
#database connection code ends



@app.route('/',methods=["GET","POST"])
def index():
    if request.method=="POST":
        id = request.form['id']
        try:
            db = get_db()
            cur = db.execute("select * from certi where id=?",[id])
            res = cur.fetchone()
            return "{}".format(res['name'])
        except:
            return "not found"
    return render_template('verify.html')


if __name__ == "__main__":
    app.run(debug=True)
