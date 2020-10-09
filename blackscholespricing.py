from math import pi
from math import log, sqrt, exp
from scipy import stats

def pricing(option, spot, K, sigma, maturity):        
    if option == "call":
        d1 = (log(spot / K) + (0 + sigma ** 2 / 2) * maturity) / (sigma * sqrt(maturity))
        d2 = (log(spot / K) + (0 - sigma ** 2  / 2) * maturity) / (sigma * sqrt(maturity))
        prob_density = 1 / sqrt(2 * pi) * exp(-d1 ** 2 * 0.5)
        price = spot * stats.norm.cdf(d1, 0.0, 1.0) - K * exp(-0 * maturity) * stats.norm.cdf(d2, 0.0, 1.0)
        delta = stats.norm.cdf(d1, 0.0, 1.0)
        gamma = (1 / sqrt(2 * pi) * exp(-d1 ** 2 / 2)) / (spot * sigma * sqrt(maturity))
        theta = (1/365) * -(spot * stats.norm.pdf(d1, 0.0, 1.0) * sigma / (2 * sqrt(maturity))) - 0 * K * exp(-0 * (maturity)) * stats.norm.cdf(d2)
        vega = (spot * stats.norm.pdf(d1, 0.0, 1.0) * sqrt(maturity)) / 100
        return price, delta, gamma, theta, vega
    
    elif option == "put":
        d1 = (log(spot / K) + (0 + sigma ** 2 / 2) * maturity) / (sigma * sqrt(maturity))
        d2 = (log(spot / K) + (0 - sigma ** 2  / 2) * maturity) / (sigma * sqrt(maturity))
        price = K * exp(-0 * maturity) * stats.norm.cdf(-d2, 0.0, 1.0) - spot * stats.norm.cdf(-d1, 0.0, 1.0)
        delta = stats.norm.cdf(d1, 0.0, 1.0) - 1
        gamma = (1 / sqrt(2 * pi) * exp(-d1 ** 2 / 2)) / (spot * sigma * sqrt(maturity))
        theta = (1/365) * (spot * stats.norm.pdf(d1) * sigma / (2 * sqrt(maturity))) + 0 * K * exp(-0 * (maturity)) * stats.norm.cdf(-d2)
        vega = (spot * stats.norm.pdf(d1, 0.0, 1.0) * sqrt(maturity)) / 100
        return price, delta, gamma, theta, vega

    else:
        print("error")
