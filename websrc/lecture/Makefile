all = index.php islands.html

target : $(all)

index.php : index.md
	markdown index.md > index.php

islands.html : islands.md
	markdown islands.md > islands.html

index.html : index.php
	php index.php > index.html

install : $(all)
	cp $(all) ../../website/lecture

clean :
	rm *.php *.html
