"""Classes for melon orders."""
#for Further study part 1 import random function
from random import randint
from datetime import datetime




class AbstractMelonOrder:
    """An abstract base class that other Melon Orders inherit from."""

    order_type = None
    tax = 0



    # every time an instance of the Abstract class is created,
    # user must pass in melon species and quantity. Default
    # value of shipped is False because order has only been
    # created
    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        if qty > 100:
            raise TooManyMelonsError()


        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_time = datetime.now()

    #further study p1
    #create base price function for splurge pricing
    def get_base_price(self):
        """ choosing a random integer between 5-9 as the base price. """
        #base price generated a random number between 5-9 inclusively
        base_price = randint(5, 9)
        #date.weekday() Return the day of the week as an integer, where Monday is 0 and Sunday is 6.
        #
        # date.isoweekday() Return the day of the week as an integer, where Monday is 1 and Sunday is 7.
        if self.order_time.weekday() != 5 or self.order_time.weekday() != 6:
            if self.order_time.hour >= 8 and self.order_time.hour <= 11:
                base_price += 4

        return base_price


    def get_total(self, base_price):
        """Calculate price, including tax."""

        # instead of creating a total variable set to 0 on line 24,
        # I thought it made more sense to define the total variable
        # after conditional logic that calculates changes to base price
        if self.species == "Christmas melon".casefold():
            base_price = base_price * 1.5

        total = (1 + self.tax) * self.qty * base_price

        if self.order_type == "international" and self.qty < 10:
            total += 3

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""
        # once this method is called on an instance of the Abstract Class
        # (or any class that has interited the Abstract, the shipped attribute
        # will change from default value of False to True)
        self.shipped = True

class TooManyMelonsError(ValueError):
    """Raise error when > 100 melons ordered """
    def __init__(self):
        super().__init__("Cannot order more than 100 melons")



class GovernmentMelonOrder(AbstractMelonOrder):
    """Melons purchased by US Govt."""

    order_type = "government"
    tax = 0
    # government orders are handled differently. This class
    # inherits attributes from Abstract class (super class),
    # including species and quantity.
    # government melons are required to pass a safety inspection.
    # the default value of the passed_inspection attribute is False
    # until the mark_inspection method is called on a created instance
    # of a GovermentMelonOrder.
    def __init__(self, species, qty):
        super().__init__(species, qty)
        self.passed_inspection = False

    def mark_inspection(self, passed):
        """Record whether or not melon order passed inspection"""

        self.passed_inspection = passed


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    order_type = "domestic"
    tax = 0.08


class InternationalMelonOrder (AbstractMelonOrder):
    """An international (non-US) melon order."""

    order_type = "international"
    tax = 0.17
    # this class is inheriting from the Abstract class.
    # once an instance of this class has been created,
    # the species and qty are inherited, and the user
    # is asked to input the country code and species if
    # there is nothing to inherit). The country code for
    # international orders can be checked by calling the
    # get_country_code method on created instances of
    # InternationalMelonOrder class.
    def __init__(self, species, qty, country_code):
        super().__init__(species, qty)
        self.country_code = country_code
        self.species = species

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

order0 = InternationalMelonOrder("watermelon", 101, "AUS")