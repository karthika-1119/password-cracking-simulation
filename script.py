# Get user inputs
name = input("Enter first name: ").upper()
user_hash = input("Enter hash: ")

# Save hash to hash.txt (overwrite if exists)
with open("hash.txt", "w") as hash_file:
    hash_file.write(user_hash + "\n")

# Generate wordlist and save to wordlist.txt (overwrite if exists)
with open("wordlist.txt", "w") as wordlist_file:
    for i in range(1900, 2071):
        word = f"{name}{i}"
        wordlist_file.write(word + "\n")

print("Files created successfully!")
print("Name used:", name)