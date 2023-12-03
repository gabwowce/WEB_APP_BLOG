from flask import Flask, render_template, request, redirect, url_for, flash, redirect
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from forms import RegistrationForms, LoginForm
import mysql.connector
from datetime import date

app = Flask(__name__)

app.config["SECRET_KEY"] = "hjk@#%$saasdhj234kasdhjk3245asdh"


public_blogs = [
  {
    "author": "Tom",
    "title": "My special day",
    "content": "Today is the super happy day for me. Today i became a programmer. Two years ago I cant even imagine this happening to me, but the day has come and the birds flying high.\r\n\r\nI always liked mathematical problem solving in the school, then I realized, that in general, i like solve the problems. Problems that may appear at first sight that are unsolvable. I like put the time on it, and receive from it biggest pleasures, when it eventually solved.\r\n\r\nIn the future, i want to wish for myself health and love. Because I know that my money will never run out. \r\n\r\n\r\nI know that one day I will have everything that i cant even imagine, because I work a lot on myself and my future career. I am not a very good writer, especially in English. But I work a lot on it. I know that in my field it is crucial to be able communicate well in English. Even I am trying a lot, even I am watching a lot of movies in English, or listening English music, it seems does not helping me. I can not write in Lithuanian correctly, so how can we talk about English??\r\n\r\nI know that this is my biggest problem, it is rock inside of me, witch I can not get rid of, but i will. Like I said in the beginning - I like solving problems. I will solve this too.",
    "date_posted": 2023,
    "post_type": "public",
    "name": ""
  },
  {
    "author": "Gabrie",
    "title": "Stanisław Lem's Prescient Vision of Artificial Life",
    "content": "In the grand tradition of H. G. Wells and Jules Verne, Stanisław Lem’s “The Invincible” tells the story of a space cruiser sent to an obscure planet to determine the fate of a sister spaceship whose communication with Earth has abruptly ceased. Landing on the planet Regis III, navigator Rohan and his crew discover a form of life that has apparently evolved from autonomous, self-replicating machines — perhaps the survivors of a “robot war.” Rohan and his men are forced to confront the classic quandary: What course of action can humanity take once it has reached the limits of its knowledge? In “The Invincible,” Lem has his characters confront the inexplicable and the bizarre: the problem that lies just beyond analytical reach.\r\n\r\nThe following is literary critic and theorist N. Katherine Hayles’ foreword to the 2020 edition of Lem’s classic novel, which was originally published in Polish in 1964.\r\n\r\nScience fiction has famously predicted many of the important technologies of the 20th century: space travel, satellites, the atomic bomb, television, the internet, and virtual reality, to name a few. In “The Invincible,” Stanisław Lem predicts another: artificial life. Although speculations about self-reproducing artificial systems date from the 1940s, the scientific field received its name from Christopher Langton only in 1986, more than two decades after the original publication of “The Invincible” (1964). One of the central controversies in artificial life is whether evolutionary programs and devices are actually alive (the strong version), or whether they merely simulate life (the weak version). Researchers who follow the strong version argue that the processes embedded in software programs such as genetic algorithms are as “natural” as life itself; what is artificial is the medium in which these processes take place.",
    "date_posted": 2021,
    "post_type": "public",
    "name": ""
  }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', public_blogs=public_blogs)


@app.route('/about')
def about():
    return render_template('about.html', title="About")


@app.route('/register', methods=["GET", "POST"])
def register():
  form = RegistrationForms()
  if form.validate_on_submit():
    flash(f"Account created for {form.username.data}!", category="success")
    return redirect(url_for("home"))
  return render_template("register.html", title="Register", form=form)

@app.route('/login')
def login():
  form = LoginForm()
  return render_template("login.html", title="Login", form=form)

if __name__ == "__main__":
    app.run(debug=True)