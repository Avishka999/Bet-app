import sys
from wallet import load_wallet, save_wallet
from games import play_coin_flip, play_dice_roll, play_roulette

def main():
    balance = load_wallet()
    
    while True:
        print("\n" + "="*40)
        print(f"💰 CURRENT BALANCE: ${balance}")
        print("="*40)
        print("1. Coin Flip (2x payout)")
        print("2. Dice Roll (6x payout)")
        print("3. Colors/Roulette (2x payout, 14x for green)")
        print("4. Exit")
        print("="*40)
        
        choice = input("Choose an option (1-4): ")
        
        if choice == '4':
            save_wallet(balance)
            print("\nThanks for playing! Your balance has been saved.")
            break
            
        if choice not in ['1', '2', '3']:
            print("\n[!] Invalid choice. Please try again.")
            continue
            
        try:
            bet_input = input("Enter your bet amount: $")
            bet = int(bet_input)
            if bet <= 0:
                print("\n[!] Bet must be greater than $0.")
                continue
            if bet > balance:
                print("\n[!] Insufficient funds!")
                continue
        except ValueError:
            print("\n[!] Please enter a valid whole number.")
            continue
            
        # Deduct bet temporarily during play
        balance -= bet
        payout = 0
        
        if choice == '1':
            guess = input("Choose 'heads' or 'tails': ").strip().lower()
            if guess not in ['heads', 'tails']:
                print("\n[!] Invalid guess. Bet refunded.")
                balance += bet
                continue
            payout, result = play_coin_flip(bet, guess)
            print(f"\n🪙 The coin landed on... {result.upper()}!")
            
        elif choice == '2':
            try:
                guess_input = input("Choose a number between 1 and 6: ")
                guess = int(guess_input)
                if guess < 1 or guess > 6:
                    raise ValueError
            except ValueError:
                print("\n[!] Invalid guess. Bet refunded.")
                balance += bet
                continue
            payout, result = play_dice_roll(bet, guess)
            print(f"\n🎲 The dice rolled a... {result}!")
            
        elif choice == '3':
            guess = input("Choose 'red', 'black', or 'green': ").strip().lower()
            if guess not in ['red', 'black', 'green']:
                print("\n[!] Invalid guess. Bet refunded.")
                balance += bet
                continue
            payout, result = play_roulette(bet, guess)
            print(f"\n🎡 The wheel landed on... {result.upper()}!")

        if payout > 0:
            print(f"🎉 YOU WON ${payout}! 🎉")
            balance += payout
        else:
            print("😞 You lost your bet.")
            
        if balance <= 0:
            print("\n💸 You're broke! Game over.")
            print("🏦 The bank took pity on you and gave you a $500 loan.")
            balance = 500
            
        save_wallet(balance)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nExiting game...")
        sys.exit(0)
