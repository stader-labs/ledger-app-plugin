from web3 import Web3
from tests.utils import run_test, load_contract

contract = load_contract(
    "0xcf5EA1b38380f6aF39068375516Daf40Ed70D299"
)

# Test from replayed transaction: https://etherscan.io/tx/0x0879b63722348980a8d2e5118d33adfa0789c81c687f0d4d8b75276247c9299f

def test_ethx_deposit(backend, firmware, navigator, test_name, wallet_addr):
    data = "0xb74825090000000000000000000000007e9bb9673ac38071a7699e6a3c48b8fbde574cd00000000000000000000000000000000000000000000000000000000000000040000000000000000000000000000000000000000000000000000000000000000a74657374696e6731323300000000000000000000000000000000000000000000"
    run_test(
        contract, 
        data, 
        backend, 
        firmware, 
        navigator, 
        test_name, 
        wallet_addr,
        value=0.0001
    )

