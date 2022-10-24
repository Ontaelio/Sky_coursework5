from flask import Flask, jsonify, abort, request, render_template, send_from_directory

from views.index import index_blueprint
from views.fight import choose_hero_blueprint, fight_blueprint

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False

app.register_blueprint(index_blueprint)
app.register_blueprint(choose_hero_blueprint)
app.register_blueprint(fight_blueprint)


if __name__ == '__main__':
    print(app.url_map)
    app.run(port=5005)
