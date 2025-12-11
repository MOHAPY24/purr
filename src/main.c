#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "checks.h"
#include <unistd.h> 

int main(int argc, char *argv[]){
    if(check_python3() != 0){
        return 1;
    }
    if(check_root() != 0){
        return 1;
    }
    if (argc < 2){
        printf("Purr usage:\n");
        printf("purr install <package_name> : Install a package\n");
        printf("purr rebuildrepos : Rebuild package repositories\n");
        printf("purr rebuildworld: Rebuilds the world database\n");
        return 1;
    }
    if (argv[1] != NULL && strcmp(argv[1], "install") == 0){
        printf("Installing package: %s\n", argv[2]);
        char command[256];
        snprintf(command, sizeof(command), "python3 /usr/bin/purr/src/get.py %s", argv[2]);
        int result = system(command);
        if (result != 0){
            printf("Package installation failed.\n");
            return 1;
        }
    }
    else if(argv[1] != NULL && strcmp(argv[1], "rebuildrepos") == 0){
        int result = system("sh /usr/bin/purr/src/rebuild_repos.sh");
        if (result != 0){
            printf("Repository rebuild failed.\n");
            return 1;
        }
    }
    else if(argv[1] != NULL && strcmp(argv[1], "rebuildworld") == 0){
        char conf[256];
        printf("Are you sure you want to rebuild your world file, this will most likely end up in untraceable packages (y/N) ");
        scanf("%s", conf);
        if (strcmp(conf, "y") == 0 || strcmp(conf, "Y") == 0){
            int result = system("sh /usr/bin/purr/src/rebuildworld.sh");
            if (result != 0){
                printf("World rebuild failed.\n");
                return 1;
            }
        }
        else {
            exit(0);
        }
    }
    return 0;
}