def convert_currency(usd_amount, exchange_amount):
    return usd_amount * exchange_amount

def main():

    try:
        usd_amount = float(input("Enter the amount in USD: "))
    except ValueError:
        print("Enter a valid number!")
        return 
    
    exchange_rate = 83.88

    inr_amount = convert_currency(usd_amount, exchange_rate)

    print(f"{usd_amount:.2f} USD is equal to {inr_amount:.2f} INR")

main()