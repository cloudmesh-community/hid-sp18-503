## Travis CI

Travis CI is a continuous integration service that syncs with github
and allows developers to automate the process of testing an deploying
code.  Travis CI allows users to test code for various different
environments and allows the use of various languages, which can be
easily specified by adding a travis.yml file in the repository.

This tutorial explores testing for python.

* First requirement to use Travis CI is to have a github account Next
* create an account on the trais CI website or login using your github
* account and alow travis to sync the repositories <a href ="https://travis-ci.org/auth?redirectUri=https%3A%2F%2Ftravis-ci.org%2Fauth%3FredirectUri%3Dhttps%253A%252F%252Ftravis-ci.org%252F">  here </a>.
* Next select the repository that you want to use with Travis-CI on
  travis website
* Go to github and locally clone the repository.

### The travis.yml file

The travis.yml file describes to travis, which language is used, what environments to test the code on, and to install any dependencies that may be required.

* The first line of the yml file specifies the language used
      language: python

* Next we need to specify the versions of python we need to test the code for.
  Here we need to specify the versions in the same manner as we use to
  install the language, as travis creates a virtual environment for each of
  these versions.
      python:
        - 3.6.4
	- 2.7.13

* Dependencies can be specified in the yml file under using he ```install:```
  tag. It is recommended that the dependencies be installed using pip as travis
  creates a virtual environment for each python version.
  	  install:
	    - pip install -r requirements.txt
	    
* If tests should be perfrmed for different versions of libraries,
  such as django for each python version, then ```env:``` tag can be used
  along with the ```install``` tag.
  	env:
	  - django_version=1.10
	  - django_version=1.11
	install:
	  - pip install Django==$django_version

* finally to specify what commands to execute to run the tests,
  we use the ```script:``` tag. If a makefile is used for this purpose,
  this can be done a follows however travis allows the use of pytest for
  this pupose as well.
       script: make test
 