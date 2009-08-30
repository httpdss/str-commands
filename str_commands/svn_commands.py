import subprocess, logging, os, sys

class SVNCommands(object):
    """
    This class represents common svn commands
    """

    def __init__(self, repository = ""):
        """
        Constructor.
        
        repository -- repository address
        """
        self._repository = repository

    def get_respository(self):
        return self._respository

    def set_repository(self, repo):
        self._repository = repo

    repository = property(get_repository, set_repository)

    def checkout(self, working_dir, repo = "" ):
        """
        SVN checkout command

        working_dir -- path to the working directory
        repo -- respository to use. if not set, it uses the one declared by the instance
        """
        subprocess.call("svn co %s %s" (self._getRepo(repo), working_dir), shell=True)

    def update(self, working_dir):
        """
        SVN update command
        
        working_dir -- path to the working directory
        """
        subprocess.call("cd %s; svn up" % working_dir, shell=True)

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

    def __init__(self):
        """
        Constructor.
        """
        Exception.__init__(self)

# vim: ai ts=4 sts=4 et sw=4
