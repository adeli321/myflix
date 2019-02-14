#!/bin/sh
for i in *.png
do
	docker exec -it mongy mongofiles -d 'thumbnails' -u restheart -p R3ste4rt! --authenticationDatabase admin put -l /thumbnails/$i $i
done

