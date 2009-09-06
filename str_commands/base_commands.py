"""
Created on Aug 30, 2009

@author: kenny
"""

class BaseCommand(object):
    """
        
    """

    def __init__(self):
        '''
        Constructor for base command class
        '''
    def execute(self, str_cmd):
        """
            join all string commands received and output a ready
            to execute command
        """
        return "; ".join(str_cmd)

class OnPathCommand(BaseCommand):
    """
        
    """
    def __init__(self):
        self._path = None

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, value):
        self._path = value

    def clear_path(self):
        self._path = None

    def chdir(self, dir = ""):
        """Change directory
        
        Command:
            cd %s
            
        dir -- change to this directory or the one set on path
        """
        return 'cd %s' % (dir or self._path)

class RepositoryIsMissing(Exception):
    """This class represents a custom exception raised when a repository 
    is not set
    """
    pass