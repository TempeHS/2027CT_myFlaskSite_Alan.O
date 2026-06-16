from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/library")
def library():
    return render_template("library.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/search")
def search():
    query = request.args.get("q", "").strip().lower()
    page_map = {
        "about": "about",
    }

    if query in page_map:
        return redirect(url_for(page_map[query]))

    return render_template("search.html", query=query)

    # if no match, show search page
    return render_template("search.html", query=query)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
