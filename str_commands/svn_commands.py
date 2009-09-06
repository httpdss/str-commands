"""
Created on Aug 30, 2009

@author: kenny
"""
from base_commands import RepositoryCommands

class SVNCommands(RepositoryCommands):
    """
    This class represents common svn commands
    """

    def checkout(self, working_dir = "", repo = "", use_path = False):
        """SVN checkout command

        working_dir -- path to the working directory
        repo -- respository to use. if not set, it uses the one declared 
        by the instance
        
        """
        str_cmd = []
        if use_path:
            str_cmd.append(self.chdir())
        str_cmd.append("svn co %s %s" % (self._get_repo(repo), working_dir))
        return self.execute(str_cmd)

    def update(self, working_dir):
        """SVN update command
        
        working_dir -- path to the working directory
        
        """
        return self.execute([self.chdir(working_dir), "svn up"])