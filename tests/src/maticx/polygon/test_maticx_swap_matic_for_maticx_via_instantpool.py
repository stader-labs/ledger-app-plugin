from web3 import Web3
from tests.utils import run_test, load_contract

contract = load_contract(
    "0xfd225C9e6601C9d38d8F98d8731BF59eFcF8C0E3"
)

def test_maticx_swap_matic_for_maticx_via_instantpool(backend, firmware, navigator, test_name, wallet_addr):
    data = "0xc78cf1a0"
    run_test(
        contract, 
        data, 
        backend, 
        firmware, 
        navigator, 
        test_name, 
        wallet_addr
    )

