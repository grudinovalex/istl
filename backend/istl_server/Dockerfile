FROM fedora:latest

LABEL maintainer="grudinov.alex@gmail.com"

SHELL ["/bin/bash", "-c"]

RUN sed -i '/tsflags=nodocs/d' /etc/dnf/dnf.conf && \
    yum update -y && \
    yum upgrade -y && \
    rpm -qa | sort | sed 's/-[0-9].*[0-9]*//g' | xargs dnf -y reinstall && \
    yum update -y && \
    yum upgrade -y && \
    yum install -y man-pages man-db man ncurses vim groff cowsay htop iputils wget git tree nano binutils bind-utils file unzip sshpass nano pcre2-tools openssh-server cracklib-dicts && \
    mandb && \
    dnf update && \
    echo 'istl2024' | passwd --stdin root && \
    sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config && \
    ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key -N '' && \
    adduser admin &&\
    echo 'tuxedo9999' | passwd --stdin admin && \
    usermod -aG wheel admin

COPY my_banner_message /etc/motd.d
COPY tux.pdf /home/admin

EXPOSE 22

CMD ["/usr/sbin/sshd", "-D"]
