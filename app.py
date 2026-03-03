from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)

DATA_FILE = "posts.json"


def ensure_data_file():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump([], f, ensure_ascii=False, indent=2)


def load_posts():
    ensure_data_file()
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_posts(posts):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(posts, f, ensure_ascii=False, indent=2)


def get_next_id(posts):
    if not posts:
        return 1
    return max(p["id"] for p in posts) + 1


def fetch_post_by_id(posts, post_id):
    for post in posts:
        if post.get("id") == post_id:
            return post
    return None



@app.route("/")
def index():
    blog_posts = load_posts()
    return render_template("index.html", posts=blog_posts)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        posts = load_posts()

        author = request.form.get("author", "").strip()
        title = request.form.get("title", "").strip()
        content = request.form.get("content", "").strip()

        if not author or not title or not content:
            return render_template(
                "add.html",
                error="Bitte fülle alle Felder aus!",
                author=author,
                title=title,
                content=content,
            )

        new_post = {
            "id": get_next_id(posts),
            "author": author,
            "title": title,
            "content": content,
        }

        posts.append(new_post)
        save_posts(posts)

        return redirect(url_for("index"))

    return render_template("add.html")


@app.route("/delete/<int:post_id>")
def delete(post_id):
    posts = load_posts()

    # remove matching post
    posts = [post for post in posts if post.get("id") != post_id]
    save_posts(posts)

    return redirect(url_for("index"))


@app.route("/update/<int:post_id>", methods=["GET", "POST"])
def update(post_id):
    posts = load_posts()

    post_index = None
    for i, p in enumerate(posts):
        if p.get("id") == post_id:
            post_index = i
            break

    if post_index is None:
        return "Post not found", 404

    if request.method == "POST":
        author = request.form.get("author", "").strip()
        title = request.form.get("title", "").strip()
        content = request.form.get("content", "").strip()

        if not author or not title or not content:
            temp_post = posts[post_index].copy()
            temp_post["author"] = author
            temp_post["title"] = title
            temp_post["content"] = content
            return render_template(
                "update.html",
                post=temp_post,
                error="Bitte alle Felder ausfüllen!",
            )

        posts[post_index]["author"] = author
        posts[post_index]["title"] = title
        posts[post_index]["content"] = content

        save_posts(posts)
        return redirect(url_for("index"))

    post = posts[post_index]
    return render_template("update.html", post=post)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)