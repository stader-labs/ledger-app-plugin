from web3 import Web3
from tests.utils import run_test, load_contract

contract = load_contract(
    "0x9F0491B32DBce587c50c4C43AB303b06478193A7"
)

# Test from replayed transaction: https://etherscan.io/tx/0x75bfb97b6f35a00f42267de655b8711d496575177e409d301b893fb8290f1b26

def test_ethx_withdraw(backend, firmware, navigator, test_name, wallet_addr):
    data = "0x1f7ec12200000000000000000000000000000000000000000000000000005af3107a40000000000000000000000000007e9bb9673ac38071a7699e6a3c48b8fbde574cd00000000000000000000000000000000000000000000000000000000000000060000000000000000000000000000000000000000000000000000000000000000a74657374696e6731323300000000000000000000000000000000000000000000"
    run_test(
        contract, 
        data, 
        backend, 
        firmware, 
        navigator, 
        test_name, 
        wallet_addr
    )

