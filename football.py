import re
import requests


def fetch_data():
    """Download the results from the English Premier League for 2001/2."""
    return requests.get('http://codekata.com/data/04/football.dat').text


def should_omit_line(index, line):
    """Decide whether the line should be skipped."""
    if index == 0:
        # skip header
        return True
    elif line == ('   --------------------------'
                  '-----------------------------'):
        # skip divider
        return True
    elif line == '':
        # skip empty line
        return True
    else:
        return False


def generate_data(data):
    """Yield data fields."""
    for index, line in enumerate(data.splitlines()):
        if should_omit_line(index, line):
            continue
        try:
            team_name = re.sub(r' +', ' ', line).lstrip(' ').split(' ')[1]
        except IndexError:
            print('Could not parse team name.')
            exit(1)
        try:
            goals = re.findall(r'\d+  -  \d+', line)[0].split('  -  ')
            for_goals = goals[0]
            against_goals = goals[1]
            yield (team_name, for_goals, against_goals)
        except IndexError:
            print('Could not parse goals.')
            exit(1)


def minimum_goals_difference(data):
    """Return name of team with minimum goals difference."""
    minimum = None
    for team_name, for_goals, against_goals in generate_data(data):
        try:
            difference_goals = abs(int(for_goals) - int(against_goals))
        except ValueError:
            print('Could not parse goals.')
            exit(1)
        if minimum is None:
            minimum = (team_name, difference_goals)
        else:
            if difference_goals < minimum[1]:
                minimum = (team_name, difference_goals)
    return minimum[0]


if __name__ == '__main__':
    print(minimum_goals_difference(fetch_data()))
