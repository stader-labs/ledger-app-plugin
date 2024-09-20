from web3 import Web3
from tests.utils import run_test, load_contract

contract = load_contract(
    "0xfd225c9e6601c9d38d8f98d8731bf59efcf8c0e3"
)

def test_polygon_request_maticx_swap(backend, firmware, navigator, test_name, wallet_addr):
    data = "0x48eaf6d600000000000000000000000000000000000000000000000792da134a3d0c8000"
    run_test(
        contract, 
        data, 
        backend, 
        firmware, 
        navigator, 
        test_name, 
        wallet_addr
    )

