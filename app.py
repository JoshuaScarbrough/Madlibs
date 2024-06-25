# flask import
from flask import Flask, render_template, request
app = Flask(__name__)


# They gave you a base class which is inside of the stories.py file. You need to import his class into your app.py
from stories import Story


@app.route('/')
def base_page():
    return render_template("hello.html")


@app.route("/madlibs")
def madlibs_start():
    """ Geneate and show form to ask words"""

    
    return render_template("madlibs_start.html")


@app.route("/madlibs_completion")
def madlibs_completion():
    place = request.args["place"]
    noun = request.args["noun"]
    verb = request.args["verb"]
    adjective = request.args["adjective"]
    plural_noun = request.args["plural_noun"]
    return render_template("madlibs_completion.html", place=place, noun=noun, verb=verb, adjective=adjective, plural_noun=plural_noun)


if __name__ == '__main__':
    app.run(debug=True)

