This repository contains code to compute the Sequential Rank Agreement (SRA) between two or more ordered lists as specified in the 2019 paper *Sequential rank agreement methods for comparison of ranked lists* by Claus Thorn Ekstrøm, Thomas Alexander Gerds, and Andreas Kryger Jensen in the journal Biostatistics, doi:10.1093/biostatistics/kxy017.

It includes a partial verification problem in which the results of Table 1(c) are reproduced.

### Dependencies

The code was written and tested on Python 2.7 for two ordered lists of the same length. It requires the following packages

```
csv
numpy
itertools
matplotlib
```

### How can I use this code?

1. Save your ordered lists as columns (with a header row) in a csv. 
2. Specify the filepath of the csv and the number of columns in main.py.
3. Run plot_sra(filepath, nCols) to compute the sequential rank agreement between your lists and plot how it varies with increasing list depth.

```
import sra
    
filepath = 'myLists.csv'
nCols = 2
plot_sra(filepath, nCols)
```
