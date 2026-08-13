import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import precision_score, recall_score, f1_score

# Column names from the UCI dataset
columns = [
    "id", "diagnosis",
    "radius_mean", "texture_mean", "perimeter_mean", "area_mean",
    "smoothness_mean", "compactness_mean", "concavity_mean",
    "concave_points_mean", "symmetry_mean", "fractal_dimension_mean",
    "radius_se", "texture_se", "perimeter_se", "area_se",
    "smoothness_se", "compactness_se", "concavity_se",
    "concave_points_se", "symmetry_se", "fractal_dimension_se",
    "radius_worst", "texture_worst", "perimeter_worst", "area_worst",
    "smoothness_worst", "compactness_worst", "concavity_worst",
    "concave_points_worst", "symmetry_worst", "fractal_dimension_worst"
]

# Load dataset
data = pd.read_csv("06_decision_tree/wdbc.data", header=None, names=columns)

# Separate features and target
X = data.drop(columns=["id", "diagnosis"])
y = data["diagnosis"]

# Convert diagnosis to numerical values
# Malignant = 1, Benign = 0
y = y.map({"M": 1, "B": 0})

# Split into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Test different tree depths
depths = range(1, 11)

precision_scores = []
recall_scores = []
f1_scores = []

print("Decision Tree Optimisation")
print("--------------------------")

for depth in depths:

    model = DecisionTreeClassifier(
        max_depth=depth,
        random_state=42
    )

    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)

    precision_scores.append(precision)
    recall_scores.append(recall)
    f1_scores.append(f1)

    print(
        f"Depth {depth}: "
        f"Precision = {precision:.3f}, "
        f"Recall = {recall:.3f}, "
        f"F1 = {f1:.3f}"
    )

# Find the depth with the highest F1 score
best_index = f1_scores.index(max(f1_scores))
best_depth = list(depths)[best_index]

print()
print(f"Best depth based on F1 score: {best_depth}")
print(f"Best F1 score: {f1_scores[best_index]:.3f}")

# Plot Precision, Recall and F1 against tree depth
plt.figure(figsize=(10, 6))

plt.plot(depths, precision_scores, marker="o", label="Precision")
plt.plot(depths, recall_scores, marker="o", label="Recall")
plt.plot(depths, f1_scores, marker="o", label="F1 score")

plt.xlabel("Decision Tree Depth")
plt.ylabel("Score")
plt.title("Decision Tree Performance vs Depth")
plt.xticks(list(depths))
plt.ylim(0, 1.05)
plt.legend()
plt.grid(True)

plt.savefig("decision_tree_depth.png")
plt.show()

# Train the best model
best_model = DecisionTreeClassifier(
    max_depth=best_depth,
    random_state=42
)

best_model.fit(X_train, y_train)

# Calculate feature importance
feature_importance = pd.Series(
    best_model.feature_importances_,
    index=X.columns
).sort_values(ascending=False)

print()
print("Most Important Features")
print("-----------------------")

for feature, importance in feature_importance.head(10).items():
    print(f"{feature}: {importance:.4f}")

# Plot the top 10 important features
plt.figure(figsize=(10, 6))

feature_importance.head(10).sort_values().plot(kind="barh")

plt.xlabel("Feature Importance")
plt.ylabel("Feature")
plt.title("Top 10 Most Important Features")

plt.tight_layout()
plt.savefig("decision_tree_feature_importance.png")
plt.show()

from sklearn.model_selection import cross_val_score
from sklearn.metrics import roc_curve, roc_auc_score

# ---------------------------------------------------------
# DECISION TREE VALIDATION
# ---------------------------------------------------------

print()
print("Decision Tree Validation")
print("------------------------")

# Use the optimised model from the previous activity
validation_model = DecisionTreeClassifier(
    max_depth=best_depth,
    random_state=42
)

validation_model.fit(X_train, y_train)

# ---------------------------------------------------------
# ROC CURVE
# ---------------------------------------------------------

# Get predicted probabilities for the malignant class
y_prob = validation_model.predict_proba(X_test)[:, 1]

# Calculate ROC curve
fpr, tpr, thresholds = roc_curve(y_test, y_prob)

# Calculate Area Under the Curve
auc = roc_auc_score(y_test, y_prob)

print(f"ROC AUC: {auc:.3f}")

# Plot ROC curve
plt.figure(figsize=(8, 6))

plt.plot(
    fpr,
    tpr,
    label=f"Decision Tree (AUC = {auc:.3f})"
)

plt.plot(
    [0, 1],
    [0, 1],
    linestyle="--",
    label="Random classifier"
)

plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve")
plt.legend()
plt.grid(True)

plt.savefig("decision_tree_roc.png")
plt.show()

# ---------------------------------------------------------
# CROSS-VALIDATION
# ---------------------------------------------------------

cv_scores = cross_val_score(
    validation_model,
    X,
    y,
    cv=5,
    scoring="f1"
)

print()
print("5-Fold Cross-Validation")
print("-----------------------")

for i, score in enumerate(cv_scores, start=1):
    print(f"Fold {i}: F1 = {score:.3f}")

print(f"Mean F1: {cv_scores.mean():.3f}")
print(f"Standard deviation: {cv_scores.std():.3f}")

# ---------------------------------------------------------
# OBSERVED AND DERIVED VARIABLES
# ---------------------------------------------------------

print()
print("Observed and Derived Variables")
print("------------------------------")

# The WDBC dataset contains observed measurements such as
# radius, perimeter and area. We create a derived feature
# representing overall tumour size using three observed
# measurements.

data["tumour_size_proxy"] = (
    data["radius_worst"]
    + data["perimeter_worst"]
    + data["area_worst"]
)

# Create features including the new derived variable
X_derived = data.drop(columns=["id", "diagnosis"])

# Recreate the target
y_derived = data["diagnosis"].map({"M": 1, "B": 0})

# Split the data using the same settings as before
X_train_derived, X_test_derived, y_train_derived, y_test_derived = train_test_split(
    X_derived,
    y_derived,
    test_size=0.2,
    random_state=42,
    stratify=y_derived
)

# Train the optimised decision tree with the derived feature
derived_model = DecisionTreeClassifier(
    max_depth=best_depth,
    random_state=42
)

derived_model.fit(X_train_derived, y_train_derived)

# Make predictions
y_pred_derived = derived_model.predict(X_test_derived)

# Calculate performance
derived_precision = precision_score(
    y_test_derived,
    y_pred_derived
)

derived_recall = recall_score(
    y_test_derived,
    y_pred_derived
)

derived_f1 = f1_score(
    y_test_derived,
    y_pred_derived
)

print("Model including derived feature")
print(f"Precision: {derived_precision:.3f}")
print(f"Recall:    {derived_recall:.3f}")
print(f"F1 score:  {derived_f1:.3f}")

print()
print("Comparison with original model")
print(f"Original F1: {f1_scores[best_index]:.3f}")
print(f"Derived F1:  {derived_f1:.3f}")

improvement = derived_f1 - f1_scores[best_index]

print(f"F1 improvement: {improvement:+.3f}")