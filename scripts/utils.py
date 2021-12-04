from brownie import accounts, network, config, MockV3Aggregator

def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config['wallets']['from_key'])


def deploy_price_feed_mock():
    if network.show_active() == "development":
        if len(MockV3Aggregator) > 0:
            price_feed = MockV3Aggregator[-1].address
        else:
            MockV3Aggregator.deploy(48, 2000000000000000000, {'from': get_account()})
            price_feed = MockV3Aggregator[-1].address
    else:
        price_feed = config['networks'][network.show_active()]['chainlink_price_feed']
    return price_feed