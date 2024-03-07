from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Sample list of tasks (you can replace this with a database)
tasks = []


@app.route("/")
def index():
    return render_template("index.html", tasks=tasks)


@app.route("/add_task", methods=["POST"])
def add_task():
    task = request.form.get("task")
    if task:
        tasks.append(task)
    return redirect(url_for("index"))


@app.route("/delete_task/<int:index>")
def delete_task(index):
    if 0 <= index < len(tasks):
        del tasks[index]
    return redirect(url_for("index"))


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=5000)
