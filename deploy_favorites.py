from dotenv import load_dotenv
import boa
from boa.network import NetworkEnv, EthereumRPC
from eth_account import Account

load_dotenv()

ANVIL_URL = "http://127.0.0.1:8545"

# Never do this with a real key...
ANVIL_KEY = "0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80"


def main():
    print("Let's read in the Vyper code and deploy it to the blockchain!")

    my_account = Account.from_key(ANVIL_KEY)
    env = NetworkEnv(EthereumRPC(ANVIL_URL))
    boa.set_env(env)
    boa.env.add_account(my_account, force_eoa=True)

    # Deploy the contract to a `pyevm` network!
    favorites_contract = boa.load("favorites.vy")

    print("Storing a number...")
    favorites_contract.store(5)

    print(f"\nFavorite Number: {favorites_contract.retrieve()}\n")

    print("Storing a person...")
    favorites_contract.add_person("Alice", 25)

    print(f"\nNew Person: {favorites_contract.list_of_people(0)}\n")


if __name__ == "__main__":
    main()
