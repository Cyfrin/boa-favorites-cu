from dotenv import load_dotenv
import boa

load_dotenv()


def main():
    print("Let's read in the Vyper code and deploy it to the blockchain!")

    # Deploy the contract to a `pyevm` network!
    favorites_contract = boa.load("favorites.vy")
    starting_favorite_number = favorites_contract.retrieve()
    print(f"The starting favorite number is: {starting_favorite_number}")

    favorites_contract.store(5) # This sends a transaction!
    ending_favorite_number = favorites_contract.retrieve()
    print(f"The ending favorite number is: {ending_favorite_number}")


if __name__ == "__main__":
    main()
