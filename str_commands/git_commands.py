"""
Created on Aug 30, 2009

@author: kenny
"""
from base_commands import RepositoryCommands

class GITCommands(RepositoryCommands):
    """
    This class represents common git commands
    """

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