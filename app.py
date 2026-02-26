from flask import Flask, request, jsonify
from match import calculate_score

app = Flask(__name__)

@app.route("/match", methods=["POST"])
def match():
    data = request.json
    resume = data["resume"]
    job = data["job"]

    score = calculate_score(resume, job)

    return jsonify({"score": score})

if __name__ == "__main__":
    app.run(port=8000)