from flask import Flask, jsonify
import pymysql

class Stores():
    def get_all():
        conn = pymysql.connect(host='localhost', db='crawling', user='root', passwd='1234', charset='utf8')
        curdic = conn.cursor(pymysql.cursors.DictCursor)
        sql = "SELECT * FROM mojjimoddi"
        curdic.execute(sql)
        store_lists = curdic.fetchall()
        return store_lists


app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False

@app.route('/')
def test():
    data = Stores.get_all()
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)