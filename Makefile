.SILENT:
prog = purr
cc = gcc
msg = "Auto commit from Makefile script: timestamp $(shell date +"%Y-%m-%d %T")"


$(prog): src/main.c
	$(cc) src/checks.c src/main.c -o $(prog)
	cp $(prog) /usr/local/bin/$(prog)
	rm $(prog)
	mkdir -p /usr/bin/purr
	mkdir -p /etc/purr
	mkdir -p /usr/bin/purr/src
	mkdir -p /usr/bin/purr/builds
	mkdir -p /usr/bin/purr/purr.d
	rm -rf /etc/purr/*
	cp -r src/ /usr/bin/purr
	cp -r purr.d/ /etc/purr/
	cp world.json /etc/purr/world.json
	chmod -R a+rw /etc/purr
	chmod -R a+rw /usr/bin/purr
	$(cc) src/upgrade.c src/checks.c -o purr-upgrade
	-cp purr-upgrade /usr/local/bin/purr-upgrade
	-rm purr-upgrade

clean:
	rm -f /usr/bin/$(prog)
	rm -rf builds/*

gitcommit: # remove if not contributing
	rm -rf builds/*
	echo "" >> world.json
	git add .
	git commit -m $(msg)
	git push origin master