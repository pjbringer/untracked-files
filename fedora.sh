#! /bin/sh

TMP=`mktemp`

for i in $(yum list installed | grep '\.' | cut -d '.' -f 1); do
	rpmquery -l $i | sed "s-^/\(lib\|bin\|sbin\)-/usr\0-";
done | sort | uniq > ${TMP}

python3 find_files_not_tracked.py ${TMP}

rm ${TMP}

