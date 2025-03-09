import webbrowser
import sys
import os

# 常數
YOUTUBE_URL = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

def ask_math_question():
    while True:
        try:
            user_input = input("1 times 1 = ? ")
            if user_input == "1":
                play_video()
                break
            elif user_input.lower() == "exit":
                sys.exit()
            else:
                print("Wrong! Try again.")
        except Exception as e:
            print(f"Unexpected error: {e}")

def play_video():
    webbrowser.open(YOUTUBE_URL)
    print("Rickroll incoming...")

if __name__ == "__main__":
    ask_math_question()
