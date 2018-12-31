from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route("/about-me")
def ame():
    a = {
        "Name": "Tran Xuan Tung",
        "Work": "Accountant",
        "School": "ФУ",
        "Hobbies": "...."
    }
    return render_template("about_me.html",
                            about=a)


@app.route("/school")
def techkids():
    return redirect("http://techkids.vn")





if __name__ == "__main__":
    app.run(debug=True)