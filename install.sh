#!/bin/bash
#
echo "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
echo "++++++++++++++++++++++++++【 Install WSamba 】++++++++++++++++++++++++++"
echo "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
echo
echo "Judge the Python Version."
python --version &>a
cat a |grep 2 &>/dev/null
result=$?
if [ "$result" -eq 0 ];then
    echo
else
    echo "Your Python Version is highly,Need Python Version 2."
    exit 1
fi

echo

echo "We need keep Samba and git software installed."
pdbedit &>/dev/null
pdbpwd=$?
smbpassword -h &>/dev/null
smbpwd=$?
if [ "$pdbpwd" -ne 0 -o "$smbpwd" -ne 0 ];then
    yum clean all &>/dev/null && yum makecach fast &>/dev/null
    yum -y install git samba &>/dev/null
fi

echo
echo "Install Django."
pip &>/dev/null
pipwd=$?

if [ "$pipwd" -ne 0 ];then
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py &>/dev/null 
    python get-pipy.py &>/dev/null
fi
pip install django==1.8.2 &>/dev/null

echo "Setting the WSamba install path."
echo
read -p "Please input your install path. [/usr/local/samba] :" path
if [ -z "$path" ];then
    path="/usr/local/samba"
    mkdir -p $path
else
    mkdir -p $path
fi
cd $path 

#删除旧数据
rm -rf web data
 
echo "Pull WSamba program."    
git clone -q https://github.com/Blowfisher/samba.git  && cd samba && mv ./* ../ && cd .. && rm -rf samba

#设置Socket 信息
read -p "Set the server Socket information. [192.168.5.6:8081] :" ip
if [ -z "$ip" ];then
    echo "You Need Set the Socket information,Retry it."
    read -p "Set the server Socket information. [192.168.5.6:8081] :" ip
fi

echo

if [ -z "$ip" ];then
    echo "Failure your socket ."
    exit
fi

echo
echo "Starting WSamba..."
cd web && nohup python manage.py runserver $ip &
echo
echo "++++++++++++++++++++++++++++++++++++++【Success Installed】++++++++++++++++++++++++++++++++++++++++++++++++++++++++"

