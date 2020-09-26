#!/bin/bash

USER=projectx
PASSWORD=
OVERLAP=10
SEGMENT_SIZE=5000
LABELS=$(cat labels.json)
echo "Overlap: " $OVERLAP
echo "Segment size: " $SEGMENT_SIZE
echo "Labels: " $LABELS

i=1
j=0
for file in ~/project_x/data/data/*.mp4; do
	if [ $j -gt 50 ]; then
		t=30
		echo "Sleep $t seconds to avoid error 429..."
		sleep $t
		j=0
	fi 
        curr_task="task_$i"
	python cli.py --auth $USER:$PASSWORD create $curr_task --labels labels.json --overlap $OVERLAP --segment_size $SEGMENT_SIZE share $file
	i=$((i + 1))
	j=$((j + 1))
done

echo "Done"
exit 0
