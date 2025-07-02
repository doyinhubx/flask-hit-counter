import os

from flask import Flask, render_template_string

app = Flask(__name__)
counter = {"visits": 0}

html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Visit Counter</title>
    <style>
        body {
            font-family: 'Segoe UI', sans-serif;
            background-color: #f0f4f8;
            text-align: center;
            padding-top: 100px;
        }
        h1 {
            color: #333;
            font-size: 48px;
        }
        p {
            font-size: 24px;
            color: #555;
        }
        .counter {
            background-color: #ffffff;
            border-radius: 10px;
            display: inline-block;
            padding: 30px 50px;
            box-shadow: 0 5px 20px rgba(0, 0, 0, 0.1);
        }
        .reset-button {
            margin-top: 30px;
            background-color: #0066cc;
            color: white;
            border: none;
            padding: 10px 20px;
            font-size: 18px;
            border-radius: 5px;
            cursor: pointer;
        }
        .reset-button:hover {
            background-color: #005bb5;
        }
    </style>
</head>
<body>
    <div class="counter">
        <h1>Hello!</h1>
        <p>
            You’ve visited this page
            <strong>{{ visits }}</strong>
            time{{ 's' if visits != 1 else '' }}.
        </p>
        <form action="/reset" method="post">
            <button class="reset-button">Reset Counter</button>
        </form>
    </div>
</body>
</html>
"""


@app.route("/", methods=["GET"])
def home():
    counter["visits"] += 1
    return render_template_string(html_template, visits=counter["visits"])


@app.route("/reset", methods=["POST"])
def reset():
    counter["visits"] = 0
    return render_template_string(html_template, visits=counter["visits"])


# if __name__ == '__main__':
#     # Read debug flag securely from environment
#     debug_mode = os.environ.get("FLASK_DEBUG", "false").lower() == "true"
#     app.run(debug=debug_mode, port=8000)

if __name__ == '__main__':
    debug_mode = os.getenv("FLASK_DEBUG", "false").lower() == "true"
    app.run(debug=debug_mode, port=8000)
