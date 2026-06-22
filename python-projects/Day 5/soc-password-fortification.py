import random

lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']
uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '@', '{', '}', '[', ']']
weak_patterns = ['123', 'password','qwerty', 'admin', 'letmein']

audit_password = input("Input your desired password for auditing: \n")

has_lower = False
has_upper = False
has_symbol = False
has_numbers = False

for every_character in audit_password:
    if every_character in lowercase:
        has_lower = True
for every_character in audit_password:
    if every_character in uppercase:
        has_upper = True
for every_character in audit_password:
    if every_character in symbols:
        has_symbol = True
for every_character in audit_password:
    if every_character in numbers:
        has_numbers = True

identified_weak_pattern = [] #this means tha for now identified_weak_pattern is = Zero
lower_audit_password= audit_password.lower()
for pattern in weak_patterns:
    if pattern in lower_audit_password:
        identified_weak_pattern.append(pattern)


sec_score = 0
audit_password_length = len(audit_password)
if audit_password_length >= 12:
    sec_score += 20

if has_lower == True:
    sec_score += 15
if has_upper == True:
    sec_score += 15
if has_symbol == True:
    sec_score += 15
if has_numbers == True:
    sec_score += 15

if len(identified_weak_pattern) == 0:
    sec_score += 20

if sec_score < 50:
    rating = "CRITICAL"
if  sec_score >= 50 and sec_score <= 79:
    rating = "MODERATE"
if sec_score >= 80 and sec_score <= 100:
    rating = "FORTIFIED"


print("=== SOC PASSWORD FORTRESS TOOL ===")

print("--- AUDIT REPORT ---")
print(f"Length: {audit_password_length} characters")
print(f"Lowercase: {'YES' if has_lower else 'NO'}")
print(f"Uppercase: {'YES' if has_upper else 'NO'}")
print(f"Digits: {'YES' if has_numbers else 'NO'}")
print(f"Symbols: {'YES' if has_symbol else 'NO'}")
if len(identified_weak_pattern) == 0:
    print(f"Weak Patterns Found: None Detected")
else:
    print(f"Weak Patterns Found: {len(identified_weak_pattern)}")
print(f"Security Score: {sec_score}/100")
print(f"Rating: {rating}")
if rating != "FORTIFIED":
    print("\n[!] Password is not FORTIFIED. Generating secure alternative...")
    # Nested Loops and Lists
    cyber_words = [["firewall", "encrypt", "packet", "malware", "phishing"], ["shield", "lock", "vault", "gate", "key"],
                   ["alpha", "delta", "ghost", "cobra", "nebula"]]

    random_words_1 = random.choice(cyber_words[0])
    random_words_2 = random.choice(cyber_words[1])
    random_words_3 = random.choice(cyber_words[2])

    selected_words = [random_words_1, random_words_2, random_words_3]

    scrambled_alphabetical_case = []
    # OUTER LOOP (the randomly selected words)
    for each_word in selected_words:
        new_word = ""  # Changing the list in selected_words to strings
        # build inner loop of each character in each_word
        for each_character in each_word:  # making the each letter of the new_word to change randomly
            random_alphabetical_case_switch = random.randint(0, 1)
            if random_alphabetical_case_switch == 0:
                new_word += each_character.upper()
            else:
                new_word += each_character.lower()
        scrambled_alphabetical_case.append(new_word)

    # adding random numbers and symbols increase no of characters
    number_1 = random.choice(numbers)
    number_2 = random.choice(numbers)
    number_3 = random.choice(numbers)
    number_4 = random.choice(numbers)

    symbol_1 = random.choice(symbols)
    symbol_2 = random.choice(symbols)
    symbol_3 = random.choice(symbols)
    symbol_4 = random.choice(symbols)

    # Building the new fortified password
    fortified_password_components = [scrambled_alphabetical_case[0], scrambled_alphabetical_case[1],
                                     scrambled_alphabetical_case[2], number_1, number_2, number_3, number_4, symbol_1,
                                     symbol_2, symbol_3, symbol_4]
    random.shuffle(fortified_password_components)

    fortified_password = ""
    for each_words in fortified_password_components:
        fortified_password += each_words

    print("\n--- FORTIFIED PASSWORD ---")
    print(f"Generated: {fortified_password}")