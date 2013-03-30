#! /bin/sh

TMP=`mktemp`

{ echo / ; python2 gentoo_owned.py; } | sort | uniq > ${TMP}

python3 find_files_not_tracked.py ${TMP}

rm ${TMP}

