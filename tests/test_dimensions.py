from datetime import date
from models.dimensions import Account, AccountingPeriod, BusinessUnit, Currency, Dimension, Driver, Scenario


def test_base_dimension():
    dim = Dimension()
    dim.id = 'PARENT'
    dim.description = 'Parent Dimension member'
    dim.parent_id = None

    dim = Dimension()
    dim.id = 'CHILD'
    dim.description = 'Child Dimension member'
    dim.parent_id = 'PARENT'


def test_account():
    account = Account()
    account.id = '100000'
    account.description = 'Cash & Banks'
    account.type = 'asset'


def test_accounting_period():
    accounting_period = AccountingPeriod()

    # Day granularity
    accounting_period.id = '19991231'
    accounting_period.date = date(1999, 12, 31)
    accounting_period.day = 31
    accounting_period.month = 12
    accounting_period.quarter = 4
    accounting_period.year = 1999


def test_business_unit():
    business_unit = BusinessUnit()
    business_unit.id = 'NORTH'
    business_unit.local_currency = 'MXN'


def test_currency():
    currency = Currency()
    currency.id = 'USD'


def test_driver():
    driver = Driver()
    driver.id = 'SALES_VOLUME'


def test_scenario():
    scenario = Scenario()
    scenario.id = 'ACTUAL'
