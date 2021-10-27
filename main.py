import os
import platform
import configparser
from github import Github
from github import GithubException

def readLocalConfiguration():

    # https://docs.python.org/3/library/configparser.html
    config = configparser.ConfigParser()
    home = os.path.expanduser('~')
    configFile = home + '/.config/configit/{0}'.format('configit.ini')
    
    print('Reading configuration file \'{0}\''.format(configFile))
    config.read(configFile)
    
    print('Sections found: ', config.sections())
    
    profile = config['profile']['name']
    token = config['github']['token']
    repo = config['github']['repo']
    
    # https://pygithub.readthedocs.io/en/latest/index.html
    g = Github(token)
    u = g.get_user()
    
    print('Github user: ', u)
    
    print('Reading \'{0}\' profile...'.format(profile))
    
    if not profile in config:
        print('\'{0}\' profile section was not found in \'{1}\''.format(profile, configFile))
        # TODO: check remote repo exists, if not - create one
        # TODO: check profiles in existing remote repo
        # TODO: ask for download profiles, download it
        # TODO: update configuration file
    
    
    files = config[profile]
    
    for key in files:
        print(files.get(key))
        f = open(home + '/.config/configit/{0}'.format(files.get(key)))
        print(f.read())

readLocalConfiguration()


# TODO: push files to repository
# TODO: ask if user wants to download .list files from repository to configuration directory
 
