from flask import Flask, request, jsonify

from game_objects.equipment import EquipmentList
from game_objects.game import GamePlayerVsAI
from game_objects.units import create_unit
from game_objects.arena import Arena

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

games = {}


@app.route('/start', methods=['POST'])
def start_game():
    """
    Expected incoming json:
    "player_name": str
    "player_role": str
    "player_armor": str
    "player_weapon": str
    "enemy_name": str
    "enemy_role": str
    "enemy_armor": str
    "enemy_weapon": str
    """
    global games
    data = request.json
    equipment = EquipmentList()
    equipment.get_data("./data/equipment.json")
    player = create_unit(data["player_name"], data["player_role"])
    enemy = create_unit(data["enemy_name"], data["enemy_role"])
    arena = Arena()
    game = GamePlayerVsAI(arena, player, enemy)
    response = game.game_start(
        equipment=equipment,
        player_weapon=data["player_weapon"],
        player_armor=data["player_armor"],
        enemy_weapon=data["enemy_weapon"],
        enemy_armor=data["enemy_armor"]
    )
    games[game.game_id] = game
    return jsonify({"game_id": game.game_id,
                    "pass": game.game_password,
                    "text": response,
                    "game_info": game.get_full_description()})


@app.route('/turn/', methods=['GET'])
def make_turn():
    """
    expects:
    "game_id": int
    "command": str (attack, skill, pass)
    """
    global games
    game_id = int(request.args.get('game_id'))
    action = request.args.get('action')
    # data = request.json
    game = games[game_id]
    if game.check_status() == 'game on':
        response = {
            "status": game.check_status(),
            "text": game.make_turn(action),
            "player": game.get_player_stats(),
            "enemy": game.get_enemy_stats()
        }
        return jsonify(response)
    return 'game over', 400


@app.route('/game/<int:game_id>', methods=['GET'])
def get_game_info(game_id):
    try:
        return jsonify(games[game_id].get_full_description())
    except KeyError:
        return 'Такой игры нет', 404


@app.route('/delete/', methods=['DELETE'])
def delete_game():
    """
    Expects parameters 'game_id' and 'pass'
    """
    game_id = int(request.args.get('game_id'))
    game = games[game_id]
    game_pass = int(request.args.get('pass'))
    if game_pass != game.game_password:
        return 'Bad password', 400
    response = game.game_end()
    games.pop(game_id)
    return response


@app.route('/equipment', methods=['GET'])
def get_equipment_list():
    """
    Get all currently available equipment, names only
    """
    equipment = EquipmentList()
    equipment.get_data("./data/equipment.json")
    return {'weapons': [w.name for w in equipment.weapons],
            'armors': [a.name for a in equipment.armors]}


if __name__ == '__main__':
    app.run(port=10001)
