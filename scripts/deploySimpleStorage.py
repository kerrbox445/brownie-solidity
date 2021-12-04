from brownie import accounts, config, SimpleStorage, network
from scripts.utils import get_account

def deploy():
    account = get_account()
    print(f"account: {account}")
    simple_storage =SimpleStorage.deploy({'from': account}, publish_source=True)


    # value =simple_storage.retreive()
    # print(value)
    # transaction = simple_storage.store(8, {'from': account})
    # transaction.wait(1)
    # print(transaction)
    # value =simple_storage.retreive()
    # print(value)

def main():
    deploy()