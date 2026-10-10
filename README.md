# Python Fundamentals & Manual Implementations

This repository documents my journey of learning Python through practical projects, exercises, and manual implementations of selected Python operations and concepts.

The main goal is **deep understanding rather than quick solutions**. By implementing common operations manually, I practice understanding the logic, algorithms, data structures, and behavior behind them instead of simply relying on built-in solutions.

---

## 📂 Projects

The `projects/` directory contains practical Python projects developed while learning and applying Python fundamentals.

### 1. Command-Line Calculator (`projects/calculator.py`)

A command-line calculator built to practice Python fundamentals, type parsing, mathematical operations, and error handling.

It supports:

- **Basic Operations:** Addition, subtraction, multiplication, and division.
- **Additional Operations:** Floor division (`//`), modulo (`%`), exponentiation (`^`), and roots (`sqrt`).
- **Error Handling:** Handles cases such as division by zero, invalid mathematical operations, and invalid user input.

> **Note:** The calculator uses its own command syntax for some operations. For example, `^` is used as the exponentiation symbol in the user interface, while Python itself uses `**` for exponentiation.

### 2. To-Do List Manager (`projects/to_do_list.py`)

A command-line task management application developed as a practical Python project.

It is used to practice:

- In-memory data management and list manipulation.
- CRUD operations (Create, Read, Update, Delete).
- User input validation.
- Command routing using `match-case`.
- Working with custom library functions.
- Building a larger program from smaller modular components.

### 3. Rock Paper Scissors (`projects/rock_paper_scissors.py`)

A command-line Rock Paper Scissors game built to practice:

- User input handling and validation.
- Conditional logic and loop control.
- List indexing and iteration.
- Pseudo-random number generation using custom library functions.
- Tracking and updating game state and scores.

---

## 🛠️ Custom Library: `abobakr_tools`

`abobakr_tools` is a custom Python library developed as part of my learning process.

The library contains manually implemented versions of selected Python operations, along with practical utilities that combine Python fundamentals into more complex functionality.

Its scope includes:

- Sequence operations and iteration.
- String and list manipulation.
- Numeric text parsing and validation.
- Input handling.
- Collection conversion and manipulation.
- Dictionary iteration and sequence zipping.
- File content processing and text insertion.
- Pseudo-random number generation.
- Basic mathematical calculations.
- Python script execution.
- Security event analysis and logging.

The library is primarily an educational project. Its purpose is to help me understand programming concepts, practice problem-solving, and apply the Python features I learn to practical tasks.

It is not intended to replace Python's built-in functions or standard library. Some functions intentionally reproduce existing functionality, while others combine multiple concepts into small utilities and experimental systems.

---

## 📦 Package: `abobakr_tools`

The package is located inside the `abobakr_tools_/` development directory.

Its files are organized as follows:

```text
abobakr_tools/
├── __init__.py
├── core.py
├── random_digits_pool.py
└── RANDOM_DIGITS_RAW_1_MILLION.txt
```

### `__init__.py`

The package initialization file.

It provides the package-level initialization and import entry point.

### `core.py`

The main module of the library.

It contains the core utility functions, the `CollectionConverter` class, the pseudo-random number generation implementations, the Python script runner, and the experimental security event analysis functionality.

Its functionality covers:

- Sequence utilities.
- String and list manipulation.
- Type checking and numeric parsing.
- Input helpers.
- Collection conversions.
- Dictionary and indexed iteration.
- Set operations.
- Zipping utilities.
- Pseudo-random number generation.
- Mathematical helpers.
- File content processing.
- Python script execution.
- Security event analysis and logging.

### `random_digits_pool.py`

A supporting Python script used by the pseudo-random number generation system to produce digit data for the main module.

The main module executes this script through `subprocess.run()` and processes its standard output to populate `random_digit_pool`.

### `RANDOM_DIGITS_RAW_1_MILLION.txt`

A raw digit data file intended to provide source data for the digit-pool processing workflow.

The relationship between this file and the generated digit sequence depends on the implementation of `random_digits_pool.py`.

The digit data is kept separate from the main utility module rather than embedding a large raw dataset directly into `core.py`.

---

## 🔧 Module: `core.py`

The `core.py` module contains the main functionality of `abobakr_tools`.

The following sections describe the functions, classes, and experimental systems present in the provided implementation.

### 1. Constants & Global State

The module defines shared constants and state used by different utilities.

- `DIGIT_MAP` — maps digit characters from `"0"` through `"9"` to their corresponding integer values.
- `RANDOM_DIGITS_POOL_RAW` — contains a raw digit string used by the current collection conversion implementation.
- `module_directory` — identifies the directory containing the module.
- `random_digits_script_path` — identifies the path to `random_digits_pool.py`.
- `random_digit_pool` — stores the digit values used by the pseudo-random number generation system.
- `random_digit_index` — tracks the current position within the digit pool.
- `events` — stores the loaded security event data.
- `window_start` — tracks the current event-processing window.
- `users_attempts` — stores event types grouped by username.
- `login_attempts_count` — tracks the number of events processed by the counting function.
- `reached_end` — tracks a condition used by the event-processing workflow.

Some of these variables represent mutable module-level state. Their behavior therefore depends on the order in which functions are called and the current state of the module.

### 2. Core Sequence Utilities

Functions for manually processing iterables and generating numeric sequences.

- `get_sequence_length(items)` — counts the items in an iterable without using `len()`.
- `get_sequence_sum(numbers)` — calculates the sum of numeric items without using `sum()`.
- `generate_sequence(stop_value)` — generates a list of integers starting at zero and progressing toward the specified stop value.
- `generate_bounded_range(start_value, stop_value)` — generates a list of integers from the specified start value toward the stop value.

These functions provide practice with iteration, counters, accumulation, conditional logic, and sequence generation.

### 3. String & List Manipulation

Functions for examining, modifying, and processing strings and lists.

- `trim_string(text)` — removes leading and trailing space characters.
- `remove_spaces(text)` — removes space characters from a string.
- `reverse_items(items)` — returns the items in reverse order.
- `append_to_list(items, item)` — appends an item to a list.
- `remove_all_occurrences(items, item)` — removes occurrences of an item from a list.
- `count_occurrences(items, item)` — counts occurrences of an item.
- `find_first_index(items, item)` — finds the first matching index and returns it.
- `check_all_results_are_different(results)` — checks whether all items in a collection are different.
- `print_items(items)` — prints each item on a separate line.
- `list_to_string(items)` — combines iterable items into a single string.
- `convert_speech_to_words(speech)` — splits existing text into word segments using custom indexing and string-processing logic.
- `text_replace(text, index, speech, Placeholder_text)` — removes a specified number of characters starting at an index and inserts replacement text.
- `insert_text_after_in_file(file, insert_thing, after_thing)` — reads a file, searches for matching text occurrences, and returns modified file content with inserted text.

These functions provide practice with indexing, slicing, string construction, list mutation, iteration, and file reading.

The file insertion function constructs and returns modified content; it does not write the modified result back to the original file.

The text-processing implementations are intentionally simple and may have limitations involving repeated characters, whitespace, indexing, line boundaries, and other edge cases.

### 4. Type Checking & Parsing

Functions for inspecting text and manually converting numeric strings.

- `is_integer_format(text)` — checks whether a string follows the implementation's integer format.
- `is_number(text, type_number)` — checks for digit characters and certain decimal patterns.
- `contains_digit(text)` — checks whether a string contains a digit.
- `string_to_integer(text)` — converts integer-formatted text into an integer using a custom digit map and arithmetic.
- `string_to_float(text)` — converts decimal-formatted text into a numeric value using custom parsing and arithmetic.

The conversion functions return an empty string for invalid input in the cases handled by their implementations.

These functions are intended to practice character inspection, numeric parsing, digit mapping, accumulation, and decimal representation rather than simply relying on Python's standard conversion functions.

Their accepted input formats and edge cases may differ from `int()` and `float()`.

### 5. Input Helpers

Functions for collecting and validating user input.

- `read_integer(message)` — repeatedly requests input until the custom integer conversion accepts it.
- `read_float(message)` — repeatedly requests input until the custom numeric conversion accepts it.
- `read_non_numeric_string(message)` — requests a non-empty string that is not recognized as an integer.
- `print_divider(length)` — prints a divider line of a specified length.

These utilities provide practice with input handling, validation loops, string processing, and function composition.

### 6. Collection Conversion

The module provides both class-based and standalone collection conversion implementations.

#### `CollectionConverter`

A class that stores an iterable in `self.items` and provides conversion methods.

- `to_tuple()` — converts the stored iterable into a tuple.
- `to_list()` — converts the stored iterable into a list.
- `to_set()` — converts the stored iterable into a set using the current placeholder-element approach.

#### Standalone conversion functions

- `to_tuple(items)` — constructs a tuple by iterating over the input.
- `to_list(items)` — constructs a list by iterating over the input.
- `to_set(items)` — constructs a set using the current placeholder-element approach.
- `to_dict(*items)` — creates a dictionary from key-value pairs.

This section provides practice with iteration, collection construction, uniqueness, key-value relationships, and class-based organization.

The set conversion implementations use `RANDOM_DIGITS_POOL_RAW` as a placeholder and remove it from the result afterward. This approach has limitations if the input itself contains the placeholder value, so it should be understood as an experimental implementation rather than a general-purpose conversion utility.

### 7. Iteration & Mapping Utilities

Functions for working with dictionary entries and indexed sequence elements.

- `get_dict_pairs(dictionary)` — returns dictionary key-value pairs as a tuple of `(key, value)` pairs.
- `get_indexed_items(items)` — returns indexed items as a tuple of `(index, item)` pairs.

These functions explore the logic behind operations similar to `dict.items()` and `enumerate()`.

The current indexed iteration implementation relies on sequence length and indexing, so it is intended for indexable collections rather than arbitrary one-pass iterators.

### 8. Set Operations

Functions for performing common set operations.

- `set_union(first_set, second_set)` — returns the union of two sets.
- `set_intersection(first_set, second_set)` — returns the intersection of two sets.
- `set_difference(first_set, second_set)` — returns the difference between two sets.
- `set_symmetric_difference(first_set, second_set)` — returns the symmetric difference between two sets.

These functions provide practice with set relationships and Python's set operators.

Unlike some of the other utilities, these functions directly use Python's existing set operators rather than manually reproducing their underlying algorithms.

### 9. Zipping Utilities

Functions for combining multiple sequences.

- `get_shortest_length(sequences)` — finds the shortest sequence length among the supplied sequences.
- `zip_as_list(*sequences)` — combines corresponding items into a list of tuples.
- `zip_as_set(*sequences)` — combines corresponding items into a set of tuples.

These functions explore sequence indexing, tuple construction, iteration across multiple sequences, and behavior similar to Python's `zip()`.

The current implementation assumes that at least one sequence is provided and that the sequences support indexing and length calculation. Empty input and arbitrary iterators are not fully handled.

### 10. Pseudo-Random Number Generation

The module contains an experimental pseudo-random number generation system that uses digit values as seed data and applies a simple arithmetic transformation to generate integers.

Its main functions are:

- `generate_random_digit_pool()` — executes the supporting digit-pool script and converts its output into the current digit pool.
- `generate_next_random_value(start, stop, seed)` — calculates a value within the specified inclusive bounds using a seed and an arithmetic transformation.
- `get_pseudo_random_int(start, stop)` — obtains a seed digit from the current pool and generates an integer within the requested range.

The module maintains shared state through:

- `random_digit_pool` — the current collection of seed digits.
- `random_digit_index` — the current position in that collection.
- `random_digits_script_path` — the path to the supporting script.

The general processing flow is:

```text
random_digits_pool.py
        │
        ▼
Digit sequence output
        │
        ▼
generate_random_digit_pool()
        │
        ▼
random_digit_pool
        │
        ▼
generate_next_random_value()
        │
        ▼
get_pseudo_random_int()
```

The provided implementation contains both a `PseudoRandomGenerator` class and standalone functions that implement similar operations. The standalone functions are the primary functions used by the current library utilities.

The system provides practice with:

- Subprocess execution.
- Digit processing and conversion.
- Module-level state.
- Index management.
- Arithmetic transformations.
- Inclusive numeric bounds.
- Coordination between modules.

**Important limitations:**

- The arithmetic transformation is simple and does not guarantee a statistically sound distribution.
- The generated values should not be assumed to be unpredictable.
- The implementation is not cryptographically secure.
- The current subprocess invocation explicitly uses `python3.14`.
- The module generates the digit pool during initialization, which means importing it can execute an external process.
- The behavior when the digit pool is empty or the requested range is invalid is not fully handled.

This system is intended for learning purposes and is not a replacement for Python's `random` or `secrets` modules.

### 11. Mathematical Helpers

Basic mathematical utilities implemented using other library functions.

- `calculate_average(numbers)` — calculates the arithmetic mean by dividing the custom sum by the custom sequence length.

The function is implemented using a lambda expression and combines `get_sequence_sum()` with `get_sequence_length()`.

It provides practice with function composition and basic arithmetic.

An empty input is not handled explicitly, so calculating an average of an empty collection raises a division-by-zero error.

### 12. Python Script Runner

The module contains a utility for executing Python files directly inside a directory.

- `run_python_folder(folder_path)` — resolves the supplied directory path, discovers Python files directly inside it, executes them through subprocesses, prints their standard output and standard error, and prints a completion message.

The implementation uses:

- `pathlib.Path` for filesystem path handling.
- `Path.resolve()` for path resolution.
- `Path.glob("*.py")` for discovering Python files.
- `subprocess.run()` for process execution.
- Captured standard output and standard error for displaying execution results.

The basic workflow is:

```text
Directory path
      │
      ▼
Resolve directory
      │
      ▼
Find direct *.py files
      │
      ▼
Execute each file
      │
      ▼
Print captured output
      │
      ▼
Report completion
```

The runner provides practical experience with filesystem paths, file discovery, subprocess execution, and output handling.

The current implementation has several limitations:

- It processes Python files directly inside the selected directory rather than recursively searching all subdirectories.
- It uses the `python3.14` command explicitly.
- It does not stop automatically when a child process exits with an error.
- It is intended for trusted scripts, since executing Python files can perform arbitrary operations on the host system.

This utility is an educational exercise rather than a complete process-management tool.

### 13. Security Event Analysis: `soc_analyst`

The module also contains an experimental security event analysis workflow that reads structured JSON event data, processes timestamped events, counts user activity, and records messages through Python's logging system.

Its main functions are:

- `create_events(events_file_path)` — reads a JSON file and loads the parsed event data into the global `events` variable.
- `count_user_attempts(window_start, window_end)` — processes a slice of the loaded events, groups event types by username, and updates the login-attempt counter.
- `get_event_time(value)` — parses an event's timestamp into a `datetime` object using the expected timestamp format.
- `analyze_events(events_file_path)` — coordinates event loading, timestamp processing, time-window calculations, activity counting, and logging.

The implementation uses:

- `json` for reading structured event data.
- `datetime` and `timedelta` for timestamp parsing and time-window calculations.
- `logging` for recording analyzed activity.
- `pathlib.Path` for file path handling.
- Dictionaries and lists for storing events and grouping user activity.
- Global state for tracking the current processing position and counters.

#### Event processing workflow

```text
JSON event file
      │
      ▼
Load event data
      │
      ▼
Parse timestamps
      │
      ▼
Process time windows
      │
      ▼
Group events by username
      │
      ▼
Count login-related events
      │
      ▼
Classify activity
      │
      ▼
Write log records
```

The current implementation classifies the number of login-related events in a processing window using the following thresholds:

- **INFO:** One or fewer login-related events.
- **WARNING:** Two to four login-related events.
- **CRITICAL:** More than four login-related events.

The analyzer provides practice with JSON parsing, timestamp handling, event processing, dictionaries, counters, mutable state, and logging.

**Important limitations:**

- The expected JSON data must match the structure used by the implementation.
- Timestamps must follow the format expected by `get_event_time()`.
- The implementation relies on the ordering and contents of the event data.
- Event loading, time-window boundaries, and the shared state used by the processing loop require further testing.
- The current implementation is experimental and should not be relied upon as a production security monitoring or alerting system.

The purpose of this component is to practice combining Python fundamentals into a more complex event-processing workflow.

---

## 🔄 Random Digit Generation

The pseudo-random number generation system uses a supporting script to produce digit data that the main module consumes.

Its general workflow is:

```text
random_digits_pool.py
        │
        ▼
Digit sequence output
        │
        ▼
generate_random_digit_pool()
        │
        ▼
random_digit_pool
        │
        ▼
get_pseudo_random_int()
```

The raw digit data file is part of the intended data-processing workflow. The supporting script is responsible for producing the output consumed by the main module.

The system is primarily educational and provides opportunities to practice:

- File processing.
- Subprocess execution.
- Numeric conversion.
- Global state management.
- Indexing and boundary handling.
- Arithmetic operations.
- Pseudo-random generation logic.

The implementation is experimental and is not intended for security-sensitive applications or as a replacement for Python's standard random-number generation tools.

---

## 🐧 Linux Runner

The library includes a `run_python_folder()` utility for practicing process execution and filesystem path handling.

The function accepts a path to a directory containing Python files. It resolves the path, finds files matching the `*.py` pattern directly inside the directory, and executes each file using an external Python interpreter.

The basic execution flow is:

```text
Directory path
      │
      ▼
Resolve path
      │
      ▼
Discover *.py files
      │
      ▼
Run each Python file
      │
      ▼
Capture stdout and stderr
      │
      ▼
Print results
      │
      ▼
Completed
```

The implementation uses `pathlib.Path` and `subprocess.run()` to handle filesystem operations and process execution.

It provides practical experience with:

- Filesystem path resolution.
- File and directory handling.
- File extension matching.
- Directory iteration.
- Subprocess execution.
- Capturing process output.
- Executing external applications.

The current implementation uses the `python3.14` command explicitly and does not recursively discover Python files in nested directories.

The runner is a learning utility rather than a general-purpose process manager.

---

## 🎯 Purpose & Philosophy

This repository is primarily a record of my learning process.

The code prioritizes **understanding and clarity of logic** over performance, brevity, or following advanced Python conventions.

### Why Manual Implementations?

Instead of only learning how to use a function, I sometimes implement a simplified version myself to understand the logic behind it.

For example, implementing a function similar to `len()` helps me practice:

- Iteration.
- Counters.
- Return values.
- Working with sequences and iterables.
- Breaking an operation down into individual steps.

The same approach is used when practicing concepts related to:

- `len()`
- `sum()`
- `range()`
- `enumerate()`
- `dict.items()`
- `zip()`
- Collection conversion.
- String manipulation.
- List manipulation.
- Input parsing.
- Set operations.
- Basic mathematical operations.

The library also includes practical exercises that combine these fundamentals with other Python features, such as:

- File handling.
- Text processing.
- Subprocess execution.
- Pseudo-random number generation.
- JSON processing.
- Timestamp handling.
- Logging.
- Security event analysis.

### Why Not Always Use Pythonic Solutions?

Python provides concise and powerful syntax, but concise code can sometimes hide the underlying logic while learning.

During these exercises, I intentionally write more explicit code so that I can focus on understanding what is happening at each step.

This **does not** mean that manual implementations are better than Python's built-in functions.

In real-world projects, Python's built-in and standard-library solutions should normally be preferred for readability, reliability, and performance.

### Learning Through Reimplementation

The library is gradually expanded as I learn new Python concepts and operations.

When I encounter an operation that I understand well enough to recreate using the concepts I have learned, I may implement a simplified version of it manually.

More advanced operations may be postponed until I have learned the concepts required to implement them properly.

The same learning approach applies to larger utilities. By combining familiar concepts into small programs, I can explore how functions, modules, classes, files, and external processes work together.

This keeps the library connected to my actual learning progress rather than attempting to reproduce Python's functionality all at once.

### Future Plan

`abobakr_tools` is a learning-oriented project.

Once I finish learning the Python fundamentals that I am using this library to practice, I plan to stop actively developing the library and move toward writing normal, idiomatic Python code.

The experience gained from these implementations and practical projects will remain useful even after I move on to more conventional approaches.

---

## 🏗️ Project Structure

The repository is organized into a package development directory and a collection of practical projects.

```text
python-learning/
│
├── .gitignore
├── README.md
│
├── abobakr_tools_/
│   ├── pyproject.toml
│   │
│   └── abobakr_tools/
│       ├── __init__.py
│       ├── core.py
│       ├── random_digits_pool.py
│       └── RANDOM_DIGITS_RAW_1_MILLION.txt
│
└── projects/
    ├── calculator.py
    ├── rock_paper_scissors.py
    └── to_do_list.py
```

### Package Development Directory

```text
abobakr_tools_/
├── pyproject.toml
└── abobakr_tools/
    ├── __init__.py
    ├── core.py
    ├── random_digits_pool.py
    └── RANDOM_DIGITS_RAW_1_MILLION.txt
```

The `abobakr_tools_/` directory contains the package configuration and the actual `abobakr_tools` Python package.

The `pyproject.toml` file defines the package's project and build configuration.

### Projects Directory

```text
projects/
├── calculator.py
├── rock_paper_scissors.py
└── to_do_list.py
```

The `projects/` directory contains practical programs that apply Python fundamentals and may use functions from the custom library.

These projects are separate from the library itself and demonstrate how programming concepts can be applied to complete command-line applications.

---

## 🚫 Git Ignore

The repository uses `.gitignore` to exclude generated files, Python cache files, virtual environments, environment files, and package build metadata that should not be tracked.

Examples include:

```text
__pycache__/
*.py[cod]
*.egg-info/
.venv/
venv/
.env
```

These files and directories are generated locally or contain environment-specific data and are not part of the source code that the repository is intended to track.

---

> **Note:** Some functions intentionally reproduce or approximate functionality already available in Python. Others are practical utilities and experimental implementations developed to practice combining Python concepts. The library prioritizes learning and understanding rather than production readiness, performance, or replacing established Python tools.
