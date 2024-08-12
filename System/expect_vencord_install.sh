#!/usr/bin/expect
# Path to your application
spawn sh -c "$(curl -sS https://raw.githubusercontent.com/Vendicated/VencordInstaller/main/install.sh)"

# Confirm the selection with Enter
send -- "\r"

# Wait for the process to complete
expect eof
