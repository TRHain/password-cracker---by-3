alphabet = "abcdefghijklmnopqrstuvwxyz"
secret = "gym"
found = False
attempts = 0

for c1 in alphabet:
    for c2 in alphabet:
        for c3 in alphabet:
            attempt = c1 + c2 + c3
            attempts += 1
            if attempt == secret:
                found = True
                print("Password found:", attempt)
                print("Attempts:", attempts)
                break
        if found:
            break
    if found:
        break