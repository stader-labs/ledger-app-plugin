from web3 import Web3
from tests.utils import run_test, load_contract

contract = load_contract(
    "0x62De59c08eB5dAE4b7E6F7a8cAd3006d6965ec16"
)

def test_kelp_initiateWithdrawalLST(backend, firmware, navigator, test_name, wallet_addr):
    data = "0x02f8b001318421bef4e984dfce82df83105db09462de59c08eb5dae4b7e6f7a8cad3006d6965ec1680b844c8393ba9000000000000000000000000a35b1b31ce002fbf2058d22f30f95d405200a15b0000000000000000000000000000000000000000000000000f99f5f1987e8000c001a05dd079fce787f4a03da05f8ba68d6a1abe3d094a6985c27dab843e84eff027b9a005fc6255e49140ca4d76477e6a4f3d6ae09d61f83a56655e166e960683d3127e"
    run_test(
        contract, 
        data, 
        backend, 
        firmware, 
        navigator, 
        test_name, 
        wallet_addr
    )

