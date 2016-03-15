#!/bin/sh
curpath=`dirname $0`
nohup python ${curpath}/nGle_sys_mon.py $@ > /dev/null & 2>&1

