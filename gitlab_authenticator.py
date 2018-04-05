import gitlab
import os
# refer : https://github.com/python-gitlab/python-gitlab/blob/master/docs/api-usage.rst

# private token or personal token authentication
def gitlab_auth_by_token(url, id, token):
  try:
    gl = gitlab.Gitlab(url, private_token=token)
    gl.auth()
    return gl.user.name.lower() == id.lower()
  except:
    return False

# username/password authentication (for GitLab << 10.2)
def gitlab_auth_by_password(url, id, password):
  try:
    gl = gitlab.Gitlab(url, email=id, password=password)
    gl.auth()
    return True
  except:
    return False
    
def memoize(function):
  memo = {}
  def wrapper(*args):
    if args in memo:
      return memo[args]
    else:
      rv = function(*args)
      memo[args] = rv
      return rv
  return wrapper

try:
  import configparser
except:
  from six.moves import configparser

@memoize
def get_url():
  from os.path import expanduser
  home = expanduser("~")
  config_file = os.path.join(home, ".conan_server", "gitlabauth.conf")
  if not os.path.exists(os.path.dirname(config_file)):
    os.makedirs(os.path.dirname(config_file))
  config = configparser.ConfigParser()
  config['gitlab'] = {'url' : 'https://gitlab.example.com'}
  if os.path.exists(config_file):
    config.read(config_file)
  else:
    with open(config_file, 'w') as fp:
      config.write(fp)
  return config['gitlab']['url']
  
def get_class():
  print("GitLabAuthenticator Loaded : " + get_url())
  return GitLabAuthenticator()

class GitLabAuthenticator(object):
  def valid_user(self, username, plain_password):
    print("valid_user")
    if gitlab_auth_by_password(get_url(), username, plain_password):
      return True
    return gitlab_auth_by_token(get_url(), username, plain_password)
