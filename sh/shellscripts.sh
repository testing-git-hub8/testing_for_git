case $USER in parrot | testing )
  echo "this is hero of the user";;
unknow | test)
  echo "error will exstis";;
*)
  echo "this is fucking"
esac

file="change"
for change in $file
do 
  echo "file are dangerous $file"
  cat $file
done

if [ -x /home/parrot/shellscript.sh ] || [ -d /home/parrot/sh ]
then 
   bash shellscript.sh
fi

name="this that we are and all of that"
for name in $name
do 
  echo "this is the file $name"
done

for (( a=1,b=23; a<20 ; ++a , --b ))
do
  echo " $a +  $b "
done

echo "$1"
echo "$2"
echo ""$?
