echo "This is the swap changing tool, use with caution"
echo "Enter a value in MB an example is 8192"
read userSwapMem
inxi -Sp
swapon
sudo swapoff -a
sudo dd if=/dev/zero of=/swapfile bs=1M count=$userSwapMem
sudo chmod 0600 /swapfile
sudo mkswap /swapfile
sudo swapon -a
