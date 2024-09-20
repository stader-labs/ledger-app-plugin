from web3 import Web3
from tests.utils import run_test, load_contract

contract = load_contract(
    "0xf03A7Eb46d01d9EcAA104558C732Cf82f6B6B645"
)

def test_maticx_submit(backend, firmware, navigator, test_name, wallet_addr):
    data = "0xea99c2a60000000000000000000000000000000000000000000000481591030b2a830000"
    run_test(
        contract, 
        data, 
        backend, 
        firmware, 
        navigator, 
        test_name, 
        wallet_addr
    )

