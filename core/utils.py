import re


def extract_data_from_game_record_file(filename):
    """helper function to extract data from the game record file"""
    game_record_regex = r'(1.)(\s).+((0-1)|(1-0)|(1/2-1/2))'
    black_player_nickname_regex = r'(Black)(\s).+(")'
    white_player_nickname_regex = r'(White)(\s).+(")'
    result_regex = r'(Result)(\s).+((0-1)|(1-0)|(1/2-1/2))'

    with open(filename, 'r') as f:
        f_content = f.read()
        game_record_string = re.search(game_record_regex, f_content, re.MULTILINE | re.DOTALL)
        game_record_list = game_record_string.group().split('. ')
        black_player_nickname_str = re.search(black_player_nickname_regex, f_content)
        white_player_nickname_str = re.search(white_player_nickname_regex, f_content)
        result_str = re.search(result_regex, f_content)
        print(print(game_record_list))
        return 'hello'


print(extract_data_from_game_record_file('record_1'))

