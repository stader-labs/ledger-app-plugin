from web3 import Web3
from tests.utils import run_test, load_contract

contract = load_contract(
    "0xf03A7Eb46d01d9EcAA104558C732Cf82f6B6B645"
)

# Test from replayed transaction: https://etherscan.io/tx/0xf3c639002557eafa1560159010093927560ebbb351720c279be67bd3c480d103

def test_maticx_claim_withdrawal(backend, firmware, navigator, test_name, wallet_addr):
    data = "0xf84444360000000000000000000000000000000000000000000000000000000000000000"
    run_test(
        contract, 
        data, 
        backend, 
        firmware, 
        navigator, 
        test_name, 
        wallet_addr
    )

