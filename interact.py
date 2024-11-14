import os 
from boa.network import EthereumRPC, NetworkEnv
import boa 
from eth_account import Account
from dotenv import load_dotenv

load_dotenv()

MY_CONTRACT = "0xCf7Ed3AccA5a467e9e704C703E8D87F634fB0Fc9"
# Address
# ABI

def main():
    rpc = os.getenv("RPC_URL")
    env = NetworkEnv(EthereumRPC(rpc))
    boa.set_env(env)

    anvil_key = os.getenv("ANVIL_KEY")
    my_account = Account.from_key(anvil_key)
    boa.env.add_account(my_account, force_eoa=True)

    favorite_deployer = boa.load_partial("favorites.vy")
    favorites_contract = favorite_deployer.at(MY_CONTRACT)

    favorite_number = favorites_contract.retrieve()
    print(f"Favorite number is {favorite_number}")

    favorites_contract.store(22)
    favorite_number_updated = favorites_contract.retrieve()
    print(f"Favorite number is now {favorite_number_updated}")

if __name__ == "__main__":
    main()