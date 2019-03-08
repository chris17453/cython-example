import os
import sys
from distutils.core import setup, Command
from distutils.extension import Extension


#incase you have the files in a strange location
prefix=""
# you can write a function for this, I just do it by hand
# cython needs to know what files and paths to compile
# these need to be explicitly defined so that so objects can load properly
# you can add extra parameters for search dirs if its a complex file with includes
extensions = [
    Extension("chello.hello",                        [prefix+"chello/hello.pyx"], ),
]
try:
    from Cython.Build import cythonize
except BaseException:
    print ("No Cython installed")
    exit(1)
extensions = cythonize(extensions)
packages=['chello']

# I like to do this , so that I inject a version into the code
exec(open('chello/version.py').read())

setup(
    name='chello',
    version=__version__,
    packages=packages,
    include_package_data=True,
    url='https://github.com/chris17453/cython_example/',
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author='Charles Watkins',
    author_email='charles@titandws.com',
    description='A test cython example',
    ext_modules=extensions,
    classifiers=[
        'Programming Language :: Python :: 2.7',
        "Development Status :: 3 - Alpha",
        "Operating System :: OS Independent",
    ],

    # here we have an entry point, tha main package __init__ defines
    entry_points="""
        [console_scripts]
        chello = chello:cli_main
        """,
    compiler_directives={"language_level": "2"},
    

 
)
