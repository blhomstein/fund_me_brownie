from scripts.helpfulScripts import get_account, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from scripts.deploy import deploy_fund
from brownie import network, accounts, exceptions
import pytest


def test_can_fun_withdraw():
    account = get_account()
    fundme = deploy_fund()
    print(fundme)
    entrance_fee = fundme.GetEntrancefee() + 109

    tx = fundme.fund({"from": account, "value": entrance_fee})
    tx.wait(1)

    assert fundme.addressToAmountFunded(account.address) == entrance_fee

    tx2 = fundme.withdraw({"from": account})
    tx2.wait(1)

    assert fundme.addressToAmountFunded(account.address) == 0


def test_only():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("we cant test outside local env")
    fundme = deploy_fund()
    bad = accounts.add()
    with pytest.raises(exceptions.VirtualMachineError):
        fundme.withdraw({"from": bad})
