from probo.marketdata import MarketData
from probo.payoff import ExoticPayoff, arithmeticAsianCallPayoff, arithmeticAsianPutPayoff
from probo.engine import MonteCarloEngine, NaiveMonteCarloPricer, PathwiseNaiveMonteCarloPricer
from probo.facade import OptionFacade

## Set up the market data
spot = 100.0
rate = 0.06
volatility = 0.20
dividend = 0.03
thedata = MarketData(rate, spot, volatility, dividend)

## Set up the option
expiry = 1.0
strike = 100.0
thecall = ExoticPayoff(expiry, strike, arithmeticAsianCallPayoff)
theput = ExoticPayoff(expiry, strike, arithmeticAsianPutPayoff)

## Set up Naive Monte Carlo
nreps = 10000
steps = 1
pricer = NaiveMonteCarloPricer
# pricer = PathwiseNaiveMonteCarloPricer
mcengine = MonteCarloEngine(nreps, steps, pricer)

## Calculate the price
option1 = OptionFacade(thecall, mcengine, thedata)
price1 = option1.price()
print("The call price via Naive Monte Carlo is: {0:.3f}".format(price1))




