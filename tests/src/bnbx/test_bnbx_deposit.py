from eth_typing import ChainId
from web3 import Web3
from tests.utils import run_test, load_contract

contract = load_contract(
    "0x3b961e83400d51e6e1af5c450d3c7d7b80588d28"
)

# Test from replayed transaction: https://bscscan.com/tx/0x9b712c0500b22839ce9f01952fc1d4237bf33277552ea5501f3dd8e3d419bd0f

def test_bnbx_deposit(backend, firmware, navigator, test_name, wallet_addr):
    data = "0x9ddb511a0000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000004065313663623065316333353133303164333338656661343334656531646166336631393335386363633363666161643163386264323733663736633133313561"
    run_test(
        contract, 
        data, 
        backend, 
        firmware, 
        navigator, 
        test_name, 
        wallet_addr,
        ChainId.BNB,
        value=1.065
    )

