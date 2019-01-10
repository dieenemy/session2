from flask import Flask, render_template, request
import mlab
from models.river import River

app = Flask(__name__)
mlab.connect()

# Ex2
@app.route('/rivers') #hien thi tat ca cac nhan vat
def rivers():
    africa_river_list = River.objects(continent__icontains="Africa")
    return render_template("rivers.html", africa_river_list= africa_river_list)



@app.route('/rivers1') #hien thi tat ca cac nhan vat
def rivers1():
    africa_river_list = River.objects(continent__icontains="S. America", length__lt=1000)
    return render_template("rivers1.html", africa_river_list= africa_river_list)



if __name__ == '__main__':
  app.run(debug=True)