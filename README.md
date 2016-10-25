# yhat demo
This repository contains some demo code to be used in a demonstration of yhat's ScienceOps software.

## DataWrangler.py
A class that performs some basic data-wrangling tasks. It would be super useful to use the result the function `group_and_normalise` in other parts of some application. Preferably to throw in the result of some database query. Some additional code may be needed to convert the result of this query to a pandas DataFrame.

## demo.py
A scripts that demonstrates the use of DataWrangler.py.

## 42.csv
Some anonymized sample data-dump that contains three columns:
- ts: the time stamp
- unit: the units of measurement
- value: the measured value
