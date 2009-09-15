"""
Created on Aug 30, 2009

@author: kenny
"""
from base_commands import OnPathCommand

class UtilsCommands(OnPathCommand):
    """
    This class represents the coreutils commands from gnu
    """

    def mkdir(self, path = "", directories = None, *args):
        """Make directory command
        
        """
        if directories:
            str_cmd = [self.chdir(path)] + ['mkdir %s %s' %
                                            (self.get_args(args), mkdir)
                                            for mkdir in directories]
        return self.execute(str_cmd)

    def copy(self, path = "", *args):
        """Copy `command"""
        return self.execute([self.chdir(path), 'cp %s' % self.get_args(args)])


    def move(self, path = "", *args):
        """Move comand"""
        return self.execute([self.chdir(path), 'mv %s' % self.get_args(args)])

    def link(self, path = "", symlink = True, *args):
        """make link of files and folders"""
        str_cmd = []
        
        sym = symlink and '-s' or ''
        if path:
            str_cmd.append(self.chdir(path))
        
        str_cmd.append('ln %s %s' % (sym, self.get_args(args)))
        return self.execute(str_cmd)  
