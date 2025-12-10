#include "checks.h"
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int check_python3(){
    if(system("python3 --version &> /dev/null") != 0){
            printf("fatal ERR! Python3 is not installed or not found in PATH.\n");
            return 1;
    }
    return 0;
}

int check_root(){
    int euid = geteuid();

    if (euid == 0) {
        return 0;
    } else {
        printf("fatal ERR! Please run as root.\n");
        exit(1);
    }
}

