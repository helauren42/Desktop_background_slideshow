all:
	update.sh

re:
	./uninstall.sh
	rm -f bg-slideshow
	rm -f bg-slideshow.x.c
	shc -f bg-slideshow.sh -o bg-slideshow
	rm -f bg-slideshow.x.c
	./install.sh
