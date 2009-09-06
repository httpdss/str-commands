"""
Created on Aug 30, 2009

@author: kenny
"""
from base_commands import OnPathCommand

class UtilsCommands(OnPathCommand):
    """
    This class represents the coreutils commands from gnu
    """

    def mkdir(self, path = "", directories = [], *args):
        """Make directory command
        
        """
        str_cmd = []
        str_cmd.append(self.chdir(path))
        str_cmd = str_cmd + ['mkdir %s %s' %
                             (self.get_args(args), mkdir) 
                             for mkdir in directories]
        return self.execute(str_cmd)

    def cp(self):
        """Copy command"""
        pass
    
    def mv(self):
        """Move comand"""
        pass