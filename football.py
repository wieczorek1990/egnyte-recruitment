import requests


def fetch_data():
    """Download the results from the English Premier League for 2001/2."""
    return requests.get('http://codekata.com/data/04/football.dat').text


def minimum_goals_difference(data):
    """Return name of team with minimum goals difference."""
    minimum = None
    for index, line in enumerate(data.splitlines()):
        if index == 0:
            # skip header
            continue
        name = line[7:23].replace(' ', '')
        if name == '----------------':
            # skip divider
            continue
        if line == '':
            # skip empty line
            continue
        f = line[43:45].replace(' ', '')
        a = line[50:52].replace(' ', '')
        difference = abs(int(f) - int(a))
        if minimum is None:
            minimum = (name, difference)
        else:
            if difference < minimum[1]:
                minimum = (name, difference)
    return minimum[0]


if __name__ == '__main__':
    print(minimum_goals_difference(fetch_data()))
