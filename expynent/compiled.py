"""
Compiled versions of constants found in expynent.patterns
"""
import re

import expynent.patterns


def compile_patterns_in_dictionary(dictionary):
    """
    Replace all strings in dictionary with compiled version of themselves and return dictionary.
    """

    for key, value in dictionary.items():
        if isinstance(value, str):
            dictionary[key] = re.compile(value)
        elif isinstance(value, dict):
            compile_patterns_in_dictionary(value)
    return dictionary


# Handle special cases i.e. patterns that must be compiled with specific flags
IP_V6 = re.compile(expynent.patterns.IP_V6, re.VERBOSE | re.IGNORECASE | re.DOTALL)
URL = re.compile(expynent.patterns.URL, re.IGNORECASE)

# get pattern constants from expynent.patterns
# filter out patterns that begin with underscores and those that are already compiled
PATTERNS = tuple((pattern, getattr(expynent.patterns, pattern)) for pattern in dir(expynent.patterns)
                 if not pattern.startswith('_') and pattern not in ('IP_V6', 'URL'))

# Programmatically compile regex patterns and put them in the global scope
__g = globals()
for name, regex_variable in PATTERNS:
    if isinstance(regex_variable, str):
        # The regex variable is a string, compile it and put it in the global scope
        __g[name] = re.compile(regex_variable)
    elif isinstance(regex_variable, dict):
        # The regex variable is a dictionary, convert all regex strings in the dictionary
        # to their compiled versions and put the variable in the global scope
        __g[name] = compile_patterns_in_dictionary(regex_variable)
