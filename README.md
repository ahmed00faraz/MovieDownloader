# Selenium Movie Downloader

This Python script automates the process of navigating through download links of movies using Selenium. It automates clicking through the necessary buttons on the website to access and download movie files.

## Features

- Automates the process of downloading movie files by navigating through various pages.
- Uses Selenium to interact with web elements.
- Supports timeout functionality for user input with a default value.

## Requirements

- Python 3.x
- Selenium
- Microsoft Edge WebDriver
- Edge browser installed

## Installation

1. Clone this repository or download the script.

2. Install the required dependencies using pip:
    ```bash
    pip install selenium
    ```

3. Ensure that Microsoft Edge WebDriver is installed. You can download it from the [official Microsoft Edge WebDriver website](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/).

4. Make sure the Edge WebDriver is in your system's `PATH` or specify the location in the script.

## Usage

1. Run the script:
    ```bash
    python movie_downloader.py
    ```

2. You will be prompted to enter the movie link:
    ```bash
    please enter the link of the movie:
    ```

3. The script will automatically open Microsoft Edge, navigate through the required pages, and begin downloading the file.

## How it Works

1. **Input and Setup**: The user provides a URL link for the movie, and the script sets up a Selenium browser instance using Edge.

2. **Navigation**: The script navigates through multiple pages by clicking the required buttons and executing JavaScript.

3. **Verification**: It handles page verification steps automatically by executing JavaScript.

4. **Download**: Once on the download page, the script looks for specific download options and clicks the desired link (default is set to "instant").

5. **Timeout Functionality**: The `get_input_with_timeout` function allows for user input with a default option in case of timeout.

## Notes

- The script is tailored for a specific website structure. Changes to the website's layout might require modifications to the script.
- Ensure that Edge and Edge WebDriver versions match.
  
## Troubleshooting

- If the script fails at any point, it will print `Sorry bro` to indicate an issue in the process (such as an element not being found).
- You may need to adjust the sleep times depending on your internet speed and the responsiveness of the website.
