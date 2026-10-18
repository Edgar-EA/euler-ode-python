# Resolución de Ecuación Diferencial Separable y Método de Euler

Este repositorio contiene un script en Python que resuelve un problema de valor inicial (PVI) de forma analítica y lo compara con un método numérico (Método de Euler).

## Problema a Resolver
Se modela el crecimiento exponencial mediante la siguiente Ecuación Diferencial Ordinaria (EDO) separable:
$$\frac{dy}{dt} = y, \quad y(0) = 1$$

* **Intervalo de estudio:** $t \in [0, 1]$
* **Tamaño de paso ($h$):** $0.2$

## Solución Analítica
Aplicando el método de **separación de variables**:
1. $\frac{1}{y} \, dy = dt$
2. $\int \frac{1}{y} \, dy = \int dt \implies \ln|y| = t + C$
3. Despejando $y(t) = e^t$ (tras aplicar la condición inicial $y(0)=1$).

## Método Numérico (Euler)
El método de Euler aproxima la solución usando la pendiente en cada punto mediante la fórmula iterativa:
$$y_{n+1} = y_n + h \cdot f(t_n, y_n)$$

Para este problema específico:
$$y_{n+1} = y_n + 0.2(y_n) = 1.2 y_n$$

## Instrucciones de Ejecución
Asegúrate de tener instalado Python y ejecuta el siguiente comando en tu terminal:
```bash
python euler_separable.py
```



