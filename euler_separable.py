import math


def f(t, y):
  """Define la función f(t, y) de la EDO dy/dt = y"""
  return y


def metodo_euler(t0, tf, h, y0):
  """Aplica el método de Euler para aproximar la solución de la EDO."""
  t_vals = [t0]
  y_vals = [y0]

  t = t0
  y = y0

  # Iterar desde t0 hasta tf con paso h
  while t < tf - 1e-9:
    y = y + h * f(t, y)
    t = t + h
    t_vals.append(round(t, 2))
    y_vals.append(y)

  return t_vals, y_vals


def main():
  # Parámetros dados
  t0 = 0.0
  tf = 1.0
  h = 0.2
  y0 = 1.0

  # Calcular aproximación con el método de Euler
  tiempos, y_aprox = metodo_euler(t0, tf, h, y0)

  print("--- COMPARACIÓN: MÉTODO DE EULER VS SOLUCIÓN EXACTA ---")
  print(f"{'t':<10} {'Euler (Aprox)':<18} {'Exacta (e^t)':<18} {'Error Absoluto':<15}")
  print("-" * 62)

  for t, y_a in zip(tiempos, y_aprox):
    y_ex = math.exp(t)
    error = abs(y_ex - y_a)
    print(f"{t:<10.1f} {y_a:<18.4f} {y_ex:<18.4f} {error:<15.4f}")


if __name__ == "__main__":
  main()
