from probo.marketdata import MarketData
from probo.payoff import VanillaPayoff, call_payoff, put_payoff
from probo.engine import AsianMonteCarloEngine, NaiveMonteCarloPricer, AsianControlVariatePricerCall, NaiveAsianCall
from probo.facade import OptionFacade

## Set up the market data
spot = 100
rate = 0.06
volatility = 0.2
dividend = 0.03
thedata = MarketData(rate, spot, volatility, dividend)

## Set up the option
expiry = 1.0
strike = 100
thecall = VanillaPayoff(expiry, strike, call_payoff)
theput = VanillaPayoff(expiry, strike, put_payoff)

## Set up Naive Monte Carlo
nreps = 10000
steps = 10
pricer = AsianControlVariatePricerCall
mcengine = AsianMonteCarloEngine(nreps, steps, pricer)

## Calculate the price
option1 = OptionFacade(thecall, mcengine, thedata)
price1,se = option1.price()
#price2,se = option1.price()
#print("The Price of an Asian Call is: {0:.3f} and the Standard Error is {0:5f}".format(price1), .format(se))

option2 = OptionFacade(thecall, mcengine, thedata)
## Only works for calls
#option2 = OptionFacade(theput, mcengine, thedata)
#price2 = option2.price()
#print("The put price via Naive Monte Carlo is: {0:.3f}".format(price2))

print("The European Arithmetic Asian Call Option with Geometric Control Variate Price is: {0:.3f}".format(price1))
print("The European Arithmetic Asian Call Option with Geometric Control Variate StdErr is: {0:.6f}".format(se))
