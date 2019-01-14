from flask import Flask, render_template, request, session, redirect
from models.bike import Bike
import mlab

app = Flask(__name__)
mlab.connect()

@app.route('/new_bike', methods=['GET','POST'])
def add_charactnew_bikeer():
    #1: gửi form(GET)
    if request.method == "GET":
        return render_template("new_bike.html")
    elif request.method == "POST":
  #4: nhận form => Lưu (POST)
        form = request.form 
        model = form["model"]
        fee = form["fee"]
        image = form["image"]
        year = form["year"]
        print(model, fee, image, year)
        new_bike = Bike(model=model, fee=fee, image=image, year=year)
        new_bike.save()
        return "Gotcha"



if __name__ == '__main__':
  app.run(debug=True)