# I used jupyter notebook for deploying the algorithm part by part at the end I copied everything here #


############################## FIRST PART OF CODE #################################

import pandas as pd
import numpy as np
from numpy import genfromtxt
from scipy.linalg import svd as scipy_svd
import matplotlib.pyplot as plt

# I manually changed the data set to csv format
# Reading the data set file
df = pd.read_csv('B-T-0.csv')
# Sort the columns Just for fun
df = df.sort_values(by=['Source'])
# Reindex the indices
df = df.reset_index(drop=True)
# print(df)


# Finding distinct values
distinctList = []
for i in df['Source']:
    if i not in distinctList:
        distinctList.append(i)

# print(distinctList)

# A zero matrix in size of distinct values initialized
neighborhoodMatrix = np.zeros((len(distinctList), len(distinctList)))

# Loop over distinct values
for i in range(len(distinctList)):
    firstItem = distinctList[i]
    # Loop over distinct values
    for j in range(len(distinctList)):
        secondItem = distinctList[j]
        # Loop over the data set
        for r in range(len(df)):
            # Check the conditions /// conditions shows having connection
            if df['Source'][r] == firstItem and df['Destination'][r] == secondItem:
                # If the condition is true change the neighborhood matrix value with indices to one
                neighborhoodMatrix[i, j] = 1
                # To prevent long loops because after first condition we don't need to continue the loop we will break it here
                break
            
# Because making neighborhood matrix takes too much time after running for first time I saved neighborhood matrix into a csv file for further use.
np.savetxt('neighborhoodMatrix.csv', neighborhoodMatrix, delimiter=',')


############################## SECOND PART OF CODE #################################

# Reading the csv file that contains neighborhood matrix
matrixA = genfromtxt('neighborhoodMatrix.csv', delimiter=',').astype(int)

# Implementing the SVD algorithm made by Numpy module
u, s, vh = np.linalg.svd(matrixA)
# To see how accurate it is
# I checked the determinants
print('SVD Numpy')
print('*' * 40)
print(f'determinant for U matrix = {round(np.linalg.det(u))}')
print('-' * 40)
print(f'determinant for V matrix = {round(np.linalg.det(vh))}')
print('*' * 40)

# Implementing the SVD algorithm made by Scipy module
u, s, vh = scipy_svd(matrixA)
# To see how accurate it is
# I checked the determinants
print('SVD Scipy')
print('*' * 40)
print(f'determinant for U matrix = {round(np.linalg.det(u))}')
print('-' * 40)
print(f'determinant for V matrix = {round(np.linalg.det(vh))}')
print('*' * 40)


############################## SECOND PART OF CODE #################################

# I use matrixA that I read it from a file in part two in this part too.

# To compute the V
# First compute the dot production of transposed A and A itself.
ATA = np.dot(matrixA.T, matrixA)

# Finding the eigenvalue and eigenvector For the matrix that we get as ATA 
eigValues1, eigVectors1 = np.linalg.eig(ATA)

# With formula that we read in class we can Compute V
V = eigVectors1

# To compute the U
# First compute the dot production of A itself and transposed A.
AAT = np.dot(matrixA, matrixA.T)

# Finding the eigenvalue and eigenvector For the matrix that we get as AAT 
eigValues2, eigVectors2 = np.linalg.eig(AAT)

# With formula that I found online we can Compute U
U = eigVectors2


# To see how accurate is our algorithm
# We checked the determinants
print('SVD by me')
print('*' * 40)
print(f'determinant for U matrix = {round(np.linalg.det(U))}')
print('-' * 40)
print(f'determinant for V matrix = {round(np.linalg.det(V))}')
print('*' * 40)


# To compute S we can use Both eigenvalues but we will show below that they are completely equal.
S1 = eigValues1
S2 = eigValues2

# To show they are the equal
eigChecker = np.equal(S1, S2).all()
if eigChecker:
    print('Sigma matrix for both ATA and AAT are same.')
else:
    print('Sigma matrix for both ATA and AAT are different.')


# Making a list for X values in plot
xV = [x for x in range(len(S1))]

# Sorting the S1
sList = list(S1)
# Sort in reverse way
sList.sort(reverse=True)

# Plot the eigenvalues
plt.plot(xV, sList, color='red', linewidth='2.0')
plt.show()