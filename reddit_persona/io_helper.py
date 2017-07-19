from os import path, getcwd
import datetime

p, f = path.split(path.abspath(__file__))
usr_path = path.join(p, 'cache')


def read_raw(USERNAME, target):
    f = USERNAME + '_raw.txt'
    memoize = path.join(usr_path, target, f)
    with open(memoize, 'r') as r_data:
        r_data = ''.join([line for line in r_data])
    return r_data


def out_path(USERNAME, target):
    f = USERNAME + '.txt'
    memoize = path.join(usr_path, target, f)
    return memoize


def check_time(USERNAME, target, seconds_):

    # Prevent new API requests if result exists from within one minute
    memoize = out_path(USERNAME, target)
    try:
        ttime = path.getmtime(memoize)
    except Exception as e:
        return True

    mtime = datetime.datetime.fromtimestamp(ttime)
    ntime = datetime.datetime.now()

    dlta = ntime - mtime
    if abs(dlta.total_seconds()) > seconds_:
        return True

    else:
        return False
