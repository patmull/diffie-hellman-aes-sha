import random
# from des import encrypt, decrypt
import Crypto.Util.number
import Crypto.Random
from sha_aes import encrypt, decrypt

class CommonMath:
    alpha = None
    p = None

    def __init__(self):
        self.alpha = self.compute_random_int()
        self.p = self.compute_random_prime()

    def compute_random_int(self):
        return random.randint(0, 9999999999)

    def compute_random_prime(self):
        prime = Crypto.Util.number.getPrime(100, randfunc=Crypto.Random.get_random_bytes)
        return prime


class CommunicationSide:
    common_math = None
    secret_key = None
    alpha = None

    def __init__(self, common_math):
        self.common_math = common_math
        self.secret_key = self.common_math.compute_random_int()

    def run_sharing_public_key(self):
        public_key_mine = pow(self.common_math.alpha, self.secret_key, self.common_math.p)

        print("Mine public key is: ")
        print(public_key_mine)

    def derivate_common_shared_key(self):
        public_key_other = input("Public key of other side:")
        shared_common_secret_key = pow(int(public_key_other), self.secret_key, self.common_math.p)
        print("Shared common secret key:")
        print(shared_common_secret_key)

    def encrypt_secret_message(self):
        plaintext = input("Enter secret message:")
        shared_common_secret_key = input("Enter shared common secret key:")
        ciphertext = encrypt(plaintext.encode(), shared_common_secret_key.encode())
        print(ciphertext)

    def decrypt_secret_message(self):
        shared_common_secret_key = input("Enter shared common secret key:")
        ciphertext = input("Enter ciphertext:")
        secret_message = decrypt(ciphertext, shared_common_secret_key.encode())
        print(secret_message.decode())


def main():
    common_math = CommonMath()

    alice = CommunicationSide(common_math)
    bob = CommunicationSide(common_math)

    print("Alice....")
    alice.run_sharing_public_key()

    print("Bob...")
    bob.run_sharing_public_key()

    print("Alice...")
    alice.derivate_common_shared_key()
    print("Bob...")
    bob.derivate_common_shared_key()

    print("Alice...")
    alice.encrypt_secret_message()
    print("Bob...")
    bob.decrypt_secret_message()


if __name__ == "__main__":
    main()
