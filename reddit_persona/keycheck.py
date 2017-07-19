from os import path, getcwd

f = 'indicoKey.txt'
base_dir = path.join(getcwd(), path.dirname(__file__))
keyPath = path.join(base_dir, f)


def get_key():
    with open(keyPath, 'r') as c:
        return c.read()


def test_key():
    with open(keyPath, 'r') as c:
        keycheck = c.read()
    try:
        import indicoio
        indicoio.config.api_key = keycheck
        indicoio.sentiment("I love writing code!")
        return True
    except Exception as e:
        print("Indico API key missing/invalid")
        print()
        print(
            'Redditor text can be collected with reddit_persona.go(USERNAME), but it will not be analyzed'
        )
        print()
        print('To enter your indico API key, use reddit_persona.new_key( )')
        print()
        return False


test_key()


def new_key(k=False):
    if k:
        with open(keyPath, 'w') as w:
            w.write(str(k))
        with open(keyPath, 'r') as t:
            test_read = t.read()
            if test_key() == True:
                print(
                    "Key validated and saved to disk. You will not need to re-enter again"
                )
                return
