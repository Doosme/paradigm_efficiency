from util_directories import DATA_LANGLIST_FOLDER

from util import LANG_TYPES, LANG_TYPES_PRONCogSci

def _read_in_languages_from_file(filename):
    with open(filename) as f:
        langs = f.read().strip().split("\n")
    return langs
LANGUAGE_LISTS = {lang_type: _read_in_languages_from_file(DATA_LANGLIST_FOLDER + "langlist_"+lang_type) for lang_type in LANG_TYPES+LANG_TYPES_PRONCogSci}
