class MarketData(object):
    """A class to encapsulate market data variables.

       Especially to be passed to pricing engines.
    """

    def __init__(self, rate, spot, volatility, dividend):
        self.__rate = rate
        self.__spot = spot
        self.__volatility = volatility
        self.__dividend = dividend

    @property
    def rate(self):
        return self.__rate

    @rate.setter
    def rate(self, new_rate):
        self.__rate = new_rate

    @property
    def spot(self):
        return self.__spot

    @spot.setter
    def spot(self, new_spot):
        self.__spot = new_spot

    @property
    def volatility(self):
        return self.__volatility

    @volatility.setter
    def volatility(self, new_volatility):
        self.__volatility = new_olatility

    @property
    def dividend(self):
        return self.__dividend

    @dividend.setter
    def dividend(self, new_yield):
        self.__dividend = new_yield
        
    def get_data(self):
        return (self.__spot, self.__rate, self.__volatility, self.__dividend)
    
