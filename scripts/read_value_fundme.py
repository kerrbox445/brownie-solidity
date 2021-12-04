from brownie import accounts, config, FundMe, network
from scripts.utils import get_account


def fund():
    account = get_account()
    print(f"account: {account}")

    fund_me = FundMe[-1]
    fund_me.fund({"from": account, "value": 100000000000000000})


def withdraw():
    account = get_account()
    print(f"account: {account}")

    fund_me = FundMe[-1]
    fund_me.withdraw({"from": account})


def main():
    fund()