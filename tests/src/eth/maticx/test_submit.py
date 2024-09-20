from web3 import Web3
from tests.utils import run_test, load_contract

contract = load_contract(
    "0xf03a7eb46d01d9ecaa104558c732cf82f6b6b645"
)

def test_maticx_submit(backend, firmware, navigator, test_name, wallet_addr):
    data = "0x02f890012b8459682f008501e45cb83d8307229094f03a7eb46d01d9ecaa104558c732cf82f6b6b64580a4ea99c2a60000000000000000000000000000000000000000000000481591030b2a830000c080a059adbe59fe76966e72c711b1487063246f5997278af9f2c7924aa49a23a50aaaa03a9c651f564666a26faa3f8ab9235bfc4d9d62a804075944d314a105e2519a30"
    run_test(
        contract, 
        data, 
        backend, 
        firmware, 
        navigator, 
        test_name, 
        wallet_addr
    )

