# Write a solution to calculate and display the number of rows and columns of players.
# Return the result as an array: [number of rows, number of columns]

import polars as pl

def getDataframeSize(players: pl.DataFrame) -> List[int]:
    return [players.height, players.width]
