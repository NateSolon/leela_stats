import chess.pgn
from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd


results_dict = {
    "1-0": 1,
    "0-1": 0,
    "1/2-1/2": 0.5,
}

def process_game(fn):
    pgn = open(fn)
    game = chess.pgn.read_game(pgn)
    length = len(list(game.mainline_moves()))
    if game.headers["Result"] != "*":
        result = results_dict[game.headers["Result"]]
    else:
        result = 1 if length % 2 == 1 else 0
    return length, result

def process_dir(path, outfile):
    path = Path(path)
    lengths, results = [], []
    i = 0
    for f in path.glob("*.pgn"):
        i += 1
        if i % 1000 == 0:
            print(i)
        if i == 10_000:
            break
        length, result = process_game(f)
        lengths.append(length)
        results.append(result)
    df = pd.DataFrame({
        "length": lengths,
        "result": results,
    })
    df.to_csv(outfile, index=False)