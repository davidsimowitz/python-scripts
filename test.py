"""Unit tests"""


import checksum


print(
    checksum.checksum(
        filename='pycharm-professional-2019.1.3.exe',
        expected='93360bc9424a4fe49ce3be988ad2188ea44e7be7859c4bf19c38c3bebb5d0cb1'
    )
)
