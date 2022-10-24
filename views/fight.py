import json

from flask import Blueprint, render_template, request, redirect
import requests

from views.view_utils import get_game_data, get_game_status
from defaults import GAME_SERVER

choose_hero_blueprint = Blueprint('choose_hero_blueprint', __name__, template_folder='templates')
fight_blueprint = Blueprint('fight_blueprint', __name__, template_folder='templates')

units = {}
current_game = {'game_id': 0, 'pass': 0}


@choose_hero_blueprint.route('/choose-hero/', methods=['GET', 'POST'])
def chose_hero_page():
    global units

    result = get_game_data()

    if request.method == "POST":
        units["player_name"] = request.form['name']
        units["player_role"] = request.form['unit_class']
        units["player_armor"] = request.form['armor']
        units["player_weapon"] = request.form['weapon']
        return redirect('/choose-enemy/')

    return render_template('hero_choosing.html', result=result)


@choose_hero_blueprint.route('/choose-enemy/', methods=['GET', 'POST'])
def chose_enemy_page():
    global units
    global current_game

    result = get_game_data()
    result['header'] = 'Выбор врага'

    if request.method == "POST":
        units["enemy_name"] = request.form['name']
        units["enemy_role"] = request.form['unit_class']
        units["enemy_armor"] = request.form['armor']
        units["enemy_weapon"] = request.form['weapon']
        data = json.loads(requests.post(f'{GAME_SERVER}/start', json=units).content)
        current_game['game_id'] = data['game_id']
        current_game['pass'] = data['pass']
        return redirect('/fight/')

    return render_template('hero_choosing.html', result=result)


@fight_blueprint.route('/fight/', methods=['GET', 'POST'])
def fight():
    heroes = get_game_status(current_game['game_id'])
    return render_template('fight.html', heroes=heroes, result='Бой начался!')


@fight_blueprint.route('/fight/hit', methods=['GET'])
def attack():
    payload = {'game_id': current_game['game_id'], 'action': 'attack'}
    raw_data = requests.get(f"{GAME_SERVER}/turn/", params=payload)
    heroes = get_game_status(current_game['game_id'])

    if raw_data.status_code == 400:
        return render_template('fight.html', heroes=heroes, result='Битва окончена!')

    data = raw_data.json()
    return render_template('fight.html', heroes=heroes, result=data['text'])


@fight_blueprint.route('/fight/use-skill', methods=['GET'])
def use_skill():
    payload = {'game_id': current_game['game_id'], 'action': 'skill'}
    raw_data = requests.get(f"{GAME_SERVER}/turn/", params=payload)
    heroes = get_game_status(current_game['game_id'])

    if raw_data.status_code == 400:
        return render_template('fight.html', heroes=heroes, result='Битва окончена!')

    data = raw_data.json()
    return render_template('fight.html', heroes=heroes, result=data['text'])


@fight_blueprint.route('/fight/pass-turn', methods=['GET'])
def pass_turn():
    payload = {'game_id': current_game['game_id'], 'action': 'pass'}
    raw_data = requests.get(f"{GAME_SERVER}/turn/", params=payload)
    heroes = get_game_status(current_game['game_id'])

    if raw_data.status_code == 400:
        return render_template('fight.html', heroes=heroes, result='Битва окончена!')

    data = raw_data.json()
    return render_template('fight.html', heroes=heroes, result=data['text'])


@fight_blueprint.route('/fight/end-fight', methods=['GET'])
def end_game():
    payload = {'game_id': current_game['game_id'], 'pass': current_game['pass']}
    requests.delete(f"{GAME_SERVER}/delete/", params=payload)
    return redirect('/')


