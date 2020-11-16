# -*- coding: UTF-8 -*-
# Copyright (C) 2018 Jean Bizot <jean@styckr.io>
""" Main lib for happymonday Project
"""

from os.path import split
import pandas as pd
import datetime
import webbrowser

pd.set_option('display.width', 200)


def try_me():
    webbrowser.open("https://www.youtube.com/watch?v=mrZRURcb1cM")


if __name__ == '__main__':
    # For introspections purpose to quickly get this functions on ipython
    import happymonday
    try_me()

