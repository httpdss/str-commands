"""
Created on Aug 30, 2009

@author: kenny
"""
from base_commands import OnPathCommand

class SVNCommands(OnPathCommand):
    """
    This class represents common svn commands
    """

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

    def checkout(self, working_dir = "", repo = "", use_path = False):
        """
        SVN checkout command

        working_dir -- path to the working directory
        repo -- respository to use. if not set, it uses the one declared by the instance
        """
        str_cmd = []
        if use_path:
            str_cmd.append(self.chdir())
        str_cmd.append("svn co %s %s" % (self._getRepo(repo), working_dir))
        return self.execute(str_cmd) 

    def update(self, working_dir):
        """
        SVN update command
        
        working_dir -- path to the working directory
        """
        str_cmd = []
        str_cmd.append(self.chdir(working_dir))
        str_cmd.append("svn up")
        return self.execute(str_cmd)
        

    def _getRepo(self, repo = ""):
        if not (repo or self.repository):
            raise RepositoryIsMissing
        if repo:
            return repo
        return self.repository

class RepositoryIsMissing(Exception):
    """
    This class represents a custom exception raised when a repository is not set
    """
    pass