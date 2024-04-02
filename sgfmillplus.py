from sgfmill import sgf

# Given a file name, create an Sgf_game object and return the root
def get_root(filename):
    with open(filename, "rb") as f:
        game = sgf.Sgf_game.from_bytes(f.read())
        return game.get_root()

# Given the root, return the string name of the game
def which_game(root):
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
    try:
        game_key = root.get("GM")
    except:
        raise Exception("Root has no GM key.")
    return games_dict[game_key]

# Given the root, return True if the game is Go
def is_go(root):
    try:
        game_key = root.get("GM")
    except:
        raise Exception("Root has no GM key.")
    return game_key == 1

# Given the root, return True if there is more than one move
def has_multiple_moves(root):
    return len(root) != 0 and len(root[0]) != 0

# Given the root, return a dictionary of player names
def get_player_names(root):
    res = {
        "b": None,
        "w": None
    }
    if root.has_property("PB"):
        res["b"] = root.get("PB")
    if root.has_property("PW"):
        res["w"] = root.get("PW")
    return res

# Given the root, return a dictionary of player ranks
def get_player_ranks(root):
    res = {
        "b": None,
        "w": None
    }
    if root.has_property("BR"):
        res["b"] = root.get("BR")
    if root.has_property("WR"):
        res["w"] = root.get("WR")
    return res

# Given the root, return the time system
def get_time_system(root):
    if root.has_property("TM"):
        return root.get("TM")
    return None

# Given the root, return the overtime system
def get_overtime_system(root):
    if root.has_property("OT"):
        return root.get("OT")
    return None

# Given the root, return the game result
def get_game_result(root):
    if root.has_property("RE"):
        return root.get("RE")
    return None

# Given a list of substrings, return whether each player name contains
# at least one of the substrings (not case-sensitive)
def playernames_contain_substrings(root, substrings):
    res = {
        "b": None,
        "w": None
    }
    if root.has_property("PB"):
        pb = root.get("PB").lower()
        res["b"] = any((s in pb) for s in substrings)
    if root.has_property("PW"):
        pw = root.get("PW").lower()
        res["w"] = any((s in pw) for s in substrings)

    return res