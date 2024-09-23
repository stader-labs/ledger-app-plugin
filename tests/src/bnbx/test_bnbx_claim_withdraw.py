from eth_typing import ChainId
from web3 import Web3
from tests.utils import run_test, load_contract

contract = load_contract(
    "0x3b961e83400d51e6e1af5c450d3c7d7b80588d28"
)

# Test from replayed transaction: https://testnet.bscscan.com/tx/0x4933296ae725dbdd0e1a093fdf508f88ad22c9ae315282eccccda148405c9856

def test_bnbx_claim_withdraw(backend, firmware, navigator, test_name, wallet_addr):
    data = "0xf84444360000000000000000000000000000000000000000000000000000000000000000"
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

