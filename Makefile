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
	mkdir -p /etc/purr
	cp -r * /etc/purr
	chmod -R a+rw /etc/purr
	rm /etc/purr/README.md
	-rm /etc/purr/purr
gitcommit: # remove if not contributing
	rm -rf builds/*
	echo "" >> world.json
	git add .
	git commit -m $(msg)
	git push origin main