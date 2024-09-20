from web3 import Web3
from tests.utils import run_test, load_contract

contract = load_contract(
    "0x62De59c08eB5dAE4b7E6F7a8cAd3006d6965ec16"
)

def test_kelp_initiateWithdrawalETH(backend, firmware, navigator, test_name, wallet_addr):
    data = "0x02f8b00150839402a08501ccf6aae1830a78d19462de59c08eb5dae4b7e6f7a8cad3006d6965ec1680b844c8393ba9000000000000000000000000eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000000000000000000000000000015f021397cf0000c001a0b812d5b2183bd21ccde3765da1ad02a7233f835b01bc3519db9a123f84acbf38a0761578a1e66af567e40dcf4597af674956381fc85db0f2c9881f3f95eb863726"
    run_test(
        contract, 
        data, 
        backend, 
        firmware, 
        navigator, 
        test_name, 
        wallet_addr
    )

