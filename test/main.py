
    #!/usr/bin/env python

from flask import Flask,render_template,url_for

app = Flask(__name__)


@app.route("/")
def home():
  return render_template("home.html")
#if __name__=="__main__":
#  app.run()

#@app.route("/esempio")
#def flaskpage():
#  return render_template("flask.html")

@app.route("/login")
def login():
  return render_template("login.html")

#@app.route("/")
#def hello_world():
#    bott ="""
#    
#    <a href="/frank">Continue</a>

#    """
   # <form action="/frank" method="get">
   # <button type="bottone"> Next Page </button> 
   # 
#    return bott #"<p>Hello, World!</p>"

#@app.route("/frank")
#def hello_frank():
#    a  = """
#    <html><header></header><body><h1>Benvenuto</h1><p>Inserisci il tuo nome e cognome.</p>

#     <form action="/login" method="get">
#  <label for="fname">Nome:</label>
#  <input type="text" id="fname" name="fname"><br><br>
#  <label for="lname">Cognome:</label>
#  <input type="text" id="lname" name="lname"><br><br>
#  <button type="submit">Submit</button>
#  <button type="submit" formmethod="post">Submit using POST</button>
#</form> 

 #   </body></html>
 #   """
 #   return a

#@app.route("/login")
#def nome_corrisponde():
#    c = """
#    
#    <html><header></header><body><p>Il tuo nome corrisponde nell'utenza, inserisci la password.</p>
#    </body></html>
#
#    <form action="/action_page.php" method="get">
#  <label for="fname">Password:</label>
#  <input type="text" id="fname" name="fname"><br><br>
#  <button type="submit">Submit</button>
#  <button type="submit" formaction="/frank formmethod="post">Submit using POST</button>
#    </form> 
#
#    """
#    return c

    # <button type="bottone" formaction="/action_page2.php"> Next Page </button>

    

    
