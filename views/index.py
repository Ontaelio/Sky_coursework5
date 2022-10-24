from flask import Blueprint, render_template, request, url_for


index_blueprint = Blueprint('index_blueprint', __name__, template_folder='templates')


@index_blueprint.route('/', methods=['GET'])
def start_page():
    return render_template('index.html')