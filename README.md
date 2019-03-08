# chello

A cython example project

- ".pyx" extensions are used to mark python files as cython. It helps with setup.
- When you build, cython will create ".c" source files for each cythonized extensions
- These files are included into your dist package, not the ".pyx" files
- When installing the package, the ".c" files are compiled into a ".so"


## Prerequizites

- you need a compiler .. gcc
- you need cython to build
- you need the python source


### Fedora/CentOS PreReq install
```
pip install cython --user
dnf install python2-devel
```


## make

```shell

make clean   # to delete build files .c;.so.gz
make build   # to build the dist file, it also bumps the patch version +1
make install # to install it in your user dir with pip
make all     # do all the things
```


## example output 

```shell
[@nd cython_example]$ chello
Version:1.0.4
Hello, from cython.

```

### compiled and tested on
- Fedora 29 x64 with python 2
