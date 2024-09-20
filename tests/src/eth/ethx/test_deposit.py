from web3 import Web3
from tests.utils import run_test, load_contract

contract = load_contract(
    "0xcf5ea1b38380f6af39068375516daf40ed70d299"
)

def test_ethx_deposit(backend, firmware, navigator, test_name, wallet_addr):
    data = "0x02f8f701248405f5e1008501fa14a6d7830329eb94cf5ea1b38380f6af39068375516daf40ed70d299865af3107a4000b884b74825090000000000000000000000007e9bb9673ac38071a7699e6a3c48b8fbde574cd00000000000000000000000000000000000000000000000000000000000000040000000000000000000000000000000000000000000000000000000000000000a74657374696e6731323300000000000000000000000000000000000000000000c001a0e50fe06c37fda195c02ee64e359020fa135b7b2e9f9e4ffc12aa1b6430eda835a0732c210ac338e9ff2431c7f5076ce6cde517a6fa4d37a6339928e58e24d1a86f"
    run_test(
        contract, 
        data, 
        backend, 
        firmware, 
        navigator, 
        test_name, 
        wallet_addr
    )
