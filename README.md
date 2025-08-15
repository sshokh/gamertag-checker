# Xbox Gamertag Checker

This tool generates random Xbox gamertags, checks their availability using [xboxgamertag.com](https://xboxgamertag.com), and saves any available gamertags into a file.

## Features

- **Random generation** of gamertags with a custom length.
- **First character always a letter** to comply with Xbox rules.
- **Live availability check** using `xboxgamertag.com`.
- **Automatic saving** of available names to `availables.txt`.
- **Rate limit handling** to avoid overwhelming the API.
- **Error handling** for failed requests.

## Getting Started

### Setup

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/gamertag-checker.git
   cd gamertag-checker
   ```

2. Install dependencies:

   ```bash
   pip install colorama threading requests
   ```

3. Start the application:

   ```bash
   python main.py
   ```

   You will be prompted to enter the desired length of gamertags.
   The length must be between **3** and **15** characters.

### Usage

After starting the application, you will be prompted to:

**Enter the length of gamertags**: Insert the length of gamertags you want to check. Input must be an integer (number).

The script will keep running, generating and checking new gamertags until stopped.

## Output

- All available gamertags are stored in `availables.txt`.
- One name per line for easy copying or importing.

## Notes

- The script waits **1 second** between each request to avoid server rate limits.
- On connection errors, it waits **5 seconds** before retrying.
- Xbox username rules: must be 3–15 characters, no starting digit, only letters and numbers.
