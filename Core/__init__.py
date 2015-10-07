__author__ = 'aminmahpour'
import os


class File:
    def __new__(cls, filename):
        """
        This is a class for files to be processed
        :param filename: This param identifies file and directory name.
        :return: a structured filename that includes correct and OS specific filename.
        """
        return os.path.abspath(filename)


class Configs:
    def __init__(self):
        pass
