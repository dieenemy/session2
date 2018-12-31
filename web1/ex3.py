from flask import Flask, render_template

app = Flask(__name__)


@app.route("/user/<username>")
def user_profile(username):
    users = {
        "tung": {
            "name": "tung",
            "age": 23,
        },
        "hung": {
            "name": "hung",
            "age": 23,
        }
    }
    return render_template("user.html", users=users,username=username)
if __name__ == "__main__": 
    app.run(debug=True)



if __name__ == "__main__":
    app.run(debug=True)