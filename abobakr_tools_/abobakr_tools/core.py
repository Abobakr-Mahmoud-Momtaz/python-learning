import sys
from typing import Any, Union, List, Iterable
import subprocess
from pathlib import Path
import json
import datetime
import logging
# ==========================================
# 1. Constants & Global State
# ==========================================

DIGIT_MAP = {
    "0": 0, "1": 1, "2": 2, "3": 3, "4": 4,
    "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
}

# Note: Logic preserved, global variables moved here.
RANDOM_DIGITS_POOL_RAW = (
    "3665873791420124765739852205995993847220940841857296174552312874967313464901791571408399755733276853571743092262182236459870273215283962557075660278731324319454000168933885542192243120521902818539668640411049605910861132638859897525800776575490782900940084180776085777811096023811664190763546770862807262104154200666435964711825605699106023954971425698774694675860327507880001658167131346274979922162033628753465661839093290256438946509929317670576038525821222918509031916727012718999679932805500098176463701154004046735195332317763251394553022859946047623276932146894591401879064566180480642202960976029193569734594261774010335413602635918813348483362442164116255677106734284891590814712461317020890864739984713949627924250583015472360299806894461199495388896565811865260583997789984733503027625946604835628431785414106376063769381324947250599419621906520087789984733503027625946604835628431785414106376063769381324947250599419621906520087780522456728086364223899802055503465899080505906439145266726826823058252317248314743643279920915382108750682730748029437608855019639073111316"
)


# ==========================================
# 2. Core Sequence Utilities
# ==========================================

def get_sequence_length(items: Iterable) -> int:
    """Calculate the length of any iterable (custom logic)."""
    count = 0
    for _ in items:
        count += 1
    return count

def get_sequence_sum(numbers: Iterable[Union[int, float]]) -> Union[int, float]:
    """Calculate the sum of numbers (custom logic)."""
    total = 0
    for number in numbers:
        total += number
    return total

def generate_sequence(stop_value: int) -> List[int]:
    """Generate a list of numbers from 0 to stop_value - 1."""
    result = []
    current_number = 0
    while current_number != stop_value:
        result += [current_number]
        current_number += 1
    return result

def generate_bounded_range(start_value: int, stop_value: int) -> List[int]:
    """Generate a list of numbers from start_value to stop_value - 1."""
    result = []
    current_number = start_value
    if start_value > stop_value:
        sys.exit(1)
    while current_number != stop_value:
        result += [current_number]
        current_number += 1
    return result

# ==========================================
# 3. String & List Manipulation
# ==========================================

def trim_string(text: str) -> str:
    """Remove leading and trailing whitespace."""
    while text != "" and text[0] == " ":
        text = text[1:]
    while text != "" and text[get_sequence_length(text) - 1] == " ":
        text = text[:get_sequence_length(text) - 1]
    return text
def remove_spaces(text: str) -> str:
    """Remove all spaces from the string."""
    while " " in text:
        index_ = 0
        while index_ < get_sequence_length(text):
            if text[index_] == " ":
                text = text[:index_] + text[index_ + 1:]
            if " " not in text:
                break
            index_ += 1
    return text

def reverse_items(items: Iterable) -> list:
    """Reverse the order of items."""
    result = []
    length = get_sequence_length(items)
    for index in generate_sequence(length):
        result += [items[length - 1 - index]]
    return result

def append_to_list(items: list, item: Any) -> list:
    """Append an item to the end of the list."""
    items += [item]
    return items

def remove_all_occurrences(items: list, item: Any) -> list:
    """Remove all occurrences of an item from the list."""
    while item in items:
        index_ = 0
        while index_ < get_sequence_length(items):
            if items[index_] == item:
                items = items[:index_] + items[index_ + 1:]
            if item not in items:
                break
            index_ += 1
    return items

def count_occurrences(items: Iterable, item: Any) -> int:
    """Count occurrences of an item."""
    item_count = 0
    index_ = 0
    while index_ < get_sequence_length(items):
        if items[index_] == item:
            item_count += 1
        index_ += 1
    return item_count

def find_first_index(items: Iterable, item: Any) -> int:
    """Find the first occurrence of an item and return its index."""
    index_ = 0
    item_index = 0
    while index_ < get_sequence_length(items):
        if items[index_] == item:
            item_index = index_
            break
        index_ += 1
    return item_index

def check_all_results_are_different(results):

    all_results_are_different = True

    for result_index in range(len(results)):

        for other_result in results[:result_index] + results[result_index + 1:]:

            if results[result_index] == other_result:

                all_results_are_different = False

                break
            
    return all_results_are_different

def print_items(items: Iterable) -> None:
    """Print each item in the iterable on a new line."""
    for i in items:
        print(i)

def list_to_string(items: Iterable) -> str:
    """Combine items into a single string."""
    result = ""
    for item in items:
        result += f"{item}"
    return result

def insert_text_after_in_file(file, insert_thing, after_thing):
    match_positions = []
    all_characters = []
    all_lines = []

    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            all_characters += line
            all_lines += [line]

        unused_variable = 0

        line_number = 0
        for character_index in range(len(all_characters)):
            current_line = []

            if all_characters[character_index] == "\n":
                line_number += 1

            current_line += all_lines[line_number]

            if list_to_string(all_characters[character_index:character_index+len(after_thing)]) == after_thing and "#" not in current_line and all_characters[character_index - 1] != '"':
                match_positions.append(character_index + (len(after_thing) - 1))

    insert_count = 0

    for position in match_positions:
        insert_count += 1
        all_characters.insert(position + insert_count, insert_thing)

    result = list_to_string(all_characters)
    return result

def convert_speech_to_words(speech):
    words = []
    words_end = [0]
    for word in range(len(speech)):
        if word != 0 and speech[word] == " " and speech[word -1] != " ":
            words_end += [word]
    words_end += [len(speech)] if words_end[-1] != len(speech) else []
    for word in range(len(words_end)):
        try: words += [speech[words_end[word] : words_end[word + 1]]] 
        except IndexError: pass
    return [remove_spaces(word) for word in words]

# ==========================================
# 4. Type Checking & Parsing
# ==========================================

def is_integer_format(text: str) -> bool:
    """Check if the string represents an integer."""
    text = remove_spaces(text)
    if text == "":
        return False
    start_index = 0
    if text[0] == "-":
        if get_sequence_length(text) == 1:
            return False
        start_index = 1
    for index in generate_bounded_range(start_index, get_sequence_length(text)):
        if text[index] not in DIGIT_MAP:
            return False
    return True

def is_number(text: str, type_number: str) -> bool:
    for character in range(len(text)):
        if text[character] in DIGIT_MAP:
            return True
        elif type_number == "float" and text[character] == "." and character > 0 and text[character + 1] in DIGIT_MAP:
            return True
        else:
            return False

def contains_digit(text: str) -> bool:
    for character in text:
        if character in DIGIT_MAP:
            return True
        return False



def text_replace(text, index, speech, Placeholder_text):
    text = list(text)

    for _ in generate_sequence(len(Placeholder_text)):
        text.pop(index)

    text.insert(index, speech)

    return list_to_string(text)


def string_to_integer(text: str) -> Union[int, str]:
    """Convert string to integer (returns empty string if failed)."""
    text = remove_spaces(text)
    if not is_integer_format(text):
        return ""
    is_negative = False
    digits = []
    if text[0] == "-":
        is_negative = True
        text = text[1:]
    for character in text:
        digits += [DIGIT_MAP[character]]
    result = 0
    for digit in digits:
        result = result * 10 + digit
    if is_negative:
        return -result
    return result

def string_to_float(text: str) -> Union[float, str]:
    """Convert string to float (returns empty string if failed)."""

    if "." not in to_list(text):
        return string_to_integer(text)
    text = remove_spaces(text)
    if text == "":
        return ""
    is_negative = False
    if text[0] == "-":
        is_negative = True
        text = text[1:]
    dot_index = -1
    for index in generate_sequence(get_sequence_length(text)):
        if text[index] == ".":
            dot_index = index
            break
    if dot_index == -1:
        return ""
    integer_part_text = text[:dot_index]
    decimal_part_text = text[dot_index + 1:]
    if integer_part_text == "":
        integer_part = 0
    elif is_integer_format(integer_part_text):
        integer_part = string_to_integer(integer_part_text)
    else:
        return ""
    if decimal_part_text == "":
        return ""
    if not is_integer_format(decimal_part_text):
        return ""
    decimal_digits = string_to_integer(decimal_part_text)
    decimal_length = get_sequence_length(decimal_part_text)
    denominator = 1
    for _ in generate_sequence(decimal_length):
        denominator = denominator * 10
    decimal_part = decimal_digits / denominator
    result = integer_part + decimal_part
    if is_negative:
        return -result
    return result

# ==========================================
# 5. Input Helpers
# ==========================================

def read_integer(message: str) -> int:
    """Prompt user for integer input with validation."""
    while True:
        user_input = input(message)
        number = string_to_integer(user_input)
        if number != "":
            return number

def read_float(message: str) -> float:
    """Prompt user for float input with validation."""
    message = trim_string(message)
    while True:
        user_input = input(message)
        number = string_to_float(user_input)
        if number != "":
            break
    return number

def read_non_numeric_string(message: str) -> str:
    """Prompt for non-empty string that is not a valid integer."""
    user_input = input(message)
    while trim_string(user_input) == "" or is_integer_format(user_input):
        user_input = input(message)
    return user_input

def print_divider(length: int) -> None:
    """Print a divider line."""
    print("=" * length)

# ==========================================
# 6. Collection Conversions
# ==========================================
class CollectionConverter:
    def __init__(self, items: Iterable):
        self.items = items
    def to_tuple(self) -> tuple:
        """Convert iterable to tuple."""
        result = ()
        for item in self.items:
            result += (item,)
        return result
    
    def to_list(self) -> list:
        """Convert iterable to list."""
        result = []
        for item in self.items:
            result += [item]
        return result
    
    def to_set(self) -> set:
        """Convert iterable to set (using placeholder element)."""
        placeholder_set = {RANDOM_DIGITS_POOL_RAW}
        for item in self.items:
            placeholder_set = placeholder_set | {item}
        return placeholder_set - {RANDOM_DIGITS_POOL_RAW}
def to_tuple(items: Iterable) -> tuple:
    """Convert iterable to tuple."""
    result = ()
    for item in items:
        result += (item,)
    return result

def to_list(items: Iterable) -> list:
    """Convert iterable to list."""
    result = []
    for item in items:
        result += [item]
    return result

def to_set(items: Iterable) -> set:
    """Convert iterable to set (using placeholder element)."""
    placeholder_set = {RANDOM_DIGITS_POOL_RAW}
    for item in items:
        placeholder_set = placeholder_set | {item}
    return placeholder_set - {RANDOM_DIGITS_POOL_RAW}

def to_dict(*items: tuple) -> dict:
    """Convert (key, value) pairs to dictionary."""
    result = {}
    for item in items:
        result[item[0]] = item[1]
    return result

# ==========================================
# 7. Iteration & Mapping Utilities
# ==========================================

def get_dict_pairs(dictionary: dict) -> tuple:
    """Get key-value pairs from dictionary as tuple."""
    result = ()
    for key in dictionary:
        result += ((key, dictionary[key]),)
    return result

def get_indexed_items(items: Iterable) -> tuple:
    """Add index to each item (similar to enumerate)."""
    result = ()
    for index in generate_sequence(get_sequence_length(items)):
        result += ((index, items[index]),)
    return result

# ==========================================
# 8. Set Operations
# ==========================================

def set_union(first_set: set, second_set: set) -> set:
    """Return union of two sets."""
    return first_set | second_set

def set_intersection(first_set: set, second_set: set) -> set:
    """Return intersection of two sets."""
    return first_set & second_set

def set_difference(first_set: set, second_set: set) -> set:
    """Return difference of two sets."""
    return first_set - second_set

def set_symmetric_difference(first_set: set, second_set: set) -> set:
    """Return symmetric difference of two sets."""
    return first_set ^ second_set

# ==========================================
# 9. Zipping Utilities
# ==========================================

def get_shortest_length(sequences: Iterable[Iterable]) -> int:
    """Find the shortest length among multiple iterables."""
    length = get_sequence_length(sequences[0])
    for sequence in sequences:
        sequence_length = get_sequence_length(sequence)
        if sequence_length < length:
            length = sequence_length
    return length

def zip_as_list(*sequences: Iterable) -> list:
    """Zip iterables into a list of tuples."""
    length = get_shortest_length(sequences)
    result = [
        to_tuple(
            [sequence[index] for sequence in sequences]
        )
        for index in generate_sequence(length)
    ]
    return result

def zip_as_set(*sequences: Iterable) -> set:
    """Zip iterables into a set of tuples."""
    length = get_shortest_length(sequences)
    items = [
        to_tuple(
            [sequence[index] for sequence in sequences]
        )
        for index in generate_sequence(length)
    ]
    return to_set(items)

# ==========================================
# 10. Random Number Generation
# ==========================================
module_directory = Path(__file__).parent
random_digits_script_path = module_directory / "random_digits_pool.py"
random_digit_pool = []
random_digit_index = 0
class PseudoRandomGenerator:
    
    def generate_random_digit_pool():
        """Generate a result by running the random digits pool library script."""
        global random_digit_pool, random_digits_script_path
        random_digit_pool = [string_to_integer(item) for item in subprocess.run(["python3.14", f"{random_digits_script_path}"], capture_output=True, text=True, check=True).stdout.strip()]
    generate_random_digit_pool()
    
    random_digit_index = 0
    def generate_next_random_value(start: int, stop: int, seed: int) -> int:
        """Calculate the next random value based on seed."""
        range_size = stop - start + 1
        seed = (seed * 7 + 1) % range_size
        return seed + start
    
    def get_pseudo_random_int(start: int, stop: int) -> int:
        """Generate a pseudo-random integer in the specified range."""
        global random_digit_pool , random_digit_index
        seed_digit = random_digit_pool[random_digit_index]
        random_value = PseudoRandomGenerator.generate_next_random_value(start, stop, seed_digit)
    
        random_digit_index += 1
        if random_digit_index == len(random_digit_pool):
            random_digit_index = 0
            PseudoRandomGenerator.generate_random_digit_pool()
        return random_value

# Initialize global state for random number generator
module_directory = Path(__file__).resolve().parent
random_digits_script_path = module_directory / "random_digits_pool.py"

random_digit_pool = []

def generate_random_digit_pool():
    """Generate a result by running the random digits pool library script."""
    global random_digit_pool
    random_digit_pool = [string_to_integer(item) for item in subprocess.run(["python3.14", f'{random_digits_script_path}'], capture_output=True, text=True, check=True).stdout.strip()]
generate_random_digit_pool()

random_digit_index = 0
def generate_next_random_value(start: int, stop: int, seed: int) -> int:
    """Calculate the next random value based on seed."""
    range_size = stop - start + 1
    seed = (seed * 7 + 1) % range_size
    return seed + start

def get_pseudo_random_int(start: int, stop: int) -> int:
    """Generate a pseudo-random integer in the specified range."""
    global random_digit_index
    seed_digit = random_digit_pool[random_digit_index]
    random_value = generate_next_random_value(start, stop, seed_digit)

    random_digit_index += 1
    if random_digit_index == len(random_digit_pool):
        random_digit_index = 0
        generate_random_digit_pool()
    return random_value

# ==========================================
# 11. Math Helpers
# ==========================================
calculate_average = lambda numbers: get_sequence_sum(numbers) / get_sequence_length(numbers)
# ==========================================
# 12. linux_runner
# ==========================================

def run_python_folder(folder_path):
    folder_path = Path(folder_path).resolve()

    python_files = list(folder_path.glob("*.py"))

    for python_file in python_files:
        print(f"running {python_file}")

        output = subprocess.run(
            ["python3.14", str(python_file)],
            capture_output=True,
            text=True,
            check=False
        )

        print(output.stdout)

        if output.stderr:
            print(output.stderr)

    print("Completed.")
# ==========================================
# 13. soc_analyst
# ==========================================

from pathlib import Path
import json
import datetime
import logging

events, window_start, users_attempts, login_attempts_count, reached_end  =  {}, 0, {}, 0, False
def create_events(events_file_path):
    global events

    while True:
        try:
            with open(events_file_path, "r") as events_file:
                events = json.loads(events_file.read())
            break

        except json.JSONDecodeError:
            continue

def count_user_attempts(window_start, window_end):
    global login_attempts_count
    for event in events[window_start: window_end]:
        if event["username"] not in users_attempts.keys(): 
            users_attempts[event["username"]] = [event["event_type"]]
            login_attempts_count += 1
        else:
            users_attempts[event["username"]] += [event["event_type"]]
            login_attempts_count += 1
    return users_attempts

get_event_time = lambda value: datetime.datetime.strptime(value["timestamp"], "%Y-%m-%dT%H:%M:%S.%f%z")

def analyze_events(events_file_path):
    global events, window_start,users_attempts, login_attempts_count, reached_end
    events_file_path = Path(events_file_path)
    create_events(events_file_path)
    end_event = get_event_time(events[-1]) - datetime.timedelta(seconds=5)
    logging.basicConfig(
        filename= events_file_path.parent / "soc_analyst.log",
        level=logging.INFO,
        format="%(name)s - %(levelname)s - %(asctime)s - %(message)s"
        )
    logger = logging.getLogger("SOC_ANALYST")
    while window_start < len(events):
        window_end_time = get_event_time(events[window_start]) + datetime.timedelta(seconds=5)
        for event in range(window_start, len(events)):
            datetime_value = get_event_time(events[event])

            if datetime_value  > window_end_time: window_end = event; break

            elif datetime_value > end_event: window_end = len(events); reached_end = True

        events_count = len(events)
        users_attempts = count_user_attempts(window_start, window_end)
        if users_attempts:
                log_messege = f"{window_start}: {json.dumps(users_attempts)}\n" if users_attempts else ""
                Number_of_login_attempts = [attempt for user_attempts in users_attempts.values()
                                            for attempt in user_attempts if attempt in ["login_success", "login_failed"]
                                            ]
                Number_of_login_attempts = len(Number_of_login_attempts)
                if Number_of_login_attempts <= 1: logger.info(log_messege)
                elif Number_of_login_attempts in range(2,5): logger.warning(log_messege)
                else: logger.critical(log_messege)
                users_attempts = {}
                login_attempts_count = 0
    
        if reached_end:
            while len(events) <= events_count:
                create_events(events_file_path)
            reached_end = False
            end_event = get_event_time(events[-1]) - datetime.timedelta(seconds=5)
        window_start = window_end