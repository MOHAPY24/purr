prog = purr
cc = gcc
msg = "Auto commit from Makefile script: timestamp $(shell date +"%Y-%m-%d %T")"


clean:
	rm -f /usr/bin/$(prog)
	rm -rf builds/*
install:
	$(cc) src/checks.c src/main.c -o $(prog)
	cp $(prog) /usr/local/bin/$(prog)
	rm $(prog)
	chmod +x /usr/local/bin/$(prog)
	mkdir -p /usr/bin/purr
	mkdir -p /etc/purr
	rm -rf /etc/purr/*
	cp -r src/* /usr/bin/purr/src
	cp -r builds /usr/bin/purr/builds
	cp -r purr.d/* /etc/purr/purr.d
	cp world.json /etc/purr/world.json
	chmod -R a+rw /etc/purr
	chmod -R a+rw /usr/bin/purr
gitcommit: # remove if not contributing
	rm -rf builds/*
	echo "" >> world.json
	git add .
	git commit -m $(msg)
	git push origin main