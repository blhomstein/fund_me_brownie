from brownie import FundMe

from scripts.helpfulScripts import get_account


def fund():
    fund_me = FundMe[-1]
    account = get_account()
    get_entrance = fund_me.GetEntrancefee()
    print(f"the current entrance fee is {get_entrance}")
    print("Funding....")
    fund_me.fund({"from": account, "value": get_entrance})
    print("funded")


def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    print("withdrawing......")
    fund_me.withdraw({"from": account})
    print("withdrawed")


def main():
    fund()
    withdraw()
