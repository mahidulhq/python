# Simple Password Generator

Generates random passwords from user-specified length using all character sets.

## Python Libraries Used

- `string` - Character sets (uppercase, lowercase, digits, punctuation)
- `random` - Shuffle and random selection

## Features

- Interactive length input
- Uses full character pool:
  - Uppercase: `A-Z`
  - Lowercase: `a-z`
  - Digits: `0-9`
  - Punctuation: `!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~`
- Shuffles complete character set before selection

## Usage

```bash
python passwdgenerator.py
```

1. Enter desired password length
2. Receive random password instantly

## Example

```
Enter the pass length: 12
Output: kX9#mP$2vNq@
```

## Code Flow

```
Input length → Combine all char sets → Shuffle → Take first N chars → Print
```

## Limitations

- No validation on input length
- No error handling
- Single password generation
- Uses first N chars after shuffle (not cryptographically secure)
- Console-only output