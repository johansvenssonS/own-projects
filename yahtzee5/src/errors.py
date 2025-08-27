"""Modul för Exepctions till unorderedlist"""


class Error(Exception):
    """Klass för egna exeptions"""


class MissingIndex(Error):
    """Fångar fall när den specifika index positionen saknas"""


class MissingValue(Error):
    """Fångar fall när positionen saknar det specifika värdet"""
