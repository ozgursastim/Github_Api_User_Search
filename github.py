from flask import Flask, render_template, request
import requests

app = Flask(__name__)

baseurl = "https://api.github.com/users/"

@app.route("/", methods = ["GET", "POST"])
def index():

    if request.method == "POST":
        # form üzerindeki github kullanıcı alanı text kutusundaki değer alınmaktadır.
        githubname = request.form.get("githubname")
        # requests.get ile url isteği gmnderilmektedir.
        response_user = requests.get(baseurl + githubname)
        response_repos = requests.get(baseurl + githubname + "/repos")
        # response nesnesi bir json verisine dönüştürülmektedir
        userInfo = response_user.json()
        reposInfo = response_repos.json()
        # json verisi bir sözlük olarak kullanılabildiği için sözlük kullanımı ile veriler alınmaktadır.
        # json verisi index.html sayfasına gönderilmektedir.
        if "message" in userInfo:
            return render_template("index.html", error = "No user found")
        else:
            return render_template("index.html", profile = userInfo, repos = reposInfo)
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)