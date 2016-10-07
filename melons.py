"""This file should have our order classes in it."""
from random import choice
from datetime import datetime

class TooManyMelonsError(ValueError):
    pass

class AbstractMelonOrder(object):
    """combines common methods between DomesticMelonOrder and International Orders"""
    def __init__(self, species, qty, order_type, tax, country_code=None):
        """Initializes general melon order attributes"""

        if qty > 100:
            raise TooManyMelonsError, 'No more than 100 melons!'

        self.species = species
        self.shipped = False
        self.country_code = country_code
        self.order_type = order_type
        self.tax = tax
        self.order_day = datetime.today().weekday()
        self.order_hour = datetime.today().hour

    def get_base_price(self):
        """Gets random base price"""

        base_price = choice([5, 6, 7, 8, 9])
        if self.order_day in [0, 1, 2, 3, 4] and self.order_hour in [8, 9, 10]:
            base_price = base_price + 4
        return base_price

    
    def get_total(self):
        """Calculate price."""

        base_price = get_base_price()
        if self.species.lower() == "christmas":
            base_price = base_price * 1.5
        total = (1 + self.tax) * self.qty * base_price
        return total


    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""

    def __init__(self, species, qty):
        """Initialize melon order attributes"""
        super(DomesticMelonOrder, self).__init__(species, qty, "domestic", 0.08)


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes"""

        super(InternationalMelonOrder, self).__init__(species, qty, "international", 0.17, country_code)
    
    
    def get_total(self):
        """Updates parent get_total to add $3 if less than 10 melons ordered"""

        total = super(InternationalMelonOrder, self).get_total()

        if self.qty < 10:
            total = total + 3

        return total
    

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

class GovernmentMelonOrder(AbstractMelonOrder):
    """A U.S. government melon order"""

    def __init__(self, species, qty):
        """Initialize melon order attributes"""

        super(GovernmentMelonOrder, self).__init__
        (species, qty, "domestic", 0)

        self.passed_inspection = False


    def mark_inspection(self, passed):
        """ Updates passed inspection attribute """

        # user_input = raw_input("Did the inspection pass? [Enter True or False] > ")
        if passed is True:
            self.passed_inspection = passed

        elif passed is not False:
            print "Input was not True or False. Try mark_inspection() again."
        else:
            self.passed_inspection = False