from sys import modules

from app import app, render_template

@app.route("/")
@app.route("/admin")
@app.route("/admin/dashboard")
def dashboard():
    module = 'dashboard'
    return render_template("admin/dashboard.html", module=module )