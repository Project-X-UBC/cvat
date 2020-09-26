#!/bin/bash

USER=projectx
PASSWORD=

j=0
for i in {878..1372}; do
	if [ $j -gt 50 ]; then
		t=30
                echo "Sleep $t seconds to avoid error 429..."
                sleep $t
                j=0
        fi
	python cli.py --auth $USER:$PASSWORD delete $i
	j=$((j + 1))
done

echo "Done"
exit 0
