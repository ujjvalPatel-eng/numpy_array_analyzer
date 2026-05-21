# NumPy Analyzer

A small interactive Python utility for creating and working with NumPy arrays.

## Overview

This project contains a single script, `analyzer.py`, that lets you:

- create 1D, 2D, or 3D NumPy arrays from keyboard input
- perform indexing and slicing operations
- combine or split arrays
- search, sort, and filter arrays
- execute mathematical operations between arrays
- compute statistics such as mean, median, standard deviation, and variance

## Requirements

- Python 3.10 or newer (required for `match` statement syntax)
- NumPy

## Installation

Install NumPy with pip:

```bash
python -m pip install numpy
```

## Usage

Run the analyzer script:

```bash
python analyzer.py
```

Follow the interactive menu prompts to:

1. create an array
2. index or slice the array
3. perform arithmetic operations
4. combine or split arrays
5. search, sort, or filter elements
6. compute aggregate statistics
7. exit

## Notes

- The script stores a single array in memory and operates on that array until the program exits.
- Array operations currently support up to 3 dimensions.
- Input values must be integers.

## File

- `analyzer.py`: main interactive NumPy array analyzer script
