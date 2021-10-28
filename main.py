import os
from pathlib import Path
import platform
import configparser
from github import Github
from github import GithubException

home = os.path.expanduser('~')
configFilePath = home + '/.config/configit/'
configFileName = 'configit.ini'
configFile = configFilePath + configFileName

def existLocalConfiguration(configFile):
    return Path(configFile).is_file()

def createLocalConfiguration(configFilePath, configFile):

    Path(configFilePath).mkdir(parents=True)
    config = configparser.ConfigParser()
    >> HERE <<
    # TODO: generate all needed files including example lists programmatically

def readLocalConfiguration(configFile):

    # https://docs.python.org/3/library/configparser.html
    config = configparser.ConfigParser()
    
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
    
    files = config[profile]
    
    for key in files:
        print(files.get(key))
        f = open(home + '/.config/configit/{0}'.format(files.get(key)))
        print(f.read())

def readRemoteConfiguration():

    # TODO: if repository has configuration profile uploaded, do nothing
    # TODO: if no repository configuration uploaded, upload it
    return False

if not existLocalConfiguration(configFile):
    print('Local configuration file does not exist.')
    createLocalConfiguration(configFilePath, configFile)

readLocalConfiguration(configFile)

readRemoteConfiguration()

# TODO: push files to repository
# TODO: ask if user wants to download .list files from repository to configuration directory
 
