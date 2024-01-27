from sgfmill import sgf

# Given a file name, create an Sgf_game object and return the root
def getRoot(filename):
    with open(filename, "rb") as f:
        game = sgf.Sgf_game.from_bytes(f.read())
        return game.get_root()

# Given the root, return the string name of the game
def whichGame(root):
    games_dict = {
        1: "Go",
        2: "Othello",
        3: "chess",
        4: "Gomoku+Renju",
        5: "Nine Men's Morris",
        6: "Backgammon",
        7: "Chinese chess",
        8: "Shogi",
        9: "Lines of Action",
        10: "Ataxx",
        11: "Hex",
        12: "Jungle",
        13: "Neutron",
        14: "Philosopher's Football",
        15: "Quadrature",
        16: "Trax",
        17: "Tantrix",
        18: "Amazons",
        19: "Octi",
        20: "Gess",
        21: "Twixt",
        22: "Zertz",
        23: "Plateau",
        24: "Yinsh",
        25: "Punct",
        26: "Gobblet",
        27: "hive",
        28: "Exxit",
        29: "Hnefatal",
        30: "Kuba",
        31: "Tripples",
        32: "Chase",
        33: "Tumbling Down",
        34: "Sahara",
        35: "Byte",
        36: "Focus",
        37: "Dvonn",
        38: "Tamsk",
        39: "Gipf",
        40: "Kropki"
    }
    return games_dict[root.get("GM")]

# Given the root, return True if the game is Go
def isGo(root):
    try:
        game_key = root.get("GM")
    except:
        return False
    return game_key == 1

# Given the root, return True if there is more than one move
def hasMultipleMoves(root):
    if len(root) == 0:
        # No moves were made
        return False
    if len(root[0]) == 0:
        # Only one move was made
        return False
    return True

def main():
    # Testing
    filename = "./test-sgfs/byoyomi-HA4PO.sgf"
    root = getRoot(filename)
    print(whichGame(root))
    print(isGo(root))
    print(hasMultipleMoves(root))

if __name__ == "__main__":
    main()