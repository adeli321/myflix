#!/bin/sh
for i in *.png
do
	docker cp $i da3003600a02:/thumbnails/$i
done

