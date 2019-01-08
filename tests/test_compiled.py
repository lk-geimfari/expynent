import re
from expynent import compiled
from expynent import patterns
from expynent.shortcuts import is_private


def assert_is_compiled(obj):
    assert isinstance(obj, type(re.compile('')))


def test_patterns_are_compiled():

    def walk(dictionary):
        for value in dictionary.values():
            if isinstance(value, dict):
                walk(value)
            else:
                yield value

    for pattern_name in dir(patterns):
        if is_private(pattern_name):
            continue

        compiled_variable = getattr(compiled, pattern_name)
        if isinstance(compiled_variable, dict):
            for value in walk(compiled_variable):
                assert_is_compiled(value)
        else:
            assert_is_compiled(compiled_variable)
