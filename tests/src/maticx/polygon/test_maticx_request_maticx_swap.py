from web3 import Web3
from tests.utils import run_test, load_contract

contract = load_contract(
    "0xfd225C9e6601C9d38d8F98d8731BF59eFcF8C0E3"
)

def test_maticx_request_maticx_swap(backend, firmware, navigator, test_name, wallet_addr):
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

