import numpy as np

# Create image matrix
img = np.array([[10, 20, 30, 40],
                [50, 60, 70, 80],
                [90, 100, 110, 120],
                [130, 140, 150, 160]])

print("Original Image:")
print(img)

# Reshape image
reshaped = img.reshape(2, 8)
print("Reshaped Image:")
print(reshaped)

# Slice a region
region = img[0:2, 0:2]
print("Selected Region:")
print(region)

# Brightness adjustment using broadcasting
bright = np.clip(img + 30, 0, 255)
print("Brightness Adjusted Image:")
print(bright)

# Matrix multiplication for transformation
matrix = np.array([[1, 0],
                   [0, 1]])

result = np.dot(region, matrix)
print("Transformed Region:")
print(result)