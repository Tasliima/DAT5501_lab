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
data = pd.read_csv("wdbc.data", header=None, names=columns)

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