#!/bin/bash
# forked from https://github.com/cguentherTUChemnitz/docker-conan-server

set -e -x

chown -R conan /conan
cat /conan/.conan_server/gitlabauth.conf
su -c /usr/local/bin/conan_server conan