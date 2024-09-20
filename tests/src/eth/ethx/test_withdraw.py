from web3 import Web3
from tests.utils import run_test, load_contract

contract = load_contract(
    "0xcf5ea1b38380f6af39068375516daf40ed70d299"
)

def test_ethx_withdraw(backend, firmware, navigator, test_name, wallet_addr):
    data = "0x02f9011101278405f5e100850202345eaa8306d1d9949f0491b32dbce587c50c4c43ab303b06478193a780b8a41f7ec12200000000000000000000000000000000000000000000000000005af3107a40000000000000000000000000007e9bb9673ac38071a7699e6a3c48b8fbde574cd00000000000000000000000000000000000000000000000000000000000000060000000000000000000000000000000000000000000000000000000000000000a74657374696e6731323300000000000000000000000000000000000000000000c080a0908adc7cdbe3110e6353592e11da106ec8ba4ca7172a1641058cb7bb26c5acefa07035284a6a0ef6f98708a30f498ac1ace86bafb8294683b4000cb638ad7beba1"
    run_test(
        contract, 
        data, 
        backend, 
        firmware, 
        navigator, 
        test_name, 
        wallet_addr
    )
