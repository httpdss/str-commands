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

class RepositoryCommands(OnPathCommand):
    
    def __init__(self, repository = ""):
        """
        Constructor.
        
        repository -- repository address
        """
        self._repository = repository

    @property
    def repository(self):
        return self._repository

    @repository.setter
    def repository(self, repo):
        self._repository = repo
    
    def _get_repo(self, repo = ""):
        if not (repo or self.repository):
            raise RepositoryIsMissing
        if repo:
            return repo
        return self.repository

class RepositoryIsMissing(Exception):
    """This class represents a custom exception raised when a repository 
    is not set
    """
    pass