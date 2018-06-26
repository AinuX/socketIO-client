from six import indexbytes


try:
    from logging import NullHandler
except ImportError:  # Python 2.6
    from logging import Handler

    class NullHandler(Handler):

        def emit(self, record):
            pass
finally:
    from logging import getLogger


try:
    memoryview = memoryview
except NameError:
    memoryview = buffer  # noqa


def get_int(*args):
    try:
        return int(get_character(*args))
    except ValueError:
        return ord(get_character(*args))


def get_byte(x, index):
    return indexbytes(x, index)


def get_log(name):
    log = getLogger(name)
    log.addHandler(NullHandler())
    return log


def get_character(x, index):
    return chr(get_byte(x, index))


def decode_string(x):
    return x.decode('utf-8')


def encode_string(x):
    return x.encode('utf-8')
