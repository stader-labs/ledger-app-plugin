from web3 import Web3
from tests.utils import run_test, load_contract

contract = load_contract(
    "0xf03A7Eb46d01d9EcAA104558C732Cf82f6B6B645"
)

# Test from replayed transaction: https://etherscan.io/tx/0x718110ca67a3f440195c388c16a1749e0d89877817d2d3e944365855f642145d

def test_maticx_request_withdraw(backend, firmware, navigator, test_name, wallet_addr):
    data = "0x745400c9000000000000000000000000000000000000000000000045c41fde9b3d420000"
    run_test(
        contract, 
        data, 
        backend, 
        firmware, 
        navigator, 
        test_name, 
        wallet_addr
    )

