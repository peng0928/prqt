# -*- coding: utf-8 -*-
# @Date    : 2022-10-24 15:58
# @Author  : chenxuepeng
import rsa

'''根据model、exponent加密， 无密钥'''
class Encrypt(object):
    def __init__(self, e, m):
        self.e = e if len(e) > 0 else '010001'
        self.m = m

    def encrypt(self, message):
        try:
            mm = int(self.m, 16)
            ee = int(self.e, 16)
            rsa_pubkey = rsa.PublicKey(mm, ee)
            crypto = self._encrypt(message.encode(), rsa_pubkey)
            return crypto.hex()
        except:
            return 'null'

    def _pad_for_encryption(self, message, target_length):
        message = message[::-1]
        max_msglength = target_length - 11
        msglength = len(message)

        padding = b''
        padding_length = target_length - msglength - 3

        for i in range(padding_length):
            padding += b'\x00'

        return b''.join([b'\x00\x00', padding, b'\x00', message])

    def _encrypt(self, message, pub_key):
        keylength = rsa.common.byte_size(pub_key.n)
        padded = self._pad_for_encryption(message, keylength)

        payload = rsa.transform.bytes2int(padded)
        encrypted = rsa.core.encrypt_int(payload, pub_key.e, pub_key.n)
        block = rsa.transform.int2bytes(encrypted, keylength)
        return block


