import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC

# Training data
X = [[1, 2], [2, 3], [3, 4], [4, 5]]
y = [0, 0, 1, 1]

# Fit the model
clf = SVC(kernel='linear')
clf.fit(X, y)

# Get the coefficients of the decision boundary (slope and intercept)
coef = clf.coef_[0]
intercept = clf.intercept_[0]

# Plot the data points
plt.scatter([x[0] for x in X], [x[1] for x in X], c=y, cmap='winter', marker='o', s=100)

# Create the decision boundary line (y = mx + b)
xx = np.linspace(0, 5, 100)
yy = -(coef[0] * xx + intercept) / coef[1]

# Plot the decision boundary
plt.plot(xx, yy, 'k-', label='Decision Boundary')

# Calculate and plot the margin lines
margin_width = 2 * abs(clf.decision_function([[3, 3]]))  # You can adjust this based on distance
yy_margin_upper = yy + margin_width / 2
yy_margin_lower = yy - margin_width / 2
plt.plot(xx, yy_margin_upper, 'r--', label='Margin (upper)')
plt.plot(xx, yy_margin_lower, 'r--', label='Margin (lower)')

# Plot support vectors
plt.scatter(clf.support_vectors_[:, 0], clf.support_vectors_[:, 1], facecolors='none', edgecolors='r', s=150, label='Support Vectors')

# Labels and title
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('SVM Decision Boundary and Margins')
plt.legend()

plt.show()
