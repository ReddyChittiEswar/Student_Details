from flask import Flask, render_template
import person

app = Flask(__name__)

@app.route("/",methods=["GET"])
def persons_list():
    persons = person.listAllPersons()
    return render_template('persons.html',persons = persons)

app.run(debug = True)

