#!usr/bin/python
# -*- coding:utf-8 -*-
import re
import hashlib
import datetime
import time


class ForStringMd5():
    def ABA(self, a, b):
        """
        Formula :(a+b) to the a power,a and b are positive integers
		
        For example：
        | ${c} | aba | 2 | 3 |
		
        And get the following:
		${c}=25
        """
        return (int(a) + int(b)) ** int(a)

    def Find_IP(self, url):
        """
		URL=http://www.example.com?ip=192.187.111.198&code=12345&name=cat,
        get host 192.187.111.198
		
        For example：
        | ${ip} | Find IP | http://www.example.com?ip=192.187.111.198&code=12345&name=cat |
		
		And get the following:
        ${ip}=192.187.111.198
        """
        ip = re.findall('ip=(.*?)&', url, re.I)
        if (ip and ip[0] != ''):
            return ip[0]

        else:
            return "Not matched IP"

    def MD5_RandStr(self, dataType, signInfo='dtxy123456a'):
        """
		The first ginseng : dataType=1&date=2018-08-02&timestamp=1533283780
        The second ginseng : dataType=1&date=2018-08-02&timestamp=1533283780&dtxy123456a
        signInfo = e80d6fe9474730b1fb99f798d7f95ff0
        Md5 key : key1=value1&key2=value2&secret
        The last url:
        http://0.0.0.0:8080/fuel/fuel/list?dataType=1&date=2018-08-02&timestamp=1533283780&signInfo=e80d6fe9474730b1fb99f798d7f95ff0
		
        For example：
        | ${key} | MD5 RandStr | dataType | dtxy123456a |
		
		And get the following:
        ${key}=e80d6fe9474730b1fb99f798d7f95ff0
        """
        date = datetime.datetime.now().strftime('%Y-%m-%d')
        timestamp = int(time.mktime(time.strptime(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')) * 1000)
        return hashlib.md5(str(dataType)+'&'+str(date)+'&'+str(timestamp)+'&'+str(signInfo)).hexdigest()

if __name__ == '__main__':
    ForStringMd5()
