"""
Created on Aug 30, 2009

@author: kenny
"""

from base_commands import OnPathCommand

APT_COMMAND = "apt-get -qy install %s"

class AptCommands(OnPathCommand):
    """
    This class represents a utility to execute apt commands in 
    a python environment.
    """
    def __init__(self):
        super(AptCommands, self).__init__()

    def update(self):
        return 'apt-get update'

    def install(self, apps):
        """
        install packages using apt-get
        """
        return APT_COMMAND % " ".join(apps)

    def upgrade(self):
        """
        upgrade packages using apt-get
        """
        return 'apt-get upgrade'

    def dpkg_install(self, filename, location = "",
                     delete = True, use_path = False):
        """
        represents the "dpkg -i <filename>" command
        it automatically removes the package after installation
        
        filename -- filename of .deb to install
        location -- download location of .deb
        delete -- delete .deb after installation
        use_path -- if true it will cd to the current path
        """
        str_cmd = []
        if use_path and self.path:
            str_cmd.append(self.chdir())
        if location:
            str_cmd.append("wget %s" % location)
        str_cmd.append("dpkg -i %s" % filename)
        if delete:
            str_cmd.append("rm %s" % filename)
        return self.execute(str_cmd)

    def fix_install(self):
        """
        command to fix the dependencies of packages while installing
        """
        return "apt-get -f install -y"