#!/bin/bash

apt update && apt install -y jq wget bzip2 libxtst6 libgtk-3-0 libx11-xcb-dev libdbus-glib-1-2 libxt6 libpci-dev libasound2
wget -qO ~/FirefoxSetup.tar.bz2 "https://download.mozilla.org/?product=firefox-latest&os=linux64"
sudo tar xjf ~/FirefoxSetup.tar.bz2 -C /opt/

INSTALL_DIR="/usr/local/bin"
json=$(curl -s https://api.github.com/repos/mozilla/geckodriver/releases/latest)
input=$(echo "$json" | jq -r '.assets[].browser_download_url | select(contains("linux64"))')
urls=$(echo $input | tr " " "\n")
for addr in $urls
do
        url=$addr
        break
done
curl -s -L "$url" | tar -xz
chmod +x geckodriver
cp geckodriver "$INSTALL_DIR"
ls "$INSTALL_DIR"
echo "installed geckodriver binary in $INSTALL_DIR"
# python3 -c "from selenium import webdriver
# from selenium.webdriver.firefox.options import Options
# options = Options()
# options.headless = True
# driver = webdriver.Firefox(options=options)
# driver.get(\"http://google.com/\")
# print (\"Headless Firefox Initialized\")
# driver.quit()"
