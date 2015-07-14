import sys
import getpass

from distutils.util import strtobool


def yes_no(question, prompt='%s [Y/n]: '):
    """Ask a yes/no question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    The "answer" return value respects distutils.util.strtobool
    https://docs.python.org/3.5/distutils/apiref.html?highlight=distutils.util#distutils.util.strtobool
    :param prompt: Prompt string
    """

    while True:
        choice = get_input(prompt % question).lower()

        try:
            return strtobool(choice)
        except ValueError:
            sys.stdout.write('Please respond with \'yes\' or \'no\''
                             '(or \'y\' or \'n\').\n')


def get_user_data(password=None):
    """
    Asks for username and password
    :param password:
    :return:
    """
    username = None

    while not username:
        username = get_input('Username: ').lower()

    while not password:
        password = get_pass().lower()

    return username, password


def get_input(label):
    """ Wrapping __builtin__.raw_input to make it testable
    :return: input data
    """
    sys.stdout.write(label)

    return raw_input()


def get_pass():
    """ Wrapping getpass.getpass to make it testable
    :return: input password data
    """
    return getpass.getpass()


def create_user(db, user_model):
    """ Used to create initial user when `createdb` command called
    :param db: SQLAlchemy instance
    :param user_model: appname.models.User model
    """
    if yes_no(question='Create user'):
        user_exists = True
        password = None

        while user_exists:
            username, password = get_user_data(password=password)

            if user_model.query.filter_by(username=username).count():
                sys.stdout.write('User with such username already exists...\n')
                continue

            user_exists = False
            db.session.add(user_model(username=username, password=password))
            db.session.commit()

            sys.stdout.write('User created...\n')
