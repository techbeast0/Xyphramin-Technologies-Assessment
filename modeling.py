import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
import os

os.makedirs("plots", exist_ok=True)
os.makedirs("results", exist_ok=True)

def fit_polynomial_model(X, y, degree=2):
    poly = PolynomialFeatures(degree)
    X_poly = poly.fit_transform(X)
    model = LinearRegression()
    model.fit(X_poly, y)
    y_pred = model.predict(X_poly)
    r2 = r2_score(y, y_pred)
    return model, poly, model.coef_, model.intercept_, r2

def evaluate_model(model, poly, X, y, name):
    X_poly = poly.transform(X)
    y_pred = model.predict(X_poly)
    r2 = r2_score(y, y_pred)

    plt.figure(figsize=(10, 6))
    plt.scatter(X, y, color='blue', alpha=0.3, label='Actual')
    plt.plot(X, y_pred, color='red', label='Predicted')
    plt.xlabel('Volume Delta')
    plt.ylabel('Volatility Delta')
    plt.title(f'{name} (R² = {r2:.4f})')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f"plots/{name}_fit.png")
    plt.close()
    return r2