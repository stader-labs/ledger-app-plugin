from web3 import Web3
from tests.utils import run_test, load_contract

contract = load_contract(
    "0x62De59c08eB5dAE4b7E6F7a8cAd3006d6965ec16"
)

def test_kelp_claimLST(backend, firmware, navigator, test_name, wallet_addr):
    data = "0x02f8910181e48439d106808502c0b7a94e8302c6ad9462de59c08eb5dae4b7e6f7a8cad3006d6965ec1680a46dbaf9ee000000000000000000000000ac3e018457b222d93114458476f3e3416abbe38fc001a015b3a4d1d38f492c00322e7a1eef1f044ddfbe0f145031d80470e22ffa63dc24a07605ee5c0b3b1b0d216e10ee28a1db78cd723df9812d3ec2585beaaa9f0844e1"
    run_test(
        contract, 
        data, 
        backend, 
        firmware, 
        navigator, 
        test_name, 
        wallet_addr
    )

