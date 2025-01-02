from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Data skor
score = {"team_a": 0, "team_b": 0}
max_score = 25  # Maksimal skor untuk pertandingan voli


@app.route("/")
def index():
    return render_template("index.html", score=score, max_score=max_score)


@app.route("/update_score", methods=["POST"])
def update_score():
    global score
    team = request.json.get("team")
    if team in score:
        if score[team] < max_score:
            score[team] += 1
    return jsonify(score)


@app.route("/reset_score", methods=["POST"])
def reset_score():
    global score
    score = {"team_a": 0, "team_b": 0}
    return jsonify(score)


if __name__ == "__main__":
    app.run(debug=True)
