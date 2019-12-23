import cProfile
import io
import pstats


def profile(func):

    """A decorator that uses cProfile to profile a function"""

    def inner(*args, **kwargs):
        pr = cProfile.Profile()

        pr.enable()
        result = func(*args, **kwargs)
        pr.disable()

        s = io.StringIO()
        sort_by = 'cumulative'

        ps = pstats.Stats(pr, stream=s).sort_stats(sort_by)
        ps.print_stats()

        print(s.getvalue())
        return result

    return inner
