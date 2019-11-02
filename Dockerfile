FROM ubuntu

ENV PASSWD Root12#@

RUN ["apt-get", "update"]
RUN ["apt-get", "-y", "install", "net-tools", "openssh-server"]
RUN ["echo", "PermitRootLogin yes", ">>", "/etc/ssh/sshd_config"]

RUN ["echo", "${PASSWD}", "|", "passwd", "root", "--stdin"]

RUN ["service", "ssh", "start"]

EXPOSE 22

CMD ["/bin/bash"]