from setuptools import setup

setup(
    name="mldcalc",
    version="0.0.1",
    author="Brendan Donegan",
    author_email="brendan.j.donegan@gmail.com",
    description="A simple program for calculating stats about integers.",
    setup_requires=['coverage', 'nose>=1.0'],
    test_suite='mldcalc.tests',
)
