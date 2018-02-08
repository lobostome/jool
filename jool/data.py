# -*- coding: utf-8 -*-

import pandas

class Frame(object):
    def __init__(self):
        self.data = pandas.DataFrame(columns=['commit_id', 'commit_message', 'commit_author'])

    def add_column(self, name, values):
        self.data[name] = values

    @property
    def number_of_rows(self):
        return self.data.shape[0]

    @property
    def number_of_columns(self):
        return self.data.shape[1]