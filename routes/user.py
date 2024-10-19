from app import app, render_template


@app.route("/admin/user/userlist")
def user():
    modules = 'user'
    return render_template("admin/userlist.html",module=modules)

@app.route("/admin/user/adduser")
def adduser():
    moduless = 'adduser'
    return render_template("admin/adduser.html", module=moduless)