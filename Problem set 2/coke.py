def main():
    price = 50
    accepted_coins = [5, 10, 25]
    inserted_amt = 0

    while(inserted_amt < price):
        print(f"Amount Due: {price - inserted_amt}")
        coin = int(input("Insert Coin: "))
        if coin in accepted_coins:
            inserted_amt += coin
        # else:
        #     print(f"Invalid amount : {coin}")

    print(f"Change Owed: {inserted_amt - price}")

main()
