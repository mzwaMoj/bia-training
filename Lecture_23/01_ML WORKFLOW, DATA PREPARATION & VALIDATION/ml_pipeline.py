from pathlib import Path

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


DATA_PATH = (
    Path(__file__).resolve().parent
    / "01_ML WORKFLOW, DATA PREPARATION & VALIDATION"
    / "S18_Housing_Study.csv"
)
TARGET = "price"
PREDICTIONS_PATH = Path(__file__).resolve().parent / "housing_test_predictions.csv"


def main():
    if not DATA_PATH.exists():
        raise FileNotFoundError(f"Dataset not found: {DATA_PATH}")

    df = pd.read_csv(DATA_PATH)

    # Basic cleanup
    df.columns = df.columns.str.strip()
    for column in df.select_dtypes(include="object").columns:
        df[column] = df[column].map(
            lambda value: value.strip() if isinstance(value, str) else value
        )
    df = df.drop_duplicates()

    if TARGET not in df.columns:
        raise ValueError(f"Target column '{TARGET}' not found. Columns: {df.columns.tolist()}")

    # Ensure the target is numeric and remove rows where it is missing or invalid.
    df[TARGET] = pd.to_numeric(df[TARGET], errors="coerce")
    df = df.dropna(subset=[TARGET])
    df = df.drop(columns=["price_per_area_at_sale", "record_id"])

    X = df.drop(columns=TARGET)
    y = df[TARGET]

    if X.empty:
        raise ValueError("No feature columns remain after removing the target.")

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    numeric_cols = X_train.select_dtypes(include="number").columns
    categorical_cols = X_train.select_dtypes(exclude="number").columns

    numeric_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler()),
    ])
    categorical_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encoder", OneHotEncoder(handle_unknown="ignore")),
    ])

    preprocessor = ColumnTransformer([
        ("numeric", numeric_pipeline, numeric_cols),
        ("categorical", categorical_pipeline, categorical_cols),
    ])

    model = Pipeline([
        ("preprocessor", preprocessor),
        ("regressor", LinearRegression()),
    ])

    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    print(f"Mean Squared Error: {mean_squared_error(y_test, predictions):.2f}")
    print(f"R2 Score: {r2_score(y_test, predictions):.2f}")
    print(f"Mean Absolute Error: {mean_absolute_error(y_test, predictions):.2f}")

    results = pd.DataFrame({
        "actual_price": y_test,
        "predicted_price": predictions,
    })
    results.to_csv(PREDICTIONS_PATH, index=False)
    print(f"Test predictions saved to: {PREDICTIONS_PATH}")


if __name__ == "__main__":
    main()