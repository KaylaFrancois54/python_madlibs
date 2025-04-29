   # Python Mad Libs Warm-Up Activity

   # Welcome message
print("Welcome to Python Mad Libs!")
print("Answer the following questions to create your very own silly story.\n")

   # Gather user inputs
   # Adding loop to allow multiple rounds
while True:
    adjective = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    adverb = input("Enter an adverb: ")

    story = (
        f"Today, I saw a {adjective} {noun} that decided to {verb} {adverb}.\n"
        "I couldn't believe my eyes!"
    )

    print("\n" + story)

    # Ask if the user wants to save the story
    save = input("Do you want to save your story to a file? (yes/no): ").strip().lower()
    if save == "yes":
        filename = input("Enter a filename (without extension): ").strip()
        with open(f"{filename}.txt", "w") as file:
            file.write(story)
        print(f"Story saved to {filename}.txt!")

    # Ask if they want to play again
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break  # ✅ This is now inside the while loop

   # Display the completed story
    print("\nHere is your story:")
    print(story)

# Answer the following questions:

# 1. which python function did you use to get user input?

#    - I used the `input()` function to get user input.

# 2. How did f-string formatting help in constructing the story?

#   - F-string formatting allowed me to easily insert the user inputs into the story template by using curly braces `{}` within the string. This made the code cleaner and more readable.

# 3. what would you change or add to your script if you wanted to make the game more interactive?

# - I would add loop to allowe the user to play multiple rounds without restarting the script.