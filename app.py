# flask import
from flask import Flask, render_template, request
app = Flask(__name__)

# They gave you a base class which is inside of the stories.py file. You need to import his class into your app.py
from stories import story


@app.route('/')
def base_page():
    return render_template("hello.html")


@app.route("/madlibs")
def madlibs_start():
    """ Geneate and show form to ask words"""

    prompts = story.prompts
    return render_template("madlibs_start.html", prompts=prompts)


@app.route("/madlibs_completion")
def madlibs_completion():
   
    text = story.generate(request.args)
    return render_template("madlibs_completion.html", text=text)





if __name__ == '__main__':
    app.run(debug=True)

