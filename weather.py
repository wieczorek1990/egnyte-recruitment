import re
import requests


def fetch_data():
    """Fetch daily weather data for Morristown, NJ for June 2002."""
    return requests.get('http://codekata.com/data/04/weather.dat').text


def should_omit_line(index, line, dy):
    """Decide whether the line should be skipped."""
    if index in (0, 1):
        # skip header
        return True
    elif dy == 'mo':
        # skip summary
        return True
    elif line == '':
        # skip empty line after summary
        return True
    else:
        return False


def generate_data(data):
    """Yield data fields."""
    for index, line in enumerate(data.splitlines()):
        line = re.sub(' +', ' ', line).lstrip(' ')
        fields = line.split(' ')
        day_no = fields[0]
        if should_omit_line(index, line, day_no):
            continue
        max_temperature = fields[1].replace('*', '')
        min_temperature = fields[2].replace('*', '')
        yield (day_no, max_temperature, min_temperature)


def minimum_temperature_spread(data):
    """Return day number with minimum temperature spread."""
    minimum = None
    for day_no, max_temperature, min_temperature in generate_data(data):
        try:
            temperature_difference = (int(max_temperature) -
                                      int(min_temperature))
        except ValueError:
            print('Could not parse temperatures.')
            exit(1)
        if minimum is None:
            minimum = (day_no, temperature_difference)
        else:
            if temperature_difference < minimum[1]:
                minimum = (day_no, temperature_difference)
    return minimum[0]


if __name__ == '__main__':
    print(minimum_temperature_spread(fetch_data()))
