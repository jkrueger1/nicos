#! /bin/bash
. $NICOSVENV/bin/activate

tools/check-setups -o setupcheck.log -s nicos_*/*/setups nicos_*/*/guiconfig*.py || ((res++)) || /bin/true
# */
~/tools2/bin/sc2gerrit

exit $((res))
