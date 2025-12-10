prog = purr
cc = gcc
msg = "Auto commit from Makefile script: timestamp $(shell date +"%Y-%m-%d %T")"

$(prog): src/main.c
	$(cc) src/checks.c src/main.c -o $(prog)
clean:
	rm -f /usr/bin/$(prog)
	rm -rf builds/*
install: # needs normal make used and sudo
	cp $(prog) /usr/local/bin/$(prog)
	chmod +x /usr/local/bin/$(prog)
gitcommit: # remove if not contributing
	rm -rf builds/*
	echo "" >> world.json
	git add .
	git commit -m $(msg)
	git push origin main