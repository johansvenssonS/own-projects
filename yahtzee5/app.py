
#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Minimal Flask application, including useful error handlers.
"""
## source .venv/bin/activate
#deactivate
#import logging (felsök i terminalen, få utskrifter där)
    #logging.debug("yahtzee routen")
import traceback
import os
import re
from flask import Flask, render_template, request, redirect, url_for, session, flash
from src.hand import Hand
from src.scoreboard import Scoreboard
from src.leaderboard import Leaderboard
from src.sort import recursive_insertion
from src.queue import Queue 
from src.players import Player
app = Flask(__name__)
app.secret_key = re.sub(r"[^a-z\d]", "", os.path.realpath(__file__))

save_file = "scores.txt"
#logging.basicConfig(level=logging.DEBUG)

@app.route("/")
def main():
    """main route"""
    
    return render_template("index.html")

@app.route("/settings", methods=["POST"])
def settings():
    """multiplayer route"""
    amount_options = [1, 2, 3, 4]
    stege = [1, 2, 3, 4, 5]
    hand = Hand(stege)
    scoreboard = Scoreboard()

    return render_template("settings.html", amount_options=amount_options, hand=hand, scoreboard=scoreboard,)
@app.route("/init", methods=["POST"])
def init():
    """init route för att starta spelet"""
    amount_players = int(request.form.get("players"))
    game_que = Queue()
    for i in range (1, amount_players+1):
        hand = Hand()
        scoreboard = Scoreboard()
        hand_data = hand.to_list()
        scoreboard_data = scoreboard.rules
        player = Player(i, hand_data, scoreboard_data)
        game_que.enqueue(player)
        

    session["game_que"] = game_que.to_list()
    active_player = game_que.peek()
    session["active_player"] = active_player.to_dict()
    session["reroll_count"] = 0
    return redirect(url_for('yahtzee'))

@app.route("/yahtzee", methods=["GET"])
def yahtzee():

    """ sTart route för yahtzee spelet """
    game_que = Queue.from_list(session["game_que"])
    active_player = game_que.peek()
    hand = Hand(active_player.hand)
    scoreboard = Scoreboard.from_dict(active_player.scoreboard)
    return render_template("yahtzee.html", hand=hand, scoreboard=scoreboard,
    reroll_count=session["reroll_count"], player_id=active_player.player_id)

@app.route("/reroll", methods = ["POST"])##tydligen är indexes 1baserade i jinja
def reroll():
    """ reroll route som slår om tärningar(indexes)"""
    game_que = Queue.from_list(session["game_que"])
    active_player = game_que.peek()
    hand = Hand(active_player.hand)
    # print(hand)
    if session["reroll_count"] <2:
        reroll_dice = request.form.getlist("reroll")
        reroll_indexes = []
        for index in reroll_dice:
            reroll_indexes.append(int(index)-1)#loop.index0 eller -1
        hand.roll(reroll_indexes)
        # print(hand)
        active_player.hand = hand.to_list()
        session["active_player"] = active_player.to_dict()
        session["reroll_count"] += 1
        session["game_que"] = game_que.to_list()
    return redirect(url_for('yahtzee'))

@app.route("/choice", methods = ["POST"])
def choice():
    """choice route som sätter poäng på vald kategori"""
    game_que = Queue.from_list(session["game_que"])
    active_player = game_que.dequeue()
    hand = Hand(active_player.hand)
    scoreboard = Scoreboard.from_dict(active_player.scoreboard)
    rule_name = request.form.get("rule")
    try:
        scoreboard.add_points(rule_name, hand)
        session["reroll_count"] = 0
        hand.roll()
        active_player.hand = hand.to_list()
        active_player.scoreboard = scoreboard.rules
        session["active_player"] = active_player.to_dict()
    except ValueError:
        flash("Kategorin har redan poängsatts","danger")#flash class
        return redirect(url_for('yahtzee'))
    game_que.enqueue(active_player)
    session["game_que"] = game_que.to_list()
    active_player = game_que.peek()
    session["active_player"] = active_player.to_dict()

    game_end = all(Scoreboard.from_dict(Player.from_dict(player).scoreboard).finished() for player in session["game_que"])
    if game_end:
        flash(f"Spelet är klart", "success")
        current_highest = 0
        winning_player = None
        for player in game_que._items:
            player_scoreboard = Scoreboard.from_dict(player.scoreboard)
            player_score = player_scoreboard.get_total_points()
            if player_score > current_highest:
                current_highest = player_score
                winning_player = player
        session["scoreboard"] = winning_player.scoreboard
        return redirect(url_for('user_input'))
    return redirect(url_for('yahtzee'))

@app.route("/user_input", methods = ["POST"])
def user_input():
    """user-input som ber hanterar spara poäng med namn"""
    name = request.form.get("name")
    scoreboard = Scoreboard.from_dict(session["scoreboard"])
    score = scoreboard.get_total_points()
    leaderboard = Leaderboard.load(save_file)
    leaderboard.add_entry(name, score)
    leaderboard.save(save_file)

    return redirect(url_for("show_leaderboard"))

@app.route("/remove", methods=["POST"])
def remove_entry():
    """route som hanterar fall där man vill ta bort användare."""
    index_remove = int(request.form.get("index"))
    leaderboard = Leaderboard.load(save_file)
    leaderboard.remove_entry(index_remove)
    leaderboard.save(save_file)

    flash("Ditt resultat har tagits bort!", "success")
    return redirect(url_for("show_leaderboard"))

@app.route("/leaderboard", methods = ["GET"])
def show_leaderboard():
    """route som laddar och renderar leaderboard"""
    leaderboard = Leaderboard.load(save_file)
    leaderboard.sort()
    return render_template("leaderboard.html", leaderboard=leaderboard)

@app.route("/about")
def about():
    """ About route """
    my_name = "Johan Svensson"
    my_akronym = "josg24"

    return render_template("about.html", name=my_name, akronym=my_akronym)

@app.route("/reset")
def reset():
    """ Route för att resetta spelet, cleara session """
    _ = [session.pop(key) for key in list(session.keys())]
    session.clear()
    return redirect(url_for("main"))

@app.errorhandler(404)
def page_not_found(e):
    """
    Handler for page not found 404
    """
    #pylint: disable=unused-argument
    return "Flask 404 here, but not the page you requested."


@app.errorhandler(500)
def internal_server_error(e):
    """
    Handler for internal server error 500
    """
    #pylint: disable=unused-argument
    return "<p>Flask 500<pre>" + traceback.format_exc()


if __name__ == "__main__":
    #app.run(debug=True) #debug=True använd bara vid utveckling.
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
