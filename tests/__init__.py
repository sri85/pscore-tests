from os import makedirs
from os import path
from os import getcwd
import errno

from execution import set_variables

# use this import in a harmless way so PyCharm does not "optimise" this import
stop_pycharm_complaining = set_variables.current_environment is None


def create_folders(path_to_file):
    """Makes all the folders in a path if they don't exist.
    Imitates the `mkdir -p` function.

    Parameters
    ----------
    path_to_file : str
        The path to the file you want to create the folders for.
    """
    try:
        makedirs(path_to_file)
    except OSError as exc:
        if exc.errno == errno.EEXIST and path.isdir(path_to_file):
            pass
        else:
            raise


create_folders(path.join(getcwd(), 'screenshots'))
