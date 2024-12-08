from flask import Flask, render_template, request

app = Flask(__name__)

d_base = {}

@app.route('/register', methods=["POST", "GET"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    else:
        form_data = request.form
        username = form_data.get("username")
        password = form_data.get("password")

        d_base["username"] = "username"
        d_base["password"] = "password"
        return render_template("login.html", name=username)


@app.route ('/login', methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        form_data = request.form
        username = form_data.get("username")
        password = form_data.get("password")
        print(f'the username is {username}')
        print(f'the password is {password}')
    
    
        if d_base.get("username") == username and d_base.get("password") == password:
            return "welcome to your account"
        else:
            return "wrong details"
    
    
app.run(debug=True)