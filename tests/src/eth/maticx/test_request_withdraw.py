from web3 import Web3
from tests.utils import run_test, load_contract

contract = load_contract(
    "0xf03a7eb46d01d9ecaa104558c732cf82f6b6b645"
)

def test_maticx_request_withdraw(backend, firmware, navigator, test_name, wallet_addr):
    data = "0x02f890012c8459682f008501deb8635e8309c5c794f03a7eb46d01d9ecaa104558c732cf82f6b6b64580a4745400c9000000000000000000000000000000000000000000000045c41fde9b3d420000c001a020d9ed1733bdea2b2fc59f7b0e4037ede9f45b7992f25c5c996f1d7ede25313aa043b6a72566c01b2d2f8abbdd3824ea5fc0410ac728cc15f5bb5d01070df4d3ca"
    run_test(
        contract, 
        data, 
        backend, 
        firmware, 
        navigator, 
        test_name, 
        wallet_addr
    )

