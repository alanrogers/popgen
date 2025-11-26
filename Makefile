website :
	cd website; rsync -Cavu --include='.htaccess' --copy-links --delete * $(HOME)/website/tch/ant5221

.PHONY: website
