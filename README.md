## Overview

This project demonstrates the process of building a neighborhood matrix from a dataset and performing Singular Value Decomposition (SVD) using different methods. It includes steps for matrix construction, SVD computation, accuracy verification, and eigenvalue visualization.

This code was developed as part of our Optimization course project at IASBS, in collaboration with my groupmate, [Erfan Faridi](https://github.com/erfanfaridii/).

## Features

- **Neighborhood Matrix Construction**  
  Creates a binary matrix representing connections between distinct values (sources and destinations).

- **Singular Value Decomposition (SVD)**  
  Implements SVD using:
  - NumPy
  - SciPy
  - Manual computation via eigenvalue decomposition

- **Accuracy Verification**  
  Compares the determinant of matrices \( U \) and \( V \) from different SVD methods to check consistency.

- **Eigenvalue Visualization**  
  Plots the sorted eigenvalues to analyze the data's structure.

## File Descriptions

- **`neighborhood_matrix_svd_analysis.py`**: The main script containing all the code for reading data, constructing the matrix, performing SVD, and visualizing the results.
- **`B-T-0.csv`**: Input dataset containing source and destination columns.
- **`neighborhoodMatrix.csv`**: Precomputed neighborhood matrix for efficient reuse.

## Installation and Usage

1. **Prerequisites**:
   - Python 3.x
   - Required libraries: `numpy`, `pandas`, `scipy`, `matplotlib`

   Install dependencies using pip:
   ```bash
   pip install numpy pandas scipy matplotlib
   ```

2. **Run the Script**:
   ```bash
   python neighborhood_matrix_svd_analysis.py
   ```

3. **Expected Outputs**:
   - Console output showing determinants of \( U \) and \( V \) matrices.
   - Plot of sorted eigenvalues.

## How It Works

1. **Data Preprocessing**:
   - Reads and sorts the dataset.
   - Constructs a binary neighborhood matrix representing connections between sources and destinations.

2. **SVD Computation**:
   - Computes SVD using NumPy and SciPy.
   - Manually computes SVD by deriving \( U \), \( V \), and \( S \) matrices using eigenvalue decomposition.

3. **Accuracy Check**:
   - Compares the determinants of matrices to verify consistency between different SVD methods.

4. **Visualization**:
   - Plots eigenvalues to highlight the data structure.

## Notes

- The script saves the neighborhood matrix as `neighborhoodMatrix.csv` to optimize repeated use.
- Eigenvalues from \( A^TA \) and \( AA^T \) are compared to verify the computed singular values.

