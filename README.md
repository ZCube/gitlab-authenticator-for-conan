# gitlab-authenticator-for-conan

# Install

1. copy gitlab_authenticator.py to ~/.conan_server/plugins/authenticator

2. create ~/.conan_server/gitlabauth.conf

~~~
[gitlab]
url = https://gitlab.example.com
~~~

3. modify ~/.conan_server/server.conf
 
~~~
...
custom_authenticator: gitlab_authenticator # must do !

# permission setting example
# case sensitive.
[write_permissions]
# */*@*/*: zcube # add permision to write
...
[read_permissions]
# */*@*/*: zcube # add permision to read
...
~~~

4. run

~~~
C:\Python35\Scripts>conan_server
GitLabAuthenticator Loaded : https://gitlab.example.com
Bottle v0.12.13 server starting up (using WSGIRefServer())...
Listening on http://0.0.0.0:9300/
Hit Ctrl-C to quit.
~~~
