eval `ssh-agent -s`
mkdir -p /root/.ssh
cp /vault/id_rsa /root/.ssh/id_rsa
chmod 400 /root/.ssh/id_rsa
ssh-add /root/.ssh/id_rsa
rm /root/.ssh/id_rsa
