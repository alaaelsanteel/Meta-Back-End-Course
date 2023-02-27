* ### Modules 
> similar to files, while packages are like directories that contain different files
  Any module that contains the  __path__ definition is a package
* ### Packages
> when viewed as a directory, can contain sub-packages and other modules
* ### Modules
> can contain classes, functions and data members just like any other Python file. 
* ### Library
> is a term that's used interchangeably with imported packages, but in general it refers to a collection of packages.
###          you can import any of them using import statements.  
* Third-party package add-ons of Python can be found in the Python Package Index (PyPI)
* To install packages that aren't a part of the standard library programmers use ‘pip’
  * To verify its installation >> py -m ensurepip --upgrade
  * install packages using pip >> py -m pip install "SomeProject"
  * To install a third-party package such as ‘requests’ >> py -m pip install requests
  * package such as matplotlib, the contents that are used most commonly are present inside the subpackage pyplot.
    Pyplot eventually may consist of various functions and attributes.
    > import matplotlib.pyplot  " importing a sub-package "
    > import matplotlib.pyplot as plt " "