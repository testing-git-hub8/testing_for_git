#! /bin/bash

var3="parrot"
var2="this"

read var
if   grep parrot  /etc/passwd
then 
  echo $var
   ls /home/$var
   ls -l /home/$var b*
 else
   echo "this user $var not found"
fi

if  [ -z  $var ]
then
echo "this is $var3 greater than $var2"
else 
  echo "not working"
fi

if [ shellscripts.sh -ot shellscript.sh ] 
then 
  echo "waste of time"
  ls /home/
else 
  echo "this is waste of yum two "
fi
