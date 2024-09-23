from eth_typing import ChainId
from web3 import Web3
from tests.utils import run_test, load_contract

contract = load_contract(
    "0x3b961e83400d51e6e1af5c450d3c7d7b80588d28"
)

# Test from replayed transaction: https://bscscan.com/tx/0x8b1657e6b4d1c508dac4d4cf882d63e0efce94dff586591ab10c8b46486bba85

def test_bnbx_request_withdraw(backend, firmware, navigator, test_name, wallet_addr):
    data = "0x0d57afa6000000000000000000000000000000000000000000000000003e819ab3f22c000000000000000000000000000000000000000000000000000000000000000040000000000000000000000000000000000000000000000000000000000000004065313663623065316333353133303164333338656661343334656531646166336631393335386363633363666161643163386264323733663736633133313561"
    run_test(
        contract, 
        data, 
        backend, 
        firmware, 
        navigator, 
        test_name, 
        wallet_addr,
        ChainId.BNB,
    )

