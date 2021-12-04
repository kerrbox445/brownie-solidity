from brownie import accounts, config, SimpleStorage, network
from scripts.utils import get_account


def read_value():
    account = get_account()
    print(f"account: {account}")
    simple_storage = SimpleStorage[-1]

    value =simple_storage.retreive()
    print(value)
    transaction = simple_storage.store(445, {'from': account})
    transaction.wait(1)
    value =simple_storage.retreive()
    print(value)


def main():
    read_value()