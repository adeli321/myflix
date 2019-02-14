#!/bin/sh
for i in *.mp4
do
	docker exec -it mongy mongofiles -d 'videos' -u restheart -p R3ste4rt! --authenticationDatabase admin put -l /videos/$i $i 
done
