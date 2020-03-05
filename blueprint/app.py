from flask import Flask
import teams

app = Flask(__name__)
app.register_blueprint(teams.teams)

if __name__ == "__main__":
    app.run()