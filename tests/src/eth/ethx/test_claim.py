from web3 import Web3
from tests.utils import run_test, load_contract

contract = load_contract(
    "0xcf5ea1b38380f6af39068375516daf40ed70d299"
)

def test_ethx_claim(backend, firmware, navigator, test_name, wallet_addr):
    data = "0x02f8910156850680edd7ec850680edd7ec83015d09949f0491b32dbce587c50c4c43ab303b06478193a780a4379607f50000000000000000000000000000000000000000000000000000000000000042c080a0ef4bce4226c5f12be27b95257456c6f51268d46a4d34c5eee583dbe41266fb51a02ca1ee59d5ddfd731edeccc0599e6f76a9012420412c98008cd05bdc3bf52668"
    run_test(
        contract, 
        data, 
        backend, 
        firmware, 
        navigator, 
        test_name, 
        wallet_addr
    )

