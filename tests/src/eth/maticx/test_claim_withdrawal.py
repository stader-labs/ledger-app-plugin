from web3 import Web3
from tests.utils import run_test, load_contract

contract = load_contract(
    "0xf03a7eb46d01d9ecaa104558c732cf82f6b6b645"
)

def test_maticx_claim_withdrawal(backend, firmware, navigator, test_name, wallet_addr):
    data = "0x02f89001078459682f008505a6d71662830307bc94f03a7eb46d01d9ecaa104558c732cf82f6b6b64580a4f84444360000000000000000000000000000000000000000000000000000000000000000c080a01dae94162970e34ff707029d274c8ab57841d80d0b374f3983b63e20d095e9f5a00ade1769548658f2a1065d6b963f49627b7cc701cb6bdcc98a7940f1b6ba5f96"
    run_test(
        contract, 
        data, 
        backend, 
        firmware, 
        navigator, 
        test_name, 
        wallet_addr
    )

