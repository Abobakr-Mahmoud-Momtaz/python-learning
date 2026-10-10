from pathlib import Path
RANDOM_DIGITS_RAW_1_MILLION_path = Path(__file__).parent / "RANDOM_DIGITS_RAW_1_MILLION.txt"
with open(RANDOM_DIGITS_RAW_1_MILLION_path, "r", encoding="utf-8") as file:

    random_digits_raw = file.read()

unique_digits = ""

for digit in list(set(random_digits_raw)):

    unique_digits += digit

print(unique_digits)