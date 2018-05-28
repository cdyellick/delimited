# cy.delimited

A set of utilities for working with delimited data

## delimiter_magic

The key to delimited is the delimiter_magic decorator.  It splits the delimited string to a list before calling the decorated functions and then converts the result back to a delimited string before returning.

delimiter_magic can be applied to any function that takes a list as a first argument and returns a list.