import random

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad


def integral_plot(f, a, b):
    # Creating a range of values for x
    x = np.linspace(-0.5, 2.5, 400)
    y = f(x)

    # Creating a schedule
    fig, ax = plt.subplots()

    # Drawing a function
    ax.plot(x, y, "r", linewidth=2)

    # Filling the area under the curve
    ix = np.linspace(a, b)
    iy = f(ix)
    ax.fill_between(ix, iy, color="gray", alpha=0.3)

    # Customize the schedule
    ax.set_xlim([x[0], x[-1]])
    ax.set_ylim([0, max(y) + 0.1])
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")

    # Add integration boundaries and a graph title
    ax.axvline(x=a, color="gray", linestyle="--")
    ax.axvline(x=b, color="gray", linestyle="--")
    ax.set_title("Графік інтегрування f(x) = x^2 від " + str(a) + " до " + str(b))
    plt.grid()
    plt.show()


def monte_carlo_integral(a, b, num_samples=1000):
    sum_values = 0

    for _ in range(num_samples):
        x = random.uniform(a, b)
        sum_values += f(x)

    average = sum_values / num_samples
    integral_approximation = (b - a) * average

    return integral_approximation


if __name__ == "__main__":

    def f(x):
        return x**2

    a = 0  # Lower limit
    b = 2  # Upper limit

    # Monte Carlo solution
    mc_result_1 = monte_carlo_integral(a, b, 1000)
    mc_result_2 = monte_carlo_integral(a, b, 10000)
    print(
        f"Finding the value of an integral by the Monte Carlo method: \n 1000 samples - {mc_result_1:.8f}"
    )
    print(
        f"Finding the value of an integral by the Monte Carlo method: \n 10000 samples - {mc_result_2:.8f}"
    )

    quad_result, error = quad(f, a, b)
    print(f"\nChecking calculations: {quad_result:.8f}")

    integral_plot(f, a, b)
