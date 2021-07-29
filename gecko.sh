!#bin/bash
export GECKO_DRIVER_VERSION='v0.24.0'
wget https://github.com/mozilla/geckodriver/releases/download/$GECKO_DRIVER_VERSION/geckodriver-$GECKO_DRIVER_VERSION-linux64.tar.gz
tar -xvzf geckodriver-$GECKO_DRIVER_VERSION-linux64.tar.gz
rm geckodriver-$GECKO_DRIVER_VERSION-linux64.tar.gz
chmod +x geckodriver
cp geckodriver /usr/local/bin/