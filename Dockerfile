FROM python:alpine
MAINTAINER ZCube<zcube@zcube.kr>
# forked from https://github.com/cguentherTUChemnitz/docker-conan-server

VOLUME /conan
RUN pip install --no-cache-dir conan python-gitlab
RUN adduser -S conan -h /conan -s /bin/sh

ADD gitlab_authenticator.py  /conan/.conan_server/plugins/authenticator/gitlab_authenticator.py
RUN chown -R conan /conan && \
    chmod 700 /conan/.conan_server/plugins/authenticator
    

EXPOSE 9300

COPY ./entrypoint.sh /entrypoint.sh
CMD ["/bin/sh", "/entrypoint.sh"]