from flask import Flask, render_template, request
from genome_model import predict_sequence

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    result = None
    features = None
    sequence = ""
    error = None

    if request.method == "POST":

        sequence = request.form.get("sequence", "")

        try:
            result, features = predict_sequence(sequence)

        except ValueError as e:
            error = str(e)

    return render_template(
        "index.html",
        result=result,
        features=features,
        sequence=sequence,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True)