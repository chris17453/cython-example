# chello

A cython example project

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
make install # to install it in your usser did with pip
make all     # for all of it
```



## example output 

```shell
[@nd cython_example]$ chello
Version:1.0.4
Hello, from cython.

```