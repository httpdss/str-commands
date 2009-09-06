"""
Created on Aug 30, 2009

@author: kenny
"""
from base_commands import OnPathCommand, RepositoryIsMissing

class GITCommands(OnPathCommand):
    """
    This class represents common git commands
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

    def clone(self, path = "", repo = "", name = ""):
        """GIT clone command

        name -- folder name of clone
        repo -- respository to use. if not set, it uses the one declared 
        by the instance
        name -- folder name of clone
        
        
        """
        str_cmd = []
        str_cmd.append(self.chdir(path))
        str_cmd.append("git clone %s %s" % (self._get_repo(repo), name))
        return self.execute(str_cmd)

    def pull(self, path = ""):
        """GIT pull command
        
        path -- path to repository clone. if not set, uses self.path
        
        """

        return self.execute([self.chdir(path), "git pull"])


    def _get_repo(self, repo = ""):
        if not (repo or self.repository):
            raise RepositoryIsMissing
        if repo:
            return repo
        return self.repository