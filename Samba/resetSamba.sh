#!/bin/bash
cp /usr/share/samba/smb.conf /etc/samba/smb.conf
dpkg-reconfigure samba-common
