from . import version

def cli_main():
    print("Version:{0}".format(version.__version__))
    print("Hello, from cython.")

if __name__ == "__main__":
    cli_main()
