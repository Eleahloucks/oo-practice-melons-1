"""Classes for melon orders."""


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
        self.species = species
        self.qty = qty
        self.shipped = False

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5
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


class InternationalMelonOrder(AbstractMelonOrder):
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
