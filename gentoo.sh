#! /bin/sh

TMP=`mktemp`
echo $TMP

{ echo / ; python3 gentoo_owned.py; } | sort -u > ${TMP}

python3 find_files_not_tracked.py ${TMP}

rm ${TMP}

