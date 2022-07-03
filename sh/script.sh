#! /bin/bash

read -n1 -p   "Do you want to continue Y/N " yes
case $yes in  Y|y)
  echo "you are approved all the terms and conitions" 

  read -p "enter your name : " name
  read -p  "enter your ae : " age
  echo "yourname is $name"
  echo "yourage is $age "
  if [ -z $name ]
  then 
    echo "you not entered your name please enter your name  "
    read name
    echo "your name is $name"
  fi
  if [ $age -le 12 ] 
  then 
    echo "YOU ARE KID SORRY"
  elif [ $age -gt 20 ]
  then
    echo "enter you mail id "
    read mail
    chmod u+x scipt.sh
    ./scipt.sh
  fi
    exit
    
   ;;
N|n )
  echo "you need to confrom the this and next step";;
*)
esac
