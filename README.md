# purr

A package manager for people who love building from source

![image](https://img.shields.io/badge/GPL--3.0-red?style=for-the-badge)
![image](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![image](https://img.shields.io/badge/C-00599C?style=for-the-badge&logo=c&logoColor=white)

## What is purr

purr is a simple package manager that can build any type of application that uses a Makefile to build.
Written in C and Python, it is modular, small and is VERY slow.


## Installation 

clone the repo

```shell
git clone https://github.com/MOHAPY24/purr
cd purr
```

DO NOT DELETE THE `.git` FOLDER! it is important for detecting updates.

```shell
sudo make
```

then test with a test tool

```shell
sudo purr install mfget --no-conf # no conf so you dont have to confirm the install
```

upgrade purr

```shell
sudo purr-upgrade --no-conf
```

## Contributions

Contributions are appreciated, fork the repo and do a pull request.

## Credits

Credits to kma and me :).

## LICENSE

purr is licensed under the GPLv3 (GNU Public General License Version 3), see more in [LICENSE](LICENSE).
