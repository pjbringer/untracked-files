#! /bin/sh

TMP=`mktemp`

{ echo '/'; pacman -Ql | sed 's-/$--'; } | cut -d " " -f 2-  | sort | uniq > ${TMP}

python3 find_files_not_tracked.py ${TMP}

rm ${TMP}

