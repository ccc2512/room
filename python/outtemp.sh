#!/bin/bash
cd /usr/share/webiopi/htdocs/bs
outTerm=`curl -k -s http://dove.omsk.otpbank.ru/files/weather.js`
echo $(date "+%Y-%m-%d %H:%M:%S,") `echo $outTerm | grep -E -o "([-0-9\.]{2,6})"` >> /usr/share/webiopi/htdocs/ccc/txt/data_outtemp.txt
