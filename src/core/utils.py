import re
from datetime import datetime
from collections import defaultdict
import requests


def extract_data(record_content):
    """Function to extract data from game record content"""

    # regex expressions to match content in game record
    game_record_regex = r"(1.)(\s).+([a-z0-9]( ))"
    black_player_nickname_regex = r"(Black)(\s).+([a-zA-Z])"
    white_player_nickname_regex = r"(White)(\s).+([a-zA-Z])"
    result_regex = r"(Result)(\s).+((0-1)|(1-0)|(1/2-1/2))"
    date_regex = r"(Date)(\s).+([0-9])"
    time_regex = r"(Time)(\s).+([0-9])"

    game_record_string = re.search(
        game_record_regex, record_content, re.MULTILINE | re.DOTALL
    ).group()
    black_player_nickname_str = re.search(
        black_player_nickname_regex, record_content
    ).group()
    white_player_nickname_str = re.search(
        white_player_nickname_regex, record_content
    ).group()
    date_str = re.search(date_regex, record_content).group()
    time_str = re.search(time_regex, record_content).group()
    result_str = re.search(result_regex, record_content).group()

    payload = defaultdict(list)
    game_record_list = make_game_record_list(game_record_string)
    swap_and_color_data = get_data_about_color_swap(game_record_list)

    # Adding keys and values to the dictionary
    payload["game_date"] = get_date_data_from_str(time_str, date_str)
    payload["game_record"] = get_game_record_from_list(game_record_list)
    payload["swap"] = swap_and_color_data[0]
    payload["swap_2"] = swap_and_color_data[1]
    payload["color_change"] = swap_and_color_data[2]

    for _ in get_data_from_str_generator(
        black_player_nickname_str, white_player_nickname_str, result_str
    ):
        if _[0] == "result" and _[1] == "1-0":
            payload[_[0]] = "black"
        elif _[0] == "result" and _[1] == "0-1":
            payload[_[0]] = "white"
        elif _[0] == "result" and _[1] == "1/2-1/2":
            payload[_[0]] = "draw"
        else:
            payload[_[0]] = _[1]
        make_game_record_list(game_record_string)

    return payload


def extract_data_from_game_record_file(filename=None, url=None):
    """
    helper function to extract data from the game record file
    function should return dictionary with values:
    white_player, black_player, date_time, result and game_record
    """
    if filename is not None and url is not None:
        raise ValueError("You can use only one way to create record at the time")
    elif filename is not None:
        with open(filename, "r") as f:
            f_content = f.read()
            print(f_content)
            return extract_data(f_content)
    elif url is not None:
        res = requests.get(url)
        print(res.text)
        if len(res.text) == 0:
            raise ValueError("no content")
        return extract_data(res.text)


def get_date_data_from_str(time_str, date_str):
    """
    Function which will extract datetime data from the string and will
    be used in the 'extract_data_from_game_record_file' function to avoid
    repeating the code
    function should return the datetime value
    """
    time_list = time_str.split(' "')
    date_list = date_str.split(' "')
    date_time_list = date_list[1] + " " + time_list[1]
    converted_time = datetime.strptime(date_time_list, "%Y.%m.%d %H:%M:%S")
    return converted_time


def get_data_from_str_generator(*data_list_params):
    """
    Function which will extract data(both players names and result)
    from the string and will
    be used in the 'extract_data_from_game_record_file' function to avoid
    repeating the code
    function should return generator
    """
    return (data_str.lower().split(' "') for data_str in data_list_params)


def make_game_record_list(game_record_str):
    """Function making game record list from the string"""

    # removing \n and \r whitespaces from game record
    game_record_list = " ".join(
        " ".join(game_record_str.split("\n")).split("\r")
    ).split(" ")
    # removing empty strings from the list
    game_record_list = [_ for _ in game_record_list if _ != ""]

    # removing . which was attached to numbers
    for i, v in enumerate(game_record_list):
        if "." in v:
            v = v.rstrip(".")
            game_record_list[i] = int(v)

    return game_record_list


def get_game_record_from_list(game_record_list):
    """
    Function extracting game record from a list to make it
    a list o tuples with a two values, number of move and coordinate
    """

    # Removing all statements from the list which aren't moves coordinates
    game_record_list_with_only_moves = []
    counter = 1
    for i, v in enumerate(game_record_list):
        if i == 0 or i % 3 == 0:
            pass
        elif v == "white" or v == "black" or v == "--":
            pass
        else:
            game_record_list_with_only_moves.append(v)
            counter += 1
    return game_record_list_with_only_moves


def get_data_about_color_swap(game_record_list):
    """
    Function determining whether during the game swap or swap2 was used
    and if players changed their original color of the stones
    """
    swap = False
    swap_2 = False
    color_change = False
    if "white" in game_record_list or "black" in game_record_list:
        swap = True
    if game_record_list[5] == "black":
        color_change = True
    elif game_record_list[10] == "white" or game_record_list[10] == "black":
        swap_2 = True
        if game_record_list[10] == "white":
            color_change = True
    return [swap, swap_2, color_change]


def check_domain(url):
    """Function checking domain from the given url"""
    domain_regex = r"((https)|(http))(://)([^/]+)"
    return re.search(domain_regex, url).group()
