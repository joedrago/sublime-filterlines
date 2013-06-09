import re

import sublime
import sublime_plugin


def match_line(needle, haystack, search_type, case_sensitive, invert_search = False):
    if invert_search:
        return not search_line(needle, haystack, search_type, case_sensitive)
    else:
        return search_line(needle, haystack, search_type, case_sensitive)

def search_line(needle, haystack, search_type, case_sensitive):
    """return true if needle is found in haystack"""
    if search_type == "regex":
        if not case_sensitive:
            return re.search(needle, haystack, re.IGNORECASE)
        else:
            return re.search(needle, haystack)
    else:
        if not case_sensitive:
            needle = needle.upper()
            haystack = haystack.upper()

        return (needle in haystack)


try:
    # Python 3
    from .filter_to_lines_command import *
    from .fold_to_lines_command import *

except (ValueError):
    # Python 2
    from filter_to_lines_command import *
    from fold_to_lines_command import *
