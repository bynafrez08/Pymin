#!/bin/bash

cat /etc/shells | cut -d/ -f3,4 --output-delimiter=" " | sed -e 's/\<shells: valid login shells\>//g' | sed -e 's/\<bin\>//g' | awk '{print $1}' ORS=' ' | awk '{ delete a; for (i=1; i<=NF; i++) a[$i]++; n=asorti(a, b); for (i=1; i<=n; i++) printf b[i]" "; print ""}'

