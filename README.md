# distributions

## Summary
This package allows a set of numbers to be drawn from three distributions: *normal*, *poisson* and *binomial*.
The code is built upon the Numpy random number generator library.

This can be achieved with both a functional approach and an object oriented approach.

### Functional:

The `draw` function takes the arguments `size` and `distribution`, which give the number of random numbers required and the chosen distribution respectively.
Additional keyword arguments are also given to parameterise the chosen distribution.
These are `mu` and `sd` for the normal distribution, `lam` for the poisson, and `n` and `p` for the binomial.
The function returns a numpy array.

### Object Oriented:

There are three generator classes, one for each distribution: `NormalGen`, `PoissonGen`, and `BinomialGen`.
An instance of such a class represents a particular parameterisation of the distribution, with parameters provided as arguments upon instantiation.
A random sample can be generated from an instance by calling the `draw` method.
The numer of random numbers to be drawn is given by the `size` argument, with a single sample being drawn as a default.
The method returns a numpy array.

A set of summary statistics of a sample can be printed with the `summarise` class method.
This can be achieved when a sample is drawn by setting the `printSummary` attribute in the `draw` method to `True` (this is `False` as a default).

Additionally the `summarise` method can be called on any set of numbers outside the scope of each class, for instance `NormalGen.summarise((1,2,3,4))` will print summary statistics for the set of numbers 1-4.

## Installation

1. Navigate your chosen installation directory.
2. Clone the repository: `git clone https://github.com/wf102/distributions.git`.
3. Ensure that the installation directory is included in you PYTHONPATH environment variable.