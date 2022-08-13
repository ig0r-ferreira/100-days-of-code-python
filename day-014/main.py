import copy
import random
from textwrap import dedent
from typing import List, Dict, Any
import art
import game_data


def clear_console() -> None:
    print("\033[H\033[J", end="")


def show_logo() -> None:
    """
        Clear the console and show the logo.
    """
    clear_console()
    print(dedent("""
        {logo}
        Welcome to Higher Lower Gamer
    """).format(logo=art.LOGO))


def show_comparison(profiles: Dict[str, Dict[str, Any]]) -> None:
    """
        Shows a formatted view of the reported profiles.
    """
    print(dedent("""
        Compare A: {A[name]}, a {A[description]}, from {A[country]}
        {versus}
        Against B: {B[name]}, a {B[description]}, from {B[country]}
    """).format(**profiles, versus=art.VS))


def random_profile(profile_list: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
        Returns a random profile removed from the profile list.
    """
    profile = random.choice(profile_list)
    profile_list.remove(profile)

    return profile


def ask_for_guess(profiles: Dict[str, Dict[str, Any]]) -> str:
    """
        Asks for a guess and returns it if it is within the allowed options.
    """
    while True:
        guess = input("Who has more followers? A or B? ").upper()
        if guess in profiles.keys():
            return guess
        
        print("Error: You must choose A or B.")


def get_higher_profile(**profiles: Dict[str, Any]) -> Dict[str, Any]:
    """
        Returns the most followed profile.
    """
    return max(profiles.values(), key=lambda profile: profile["follower_count"])


def main() -> None:
    profiles_data = copy.deepcopy(game_data.DATA)
    
    show_logo()
    
    if len(profiles_data) < 2:
        print("Not enough profiles.")
        return
    
    profiles = {
        "A": random_profile(profiles_data),
        "B": random_profile(profiles_data),
    }
    
    score = 0
    
    while True:      
        show_comparison(profiles)

        guess = ask_for_guess(profiles)

        clear_console()
        show_logo()

        higher_profile = get_higher_profile(**profiles)

        if profiles[guess] != higher_profile: 
            print(f"Sorry, that's wrong. Final score: {score}.")
            break
                
        score += 1

        if len(profiles_data):
            print(f"You're right. Current score: {score}.")
        else:
            print(f"Congratulations, you got them all right. Final score: {score}.")
            break
        
        profiles.update({"A": higher_profile, "B": random_profile(profiles_data)})
  

if __name__ == "__main__":
    main()