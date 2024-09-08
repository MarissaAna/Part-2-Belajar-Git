import random

def get_user_choice():
    print("\nPilih salah satu: (b) Batu, (g) Gunting, (k) Kertas, atau (q) untuk keluar")
    user_input = input("Masukkan pilihan Anda (b/g/k/q): ").lower()

    while user_input not in ['b', 'g', 'k', 'q']:
        print("Pilihan tidak valid. Coba lagi.")
        user_input = input("Masukkan pilihan Anda (b/g/k/q): ").lower()

    if user_input == 'b':
        return "Batu"
    elif user_input == 'g':
        return "Gunting"
    elif user_input == 'k':
        return "Kertas"
    elif user_input == 'q':
        return "Keluar"

def get_computer_choice():
    choices = ["Batu", "Gunting", "Kertas"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Seri!"
    elif (user_choice == "Batu" and computer_choice == "Gunting") or \
         (user_choice == "Gunting" and computer_choice == "Kertas") or \
         (user_choice == "Kertas" and computer_choice == "Batu"):
        return "Anda menang!"
    else:
        return "Komputer menang!"

def play_game():
    print("Selamat datang di permainan Batu Gunting Kertas!")

    while True:
        user_choice = get_user_choice()

        if user_choice == "Keluar":
            print("Terima kasih telah bermain!")
            break

        computer_choice = get_computer_choice()

        print(f"Pilihan Anda: {user_choice}")
        print(f"Pilihan komputer: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

play_game()
