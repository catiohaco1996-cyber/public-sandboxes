#!/bin/bash

# Generate Hostname
if [ -n "$ECS_CONTAINER_METADATA_URI_V4" ]; then
  RUNTIME_ID=$(echo "$ECS_CONTAINER_METADATA_URI_V4" | cut -d '/' -f 5)
  export HOSTNAME="$RUNTIME_ID"
else
  export HOSTNAME="sandbox"
fi

echo $HOSTNAME > /etc/hostname
echo "127.0.0.1 $HOSTNAME" >> /etc/hosts

# Reforce password
echo root:`echo $HOSTNAME | cut -d '-' -f 1` | chpasswd

# Restart ssh
service ssh restart >/dev/null 2>&1

# Run console
ttyd --cwd /root --writable --credential=$(echo $HOSTNAME | cut -d '-' -f 1):$(echo $HOSTNAME | cut -d '-' -f 1) -p 3001 /bin/bash &

# Run VSCode
openvscode-server --host 0.0.0.0 --connection-token=$(echo $HOSTNAME | cut -d '-' -f 1) --log off 2>&1
