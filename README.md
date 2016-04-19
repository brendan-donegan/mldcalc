MLD Calculator
==============

MLD Calculator provides a set of functions for calculating statistics about
integers stored in a CSV file. The statistics that can be calculated are:

- The total number of integers in the file
- The number of integers in the line with the most integers
- The mean of all integers in the file
- The most common integer(s) in the file

Usage
=====

The simplest way to use MLD Calculator is to simply install Python 2.7 and run
the simple command line script directly:

  python mldcalc/mldcalc <subcommand> <path to csv>

The available subcommands are:

- 'num' for the number of integers
- 'longest' for the length of the longest line
- 'mean' for the mean of all integers
- 'common' for the most common integer(s)

Running tests
=============

Running the tests requires a virtual environment (a common Python development
tool). It can be installed on a Debian-based Linux distribution using:

  sudo apt-get install python-virtualenv

Then we can run:

  virtualenv --python=python2.7 venv
  . venv/bin/activate
  python setup.py test

All tests should run and pass (12 in total)
