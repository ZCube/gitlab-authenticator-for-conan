#!/bin/bash
# forked from https://github.com/cguentherTUChemnitz/docker-conan-server

set -e -x

chown conan -R /conan/.conan_server
chown conan -R /conan
chmod +r /conan/.conan_server/*.conf
find /conan/.conan_server/
ls -alR /conan/.conan_server/
cat /conan/.conan_server/gitlabauth.conf
su -c /usr/local/bin/conan_server conan