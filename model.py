import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Carregar os datasets CSV
df = pd.read_csv("dados2.csv", delimiter=";")  # Define ";" como separador

# Verificar valores ausentes
print(df.isnull().sum())

# Remover linhas com valores ausentes (se necessário)
df = df.dropna()

# Definir a variável-alvo (exemplo: "preco" como preço do imóvel)
y = df["preco"]

# Selecionar apenas as colunas relevantes para as features
X = df.drop(columns=["preco"]) 

# Dividir entre treino e teste (80% treino, 20% teste)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=82)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

gbr = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42)

# Treinar o modelo
gbr.fit(X_train_scaled, y_train)


y_pred = gbr.predict(X_test_scaled)

mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"MSE: {mse:.2f}")
print(f"MAE: {mae:.2f}")
print(f"R² Score: {r2:.2f}")



plt.figure(figsize=(12, 8))
sns.scatterplot(x=y_test, y=y_pred, alpha=0.6)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], "--r", linewidth=2)
plt.xlabel("Preço Real")
plt.ylabel("Preço Previsto")
plt.title("Comparação entre Preço Real e Previsto")
plt.savefig("resultado.png", dpi=300, bbox_inches="tight")
