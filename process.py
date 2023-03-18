import chess.pgn
from pathlib import Path
import pandas as pd

from chart import plot_first_moves, plot_length, plot_results


results_dict = {
    "1-0": 1,
    "0-1": 0,
    "1/2-1/2": 0.5,
}

def process_game(f):
    pgn = open(f)
    game = chess.pgn.read_game(pgn)
    moves = list(game.mainline_moves())
    length = len(moves)
    first_move = chess.Board().san(moves[0])
    if game.headers["Result"] != "*":
        result = results_dict[game.headers["Result"]]
    else:
        result = 1 if length % 2 == 1 else 0
    return length, result, first_move

def get_data(path, outfile):
    path = Path(path)
    lengths, results, first_moves = [], [], []
    i = 0
    for f in path.glob("*.pgn"):
        i += 1
        if i % 1000 == 0:
            print(i)
        length, result, first_move = process_game(f)
        lengths.append(length)
        results.append(result)
        first_moves.append(first_move)
    df = pd.DataFrame({
        "length": lengths,
        "result": results,
        "first_move": first_moves,
    })
    df.to_csv(outfile, index=False)

def process_dir(pgn_path, op_dir):
    name = Path(pgn_path).name
    p = op_dir/name
    p.mkdir(exist_ok=True)
    get_data(pgn_path, p/"data.csv")
    df = pd.read_csv(p/"data.csv")
    plot_length(df, p/"length.png")
    plot_results(df, p/"results.png")
    plot_first_moves(df, p/"first_moves.png")