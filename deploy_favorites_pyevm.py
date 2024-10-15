from dotenv import load_dotenv
import boa

load_dotenv()


def main():
    print("Let's read in the Vyper code and deploy it to the blockchain!")

    # Deploy the contract to a `pyevm` network!
    favorites_contract = boa.load("favorites.vy")
    print(favorites_contract)


if __name__ == "__main__":
    main()
