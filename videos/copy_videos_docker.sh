#!/bin/sh
for i in *.mp4
do
	docker cp $i da3003600a02:/videos/$i
done

