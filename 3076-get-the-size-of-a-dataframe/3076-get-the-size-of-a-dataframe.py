import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    rows,columns = players.shape
    result = [rows,columns]
    return result
    