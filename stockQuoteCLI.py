#! /usr/bin/python
import os
import sys
import string
import urllib
from xml.dom import minidom
scripCode = sys.argv[1]
fdate = sys.argv[2]
fmonth = sys.argv[3]
fyear = sys.argv[4]
url = "http://www.google.com/ig/api?stock=%s"% scripCode 
dom = minidom.parse(urllib.urlopen(url))
companyNameTag = dom.getElementsByTagName('company')
companyNameAttributes = companyNameTag[0].attributes['data']
companyName = companyNameAttributes.nodeValue
link = "http://www.bseindia.com/histdata/stockprc2.asp?main1=%s" % scripCode+"&fdate=%s" %fdate+"&fmonth=%s"%fmonth+"&fyear=%s"%fyear+"&main2=1&default1=1"
print link
orignalPsourceObj = urllib.urlopen(link)
orignalPsource = orignalPsourceObj.read()
file = open('Test.txt','w')
file.write(orignalPsource)
file.close()
file1 = open('Test.txt','r')
for line in file.readlines():
    line = line.strip()
    txt = "<td align=left width=100px valign=bottom bgcolor=#e6eef1><font face=Arial size=2 color=#ic355d>"
    bool = txt in line
    if  bool == True:
        file1 = open('Test.txt','w')
        file1.write(line)
        file1.close() 
modifiedPsourceObj = open('Test.txt','r')
text = modifiedPsourceObj.read()
text = text.strip()
p = string.replace(text,'<tr><td align=left width=100px valign=bottom bgcolor=#e6eef1><font face=Arial size=2 color=#ic355d>','%s;'%companyName)
q = string.replace(p,'&nbsp;</font></td><td align=right valign=bottom bgcolor=#e6eef1><font face=Arial size=2 color=#ic355d>',';')
r = string.replace(q,'&nbsp;</font></td></tr>','\n')
modifiedPsourceObj.close()
output = open('Output.txt','a')
output.write(r)
output.close()
os.remove('Test.txt')  
