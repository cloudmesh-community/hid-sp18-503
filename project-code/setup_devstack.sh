sudo apt-get install -y python-systemd
sudo useradd -s /bin/bash -d /opt/stack -m stack
echo "stack ALL=(ALL) NOPASSWD: ALL" | sudo tee /etc/sudoers.d/stack
sudo su -l stack

sudo apt-get install git-core -y
git clone https://git.openstack.org/openstack-dev/devstack
