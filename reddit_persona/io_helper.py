from os import path, getcwd
import datetime

working_dir = path.join(getcwd(), path.dirname(__file__))
usr_path = path.join(working_dir, 'usr')

def read_raw(USERNAME):
        f =  USERNAME + '_raw.txt'
        memoize = path.join(usr_path, f)
        with open(memoize, 'r') as r_data:
            r_data = ''.join([line for line in r_data])
        return r_data

def out_path(USERNAME):
        f =  USERNAME + '.txt'
        memoize = path.join(usr_path, f)
        return memoize

def check_time(USERNAME,seconds_):

    # Prevent new API requests if result exists from within one minute
    memoize = out_path(USERNAME)
    try:
        ttime = path.getmtime(memoize)
    except Exception as e:
        return True
    
    mtime = datetime.datetime.fromtimestamp(ttime)
    ntime = datetime.datetime.now()

    dlta = ntime - mtime
    if abs(dlta.total_seconds()) > seconds_:
        return True

    else: return False