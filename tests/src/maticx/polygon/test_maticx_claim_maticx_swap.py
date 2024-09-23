from eth_typing import ChainId
from web3 import Web3
from tests.utils import run_test, load_contract

contract = load_contract(
    "0xfd225C9e6601C9d38d8F98d8731BF59eFcF8C0E3"
)

# Test from replayed transaction: https://polygonscan.com/tx/0xe26214e3577874118e16ce1a605a9ad06b0836c0507e2071ddc3b4bac795b2a0

def test_maticx_claim_maticx_swap(backend, firmware, navigator, test_name, wallet_addr):
    data = "0x77baf2090000000000000000000000000000000000000000000000000000000000000000"
    run_test(
        contract, 
        data, 
        backend, 
        firmware, 
        navigator, 
        test_name, 
        wallet_addr,
        ChainId.MATIC
    )

