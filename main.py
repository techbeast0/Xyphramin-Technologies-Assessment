from data_loader import datasets
from feature_engineering import compute_volatility
from modeling import fit_polynomial_model, evaluate_model
import os

with open("results/model_equations.txt", "w") as f:
    for name, df in datasets.items():
        print(f"\n===== Analyzing {name} =====")
        features = compute_volatility(df)
        X = features['Volume_delta'].values.reshape(-1, 1)
        y = features['Volatility_delta'].values

        model, poly, coefs, intercept, r2 = fit_polynomial_model(X, y)
        equation = (
            f"{name} Polynomial Model:\n"
            f"ΔV = {coefs[2]:.2e}*(ΔVolume)^2 + {coefs[1]:.2e}*(ΔVolume) + {intercept:.5f}\n"
            f"R² = {r2:.4f}\n"
            "-----------------------------\n"
        )
        print(equation)
        f.write(equation)

        evaluate_model(model, poly, X, y, name=name)