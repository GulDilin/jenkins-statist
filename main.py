from flask import Flask, request, escape
import json
import psycopg2

conn = None
cursor = None

app = Flask(__name__)
LOG_PATH = 'C:/Progs/statlog.txt'
log_file = open(LOG_PATH, "w")


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/steps/')
def print_build_steps():
    data = request.data
    print(data)
    return "OK"


@app.route('/build/', methods=['GET', 'POST'])
def print_builds():
    data = str(request.data)[2:-1].replace("\'", '"')
    print(f"data = {data}")
    data_json = json.loads(data)
    print(f"data_json = {data_json}")
    timestamp = data_json['timestamp'].replace("T", " ")
    status = data_json['status']
    node = data_json['node']
    date = data_json['date']

    cursor.execute(f'''INSERT INTO BUILD
        VALUES (\'{timestamp}\', \'{status}\', \'{node}\', \'{date}\');''')
    conn.commit()
    return "OK"


@app.route('/project/')
def print_project():
    data = request.data
    print(data)
    # return "project"


@app.route('/checkout/')
def print_checkout():
    data = request.data
    print(data)
    return "check"


@app.route('/queues/', methods=['GET', 'POST'])
def print_queues():
    data = request.data
    print(data)
    return "queues"


if __name__ == '__main__':
    conn = psycopg2.connect(dbname='mydb',
                        user='postgres',
                        password='',
                        host='localhost',
                        port="5433")
    cursor = conn.cursor()
    print("Database opened successfully")
    app.run()
    conn.close()
    log_file.close()
