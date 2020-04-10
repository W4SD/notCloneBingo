from flask import Flask, render_template, request, redirect, url_for
from generator import BingoCard
import json

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def enter_site():
    BingoCards = []
    if request.method == "POST":

        data = json.loads(request.data)
        print(data)
        for x in range(data):
            new_card = BingoCard()
            BingoCards.append(new_card)

        return render_template("bingoCard.html", BingoCards=BingoCards)

    else:
        BingoCards.append(BingoCard())

    print(f'KORTIT: {len(BingoCards)}')
    return render_template("bingo.html", BingoCards=BingoCards)


if __name__ == '__main__':
    app.run()
