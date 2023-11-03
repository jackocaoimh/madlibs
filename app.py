from flask import Flask, render_template, request
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = 'chickenzarecool21837'

@app.route('/')
def show_questions():
    prompts = story.promts
    return render_template('index.html', prompts = prompts)

@app.route('/results')
def show_results():

    text = story.generate(request.args)
    return render_template('story.hmtl', text=text)