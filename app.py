from flask import Flask, render_template
app = Flask(__name__)
@app.route('/', methods = ['GET'])
def home():
    Top_restaurants=[
        "Thank God Its Friday",
        "Pablos",
        "Barbeque Nation",
        "CoSo"
    ]
    return render_template('landingpage.html',rest_list=Top_restaurants)
@app.route('/search', methods=['GET'])
def search():
    return render_template('search.html')
@app.route('/mybookings',methods=['GET'])
def mybookings():
    return render_template('mybookings.html')
if __name__=="__main__":
    app.debug=True
    app.run(host='0.0.0.0', port=3000)