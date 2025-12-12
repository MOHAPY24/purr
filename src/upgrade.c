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
    if(argc > 1 && argv[1] != NULL && strcmp(argv[1], "--no-conf") == 0){
        int result = system("python3 /usr/bin/purr/src/upgrade.py y");
        if(result != 0){
            printf("Upgrade failed.\n");
            return 1;
    }
    }
    else{
        int result = system("python3 /usr/bin/purr/src/upgrade.py");
        if(result != 0){
            printf("Upgrade failed.\n");
            return 1;
    }
    }
    return 0;
}