import mysql.connector
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def datasearch():
    ''' Gathers all gene description that have a specific
        search term as substring
    :return: renders html template
    '''

    # if the method is POST
    if request.method == "POST":
        zoekterm = request.form["term"]

        # database connection info
        db_info = {"user": "anonymous", "host": "ensembldb.ensembl.org",
                   "port": 3306,
                   "db": "homo_sapiens_core_91_38"}

        # create connection
        conn = mysql.connector.connect(**db_info)

        # create cursor
        cursor = conn.cursor()

        # gathers all descriptions that contain 'zoekterm'
        cursor.execute(f"SELECT description "
                       f"FROM gene "
                       f"WHERE description "
                       f"like '%{zoekterm}%'")

        # fetches everything from cursor
        genen = cursor.fetchall()

        # closes connections
        cursor.close()
        conn.close()
        return render_template("Afvink3.html", term=zoekterm, genes=genen)
    else:
        return render_template("Afvink3.html")


def main():
    app.run(debug=True)

main()