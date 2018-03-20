import requests


def fetch_data():
    """Fetch daily weather data for Morristown, NJ for June 2002."""
    return requests.get('http://codekata.com/data/04/weather.dat').text


def minimum_temperature_spread(data):
    """Return day number with minimum temperature spread."""
    minimum = None
    for index, line in enumerate(data.splitlines()):
        if index in (0, 1):
            # skip header
            continue
        dy = line[:4].replace(' ', '')
        if dy == 'mo':
            # skip summary
            continue
        if line == '':
            # skip empty line after summary
            continue
        max_t = line[4:8].replace(' ', '').replace('*', '')
        min_t = line[8:14].replace(' ', '').replace('*', '')

        dt = int(max_t) - int(min_t)
        if minimum is None:
            minimum = (dy, dt)
        else:
            if dt < minimum[1]:
                minimum = (dy, dt)
    return minimum[0]


if __name__ == '__main__':
    print(minimum_temperature_spread(fetch_data()))
