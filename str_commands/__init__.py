from str_commands import utils_commands, apache_commands, apt_commands, \
    svn_commands, git_commands


VERSION = (0, 1, 0, 'alfa', 1)

apache = apache_commands.ApacheCommands()
apt = apt_commands.AptCommands()
svn = svn_commands.SVNCommands()
git = git_commands.GITCommands()
utils = utils_commands.UtilsCommands()

link = utils.link

def get_version():
    """return version with a specific format"""
    version = '%s.%s' % (VERSION[0], VERSION[1])
    if VERSION[2]:
        version = '%s.%s' % (version, VERSION[2])
    if VERSION[3] != "final":
        version = '%s%s%s' % (version, VERSION[3], VERSION[4])
    return version

__version__ = get_version()