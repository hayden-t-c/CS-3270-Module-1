# Module 1

Module 1 is an introduction to the system and demonstrates how to set up a Python environment.

## Installation

Install panadas package

```bash
pip install pandas
```

## Usage

This function loads a csv file into a pandas dataframe. Function returns that pandas dataframe.

```python
import pandas as pd

def loadCSV(filepath):
    csvdata = pd.read_csv(filepath)
    return csvdata
```