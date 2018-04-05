#!/bin/bash
# forked from https://github.com/cguentherTUChemnitz/docker-conan-server

set -e -x

chown -R conan /conan
find /conan
cat /conan/.conan_server/plugins/authenticator/gitlabauth.json
cat /conan/.conan_server/server.conf
su -c /usr/local/bin/conan_server conan