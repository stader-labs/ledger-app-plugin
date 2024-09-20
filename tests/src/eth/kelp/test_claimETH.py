from web3 import Web3
from tests.utils import run_test, load_contract

contract = load_contract(
    "0x62De59c08eB5dAE4b7E6F7a8cAd3006d6965ec16"
)

def test_kelp_claimETH(backend, firmware, navigator, test_name, wallet_addr):
    data = "0x02f89001078439d106808502f335de57830227ce9462de59c08eb5dae4b7e6f7a8cad3006d6965ec1680a46dbaf9ee000000000000000000000000eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec080a0e5b528d407765077dc056f703a6b616bff83ed970eb2250615e94347846ad133a040c023c952756e5aa6d25dec78cb7f67f9ebb5f42de588d6e46c34e2976f6308"
    run_test(
        contract, 
        data, 
        backend, 
        firmware, 
        navigator, 
        test_name, 
        wallet_addr
    )

