import pymysql
import creds 
from flask import Flask
from flask import render_template, request, flash, redirect, url_for

app = Flask(__name__)

def get_conn():
    conn = pymysql.connect(
        host= creds.host,
        user= creds.user, 
        password = creds.password,
        db=creds.db,
        )
    return conn

def execute_query(query, args=()):
    try:
        cur = get_conn().cursor()
        cur.execute(query, args)
        rows = cur.fetchall()
        cur.close()
        return rows
    except Exception as e:
        print("Error:", e)
        return []
    
#display the sqlite query in a html table
def display_html(rows):
    html = ""
    html += """<table><tr><th>ArtistID</th><th>Artist</th><th>Track Title</th><th>Price</th><th>Milliseconds</th></tr>"""

    for r in rows:
        html += "<tr><td>" + str(r[0]) + "</td><td>" + str(r[1]) + "</td><td>" + str(r[2]) + "</td><td>" + str(r[3]) + "</td><td>" + str(r[4]) + "</td></tr>"
    html += "</table></body>"
    return html

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'viewdb':
            return redirect(url_for('viewdb'))
        elif action == 'top_artists':
            return redirect(url_for('top_artists'))
        elif action == 'price':
            return redirect(url_for('price_form'))
        elif action == 'time':
            return redirect(url_for('time_form'))
        else:
            flash("Please select an option.", "warning")
            return redirect(url_for('home'))
    return render_template('home.html')


@app.route("/viewdb")
def viewdb():
    rows = execute_query("""SELECT ArtistId, Artist.Name, Track.Name, UnitPrice, Milliseconds
                FROM Artist JOIN Album using (ArtistID) JOIN Track using (AlbumID)
                ORDER BY Track.Name 
                Limit 500""")
    return display_html(rows)

@app.route("/timequery/<time>")
def viewtime(time):
    nrows = execute_query("""select ArtistId, Artist.Name, Track.Name, UnitPrice, Milliseconds
            from Artist JOIN Album using (ArtistID) JOIN Track using (AlbumID)
            where Milliseconds > %s order by Track.Name 
            Limit 500""", (str(time)))
    return display_html(nrows) 

@app.route("/pricequery/<price>")
def viewprices(price):
    rows = execute_query("""select ArtistId, Artist.Name, Track.Name, UnitPrice, Milliseconds
            from Artist JOIN Album using (ArtistID) JOIN Track using (AlbumID)
            where UnitPrice = %s order by Track.Name 
            Limit 500""", (str(price)))
    return display_html(rows)

@app.route("/pricequerytextbox", methods = ['GET'])
def price_form():
  return render_template('textbox.html', fieldname = "Price")

@app.route("/pricequerytextbox", methods = ['POST'])
def price_form_post():
  text = request.form['text']
  return viewprices(text)

@app.route("/timequerytextbox", methods = ['GET'])
def time_form():
    return render_template('textbox.html', fieldname = "Milliseconds")

@app.route("/timequerytextbox", methods = ['POST'])
def time_form_post():
    text = request.form['text']
    return viewtime(text)

@app.route("/top-artists")
def top_artists():
    nrows = execute_query("""select Artist.Name, COUNT(Track.TrackId) as TrackCount 
            from Artist join Album using (ArtistId) join Track using (AlbumId) 
            group by Artist.ArtistId order by TrackCount desc limit 10""")
    html = "<h2>Top 10 Artists by Track Count</h2><table><tr><th>Artist</th><th># of Tracks</th></tr>"
    for r in nrows:
        html += "<tr><td>" + str(r[0]) + "</td><td>" + str(r[1]) + "</td></tr>"
    html += "</table>"
    return html

@app.route('/add-new-entry', methods=['GET', 'POST'])
def add_new_entry():
    if request.method == 'POST':
        name = request.form['name']
        album = request.form['album']
        print("Artist Name:", name, ":", "Album Title:", album)
        flash('Artist added successfully!', 'success')
        return redirect(url_for('home'))
    else:
        return render_template('add_new_entry.html')

@app.route('/delete-entry',methods=['GET', 'POST'])
def delete_entry():
    if request.method == 'POST':
        name = request.form['name']
        print("Name to delete:", name)
        flash('User deleted successfully!', 'warning') 
        return redirect(url_for('home'))
    else:
        return render_template('delete_entry.html')

@app.route('/update-entry',methods=['GET', 'POST'])
def update_entry():
    if request.method == 'POST':
        name = request.form['name']
        new_album = request.form['album']
        print("Update:", name, "->", new_album)
        flash('User updated successfully!', 'info')
        return redirect(url_for('home'))
    else:
        return render_template('update_entry.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug = True)