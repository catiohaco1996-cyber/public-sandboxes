FROM ubuntu:22.04

RUN apt-get update

# Install TTYD
RUN apt-get install -y wget
RUN apt-get install -y build-essential cmake git libjson-c-dev libwebsockets-dev
RUN apt-get install -y emacs vim gdb lsof sudo
RUN apt-get install -y telnet file
RUN git clone https://github.com/tsl0922/ttyd.git
WORKDIR /ttyd
RUN mkdir build
WORKDIR /ttyd/build
RUN cmake ..
RUN make
RUN make install

# Cleaning
WORKDIR /
RUN rm -r /ttyd

# Install VSCode
RUN wget https://github.com/gitpod-io/openvscode-server/releases/download/openvscode-server-v1.75.1/openvscode-server-v1.75.1-linux-x64.tar.gz
RUN tar -xzf openvscode-server-v1.75.1-linux-x64.tar.gz
WORKDIR /openvscode-server-v1.75.1-linux-x64
RUN mv bin/openvscode-server /bin
RUN rm -r bin
RUN mv * /usr/

# Cleaning
WORKDIR /
RUN rm -r openvscode-server-v1.75.1-linux-x64 openvscode-server-v1.75.1-linux-x64.tar.gz
RUN rm /root/.wget-hsts

# Tools
RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN apt-get install -y gcc
RUN apt-get install -y nano ssh
RUN apt-get install -y iproute2 dnsutils iputils-arping iputils-ping iputils-tracepath iputils-clockdiff

# Install man pages
RUN sed -i 's:^path-exclude=/usr/share/man:#path-exclude=/usr/share/man:' \
        /etc/dpkg/dpkg.cfg.d/excludes
RUN apt-get install -y man man-db manpages-posix

# Allow remote login
RUN echo 'PasswordAuthentication yes' >> /etc/ssh/sshd_config
RUN echo 'PermitRootLogin yes' >> /etc/ssh/sshd_config
RUN echo 'AuthorizedKeysFile .ssh/authorized_keys' >> /etc/ssh/sshd_config
RUN echo 'TCPKeepAlive yes' >> /etc/ssh/sshd_config

RUN apt-get install -y curl git

COPY run.sh /etc/
RUN sed -i 's/\r$//' /etc/run.sh

# Install SSH Key script
RUN pip3 install requests

# Create Shell, navigation project files
RUN mkdir /root/empty_directory
RUN touch /root/not_here
RUN touch /root/old_school
RUN touch /root/ready_to_be_removed
RUN echo 'Hello School' > /root/school

# Create Admissions project files
RUN mkdir /root/my_school
RUN echo "d254501c321d4a02" > /root/my_school/first_file

# Install Betty for C projects
RUN git clone https://github.com/hs-hq/Betty.git
WORKDIR /Betty
RUN ./install.sh
WORKDIR /
RUN rm -r /Betty

# Configure history
RUN echo 'export PROMPT_COMMAND="history -a"' >> ~/.bashrc

# Bootstrap is in run.sh (chpasswd, ssh, ttyd, openvscode). Exec JSON form; invoke bash so run.sh need not be +x.
ENTRYPOINT ["/bin/bash", "/etc/run.sh"]
