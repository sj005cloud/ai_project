import sys
import time
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Import your modules
from knn_recommendation import recommend_nearest_spots
from data_analysis import analyze_parking_patterns
from availability_prediction import predict_availability

def welcome_banner():
    print(Fore.CYAN + "=" * 50)
    print(Fore.CYAN + f"{'SMART PARKING ASSISTANCE SYSTEM':^50}")
    print(Fore.CYAN + "=" * 50)

def get_user_coordinates():
    try:
        lat = float(input(Fore.YELLOW + "Enter your current latitude: "))
        lon = float(input(Fore.YELLOW + "Enter your current longitude: "))
        return [lat, lon]
    except ValueError:
        print(Fore.RED + "Invalid input. Please enter valid numeric coordinates.")
        sys.exit()

def main():
    welcome_banner()
    coordinates = get_user_coordinates()

    print(Fore.MAGENTA + "\n🔎 Searching for nearest parking spots...\n")
    time.sleep(1)  # Simulate thinking
    spots = recommend_nearest_spots(coordinates)
    print(Fore.GREEN + "Recommended Parking Spots:")
    for index, spot in enumerate(spots, 1):
        print(f"{index}. Location: {spot}")

    print(Fore.MAGENTA + "\n📊 Analyzing historical parking trends...\n")
    time.sleep(1)
    analyze_parking_patterns()

    print(Fore.MAGENTA + "\n🧠 Predicting future parking availability...\n")
    time.sleep(1)
    prediction = predict_availability()
    print(Fore.GREEN + f"\nPredicted Availability: {prediction}")

    print(Fore.CYAN + "\n✅ Thank you for using Smart Parking Assistance!\n")

if __name__ == '__main__':
    main()

