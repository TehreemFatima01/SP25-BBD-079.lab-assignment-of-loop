#List of favorite movies
favorite_movies = ["Megan", "Dead man", "Bly manor"]

# Printing each movie
print("Favorite Movies:")
for index, movie in enumerate(favorite_movies, start=1):
    print(f"{index}. {movie}")

print("\nString Iteration:")

# Full name
full_name = "Tehreem Fatima"

# Printing each character
for char in full_name:
    print(char)

# Counting vowels
vowels = "aeiouAEIOU"
vowel_count = sum(1 for char in full_name if char in vowels)
print(f"\nNumber of vowels in '{full_name}': {vowel_count}")
