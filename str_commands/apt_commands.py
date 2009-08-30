import logging

APT_COMMAND = "apt-get -qy install %s"

class AptCommands(object):
    """
    This class represents a utility to execute apt commands in 
    a python environment.
    """

    def update(self):
        return 'apt-get update'

    def install(self,apps):
        """
        install packages using apt-get
        """
        return APT_COMMAND % " ".join(apps)

    def upgrade(self):
        """
        upgrade packages using apt-get
        """
        return 'apt-get upgrade'

    def dpkg_install(self, filename, location = "",delete = True):
        """
        represents the "dpkg -i <filename>" command
        it automatically removes the package after installation
        
        filename -- filename to install
        """
        if location:
            subprocess.call("wget %s" % location, shell=True)
        subprocess.call("dpkg -i %s" % filename, shell=True)
        if delete:
            subprocess.call("rm %s" % filename, shell=True)

    def fix_install(self):
        """
        command to fix the dependencies of packages while installing
        """
        return "apt-get -f install -y"
