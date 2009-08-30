import logging

class ApacheCommands(object):
    """
    This class represents apache administration commands

    TODO version integration (apache, apache2)
    """

    def __init__(self, version = 2):
        """
        Constructor.

        version -- apache version to use
        """
        assert version
        self._version = version

    def restart(self):
        logging.debug("Restarting apache...")
        return '/etc/init.d/apache2 restart'

    def enable_mods(mods):
        mod_str = "; ".join(['/usr/sbin/a2enmod %s' % mod for mod in mods])
        return mod_str

    def disable_mods(mods):
        mod_str = "; ".join(['/usr/sbin/a2dismod %s' % mod for mod in mods])
        logging.debug("Executing: %s" % mod_str)
        return mod_str

    def enable_sites(sites):
        site_str = "; ".join(['/usr/sbin/a2ensite %s' % site for site in sites])
        logging.debug("Executing: %s" % site_str)
        return site_str
