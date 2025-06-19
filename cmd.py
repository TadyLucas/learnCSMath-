import random

MAX_VALUE = 50

def dec_to_bin(n):
    return bin(n)[2:]

def dec_to_hex(n):
    return hex(n)[2:]

def bin_to_dec(b):
    return str(int(b, 2))

def hex_to_dec(h):
    return str(int(h, 16))

def quiz_round():
    conversions = [
        ("Decimal → Binary", dec_to_bin, "decimal", "binary"),
        ("Decimal → Hexadecimal", dec_to_hex, "decimal", "hex"),
        ("Binary → Decimal", bin_to_dec, "binary", "decimal"),
        ("Hexadecimal → Decimal", hex_to_dec, "hex", "decimal"),
    ]

    conv_name, func, from_type, to_type = random.choice(conversions)

    # Generate random input
    if from_type == "decimal":
        value = random.randint(1, MAX_VALUE)
        display_value = str(value)
    elif from_type == "binary":
        value = random.randint(1, MAX_VALUE)
        display_value = bin(value)[2:]
    else:  # hex
        value = random.randint(1, MAX_VALUE)
        display_value = hex(value)[2:]

    print(f"{conv_name}")
    print(f"Input: {display_value}")

    user_answer = input("Your answer: ").lower().strip()
    if from_type == "decimal":
        correct_answer = func(value)
    else:
        correct_answer = func(display_value)


    if user_answer == correct_answer:
        print("✅ Correct!")
    else:
        print(f"❌ Wrong. Correct answer: {correct_answer}")

def main():
    global MAX_VALUE
    print("🔢 Number Conversion Quiz")
    maxn = input("Max number: ")
    print("----------------------")
    try:
        if maxn:
            MAX_VALUE = int(maxn)
    except:
        pass
    while True:
        quiz_round()
        print("")

if __name__ == "__main__":
    main()
