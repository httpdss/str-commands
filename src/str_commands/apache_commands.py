"""
Created on Aug 30, 2009

@author: kenny
"""
from base_commands import BaseCommand

class ApacheCommands(BaseCommand):
    """
    This class represents apache administration commands
    """

    def __init__(self, version = 2):
        """
        Constructor.

        version -- apache version to use
        """
        assert version
        self._version = version

    def restart(self):
        """Restart the apache server
        
        Command: 
            /etc/init.d/apache2 restart
            
        """
        return '/etc/init.d/apache2 restart'

    def enable_mods(self, mods):
        """Enable a list of apache modules
        
        Command: 
            /usr/sbin/a2enmod %s
        
        mods -- list of modules
        
        """
        return self.execute(['/usr/sbin/a2enmod %s' % mod for mod in mods])

    def disable_mods(self, mods):
        """Disable a list of apache modules
        
        Command: 
            /usr/sbin/a2dismod %s
        
        mods -- list of modules
        
        """
        return self.execute(['/usr/sbin/a2dismod %s' % mod for mod in mods])

    def enable_sites(self, sites):
        """Enable a list of sites
        
        Command: 
            /usr/sbin/a2ensite %s
        
        sites -- list of sites
        
        """
        return self.execute(['/usr/sbin/a2ensite %s' % site for site in sites])

    def disable_sites(self, sites):
        """Disable a list of sites
        
        Command: 
            /usr/sbin/a2ensite %s
        
        sites -- list of sites
        
        """
        return self.execute(['/usr/sbin/a2dissite %s' % site for site in sites])