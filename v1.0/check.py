#!/usr/bin/env python

###########################################
#                                         #
#  Validator Emaillist v 1.0 at 2014/9/1  #
#       Coded By AmRocky-Dz97             #
#             fb: fb/team4sec             #
#                                         #
###########################################

import urllib
import sys
from os.path import exists
 

logo = """Welcome To Maillist Validator v 1.0
it's Open source But Dont touch the
name of creator :v and thank you
my email1 : amrocky.dz97@gmail.com
my email2 : shark2serv@outlook.com
Enjoyy !!!
""";

def checkpath():
 l = len(sys.argv);
 if l >= 2 :
  if exists(sys.argv[1]) :
   return 1;
  else :
   return 0;
 else :
  return 0;

def isemail(email) :
 try :
  cchar = len(email);
  arr = email.split("@");
  url = "http://"+arr[1]
  op = urllib.urlopen(url);
  s = op.code
  op.close();
  if s == 200 :
   return 1;
 except :
  return 0;

def getdom(email) :
  arr = email.split("@");
  dom = arr[1];
  return dom

def sav200(email) :
 arr = email.split("@");
 so = open("200.db","a+");
 so.write(arr[1]+"\n");
 so.close();


def fetch200():
 chk = open("200.db","r");
 alls = chk.read();
 emailn = alls.split();
 lemail = len(emailn);
 ccl = [];
 for i in range(lemail) :
  ccl += [emailn[i].replace("\n","")];
 return ccl;


if checkpath() == 0 :
 print " [!] File Not Found !!"
 print "~Ex : python check.py emailsfile";
 sys.exit(1);
print logo;
path = sys.argv[1];
ban = ['@','.'];
op = open(path,"r");
data = op.read();
ss = data.split();
ls = len(ss);
sls = str(ls);
print "Load Email : %d"%ls
clean = [];
for i in range(ls) :
 if ban[0] in ss[i] and ban[1] in ss[i] :
  clean += [ss[i]];
lc = len(clean);
checked = [];
for h in range(lc) :
 if clean[h] not in checked : 
  com = str(h)+"/"+sls
  if getdom(clean[h]) in fetch200() or isemail(clean[h]) == 1 :
   sys.stdout.write("\r"+com);
   sys.stdout.flush();
   checked += [clean[h]];
   if getdom(clean[h]) not in fetch200() :
    sav200(clean[h]);
  else :
   sys.stdout.write("\r"+com);
   sys.stdout.flush();

llc = len(checked);
print "\nEmail valid : %d"%llc
fname = "c-c"
if exists(fname) :
 nname = raw_input("c-c is already exist enter New name : ");
 opp = open(nname,"a+");
 for j in range(llc) :
  opp.write(checked[j]+"\n");
 opp.close();
else :
 oppp = open(fname,"a+");
 for j in range(llc) :
  oppp.write(checked[j]+"\n");
 oppp.close();

print "Done";



