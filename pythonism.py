from functools import wraps

def join_words_dec(func):
    @wraps(func)
    def count_twenty(*args, **kwargs):
        val = func(*args, **kwargs)
        return f''