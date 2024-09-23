from web3 import Web3
from tests.utils import run_test, load_contract

contract = load_contract(
    "0x9F0491B32DBce587c50c4C43AB303b06478193A7"
)

# Test from replayed transaction: https://etherscan.io/tx/0x6a9c6ec076057ece2cd2201376e889fd58aed440ced33b769e78f86d0043a9a5

def test_ethx_claim(backend, firmware, navigator, test_name, wallet_addr):
    data = "0x379607f50000000000000000000000000000000000000000000000000000000000000042"
    run_test(
        contract, 
        data, 
        backend, 
        firmware, 
        navigator, 
        test_name, 
        wallet_addr
    )

