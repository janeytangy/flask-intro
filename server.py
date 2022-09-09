"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Start Page</title>
      </head>
      <body>
        Hi! This is the home page. Go to <a href="/hello">hello</a>.
      </body>
    </html>
    """


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <h2>Please fill out the below for a compliment.</h2>
        <form action="/greet">
          <section>
          What's your name? <input type="text" name="person">
          </section>
          <section>
          Which compliment would you like to receive?
          <select name="nice_thing">
            <option value="awesome">Awesome</option>
            <option value="terrific">Terrific</option>
            <option value="fantastic">Fantastic</option>
          </select>
          </section>
          <input type="submit" value="Submit">
        </form>

        <h2>Please fill out the below for a DISS.</h2>
        <form action="/diss">
          <section>
          What's your name? <input type="text" name="person">
          </section>
          <section>
          Which insult would you like to receive?
          <select name="mean_thing">
            <option value="ugly">Ugly</option>
            <option value="annoying">Annoying</option>
            <option value="stupid">Stupid</option>
          </select>
          </section>
          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("nice_thing")
    # compliment = choice(AWESOMENESS)

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {compliment}!
      </body>
    </html>
    """

@app.route('/diss')
def insult_person():
  """Dish out an insult."""

  player = request.args.get("person")

  insult = request.args.get("mean_thing")
  # compliment = choice(AWESOMENESS)

  return f"""
  <!doctype html>
  <html>
    <head>
      <title>A DISS</title>
    </head>
    <body>
      Hi, {player}! I think you're {insult}!
    </body>
  </html>
  """


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
