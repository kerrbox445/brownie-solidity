from brownie import accounts, config, FundMe, network, MockV3Aggregator
from scripts.utils import get_account, deploy_price_feed_mock




def deploy():
    account = get_account()
    print(f"account: {account}")
    price_feed = deploy_price_feed_mock()
    fund_me = FundMe.deploy(price_feed, {'from': account})


def main():
    deploy()