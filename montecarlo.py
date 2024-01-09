import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def simulate_brownian_motion(starting_price, expected_return, vol, timestep):
    z = np.random.normal()
    price = starting_price * math.exp((expected_return - 0.5 * vol ** 2) * timestep + vol * z * math.sqrt(timestep))
    return price

def simulate_asset_path(steps, starting_price, expected_return, vol, timestep):
    simulated_path = [starting_price]
    price = starting_price
    for step in range(steps):
        price = simulate_brownian_motion(price, expected_return, vol, timestep)
        simulated_path.append(price)
    return simulated_path

def simulate_multiple_paths(paths, steps, starting_price, expected_return, vol, timestep):
    multiple_paths = []
    for path in range(paths):
        path = simulate_asset_path(steps, starting_price, expected_return, vol, timestep)
        multiple_paths.append(path)
    return pd.DataFrame(multiple_paths).T  # Transpose so each path is a column

def monte_carlo_pricing(derivative, paths, steps, r, strike, starting_price, vol, timestep):
    df = simulate_multiple_paths(paths, steps, starting_price, r, vol, timestep)
    
    if derivative == "call":
        payoffs = np.maximum(df.iloc[-1, :] - strike, 0)
        discounted_payoffs = payoffs * math.exp(-r * steps * timestep)
        expected_payoff = np.mean(discounted_payoffs)
        return expected_payoff, discounted_payoffs, payoffs, df
    
    elif derivative == "put":
        payoffs = np.maximum(strike - df.iloc[-1, :], 0)
        discounted_payoffs = payoffs * math.exp(-r * steps * timestep)
        expected_payoff = np.mean(discounted_payoffs)
        return expected_payoff, discounted_payoffs, payoffs, df

# Simulate brownian motion
price = simulate_brownian_motion(100, 0.04, 0.2, 0.25)
print(price)

# Simulate asset path
gbm = simulate_asset_path(2, 100, 0.04, 0.2, 0.25)
# plotting
plt.plot(gbm)
plt.title("Simulated Asset Path")
plt.xlabel("Step")
plt.ylabel("Price")
plt.show()

# Simulate multiple paths
stock_paths = simulate_multiple_paths(100, 8, 100, 0.1, 0.2, 0.25)
# plotting
for column in stock_paths.columns:
    plt.plot(stock_paths[column], label=f'Path {column+1}')
plt.title("Simulated Multiple Asset Paths")
plt.xlabel("Step")
plt.ylabel("Price")
plt.show()

# Monte Carlo pricing
option_price = monte_carlo_pricing("call", 1000000, 2, 0.04, 150, 140, 0.25, 0.25)
print(option_price[0])