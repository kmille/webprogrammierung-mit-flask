from flask import Flask, jsonify, request, render_template
from os import listdir
import giphypop

app = Flask(__name__)


@app.route("/")
def index():
    return "hi"

@app.route("/dirs")
def show_dirs():
    #print(request.headers['user-agent'])
    dest = request.args.get("dest")
    print(dest)
    files = listdir(dest)
    return jsonify(files)

@app.route("/template")
def ret_render_template():
    name = request.args.get("name")
    g = giphypop.Giphy()
    gif = g.random_gif(tag=name)
    return render_template("index.html", user_name=name, gif_url=gif.media_url)


app.run(debug=True)
