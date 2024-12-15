from datetime import datetime as dt


FMT = '%H:%M'


def time_difference(start, end):
    delta = dt.strptime(start, FMT) - dt.strptime(end, FMT)
    return abs(delta.total_seconds()) / 60


if __name__ == '__main__':
    res = time_difference("09:00", "10:00")
    print(f'{res} minutes')

