import flask

app = flask.Flask(__name__)
TVshows =["Peaky Blinders","Money Heist","The Witcher","Castlevania","The Queen's Gambit"]
images = ["/static/pb.jpg","/static/mh.jpg","/static/tw.jpg","/static/c.jpg","/static/tqg.jpg"]
@app.route("/")  # Python decorator
def main():
    return flask.render_template("index.html",len = len(TVshows), TVshows = TVshows, images = images)

app.run(
    use_reloader = True,
    debug=True
)