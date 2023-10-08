# Instagram Automation Script

This Python script automates interactions on Instagram, such as liking photos, leaving comments, and following users, based on a list of hashtags. It uses the Selenium library to control a web browser and perform these actions. Below is a step-by-step guide on how to use this script.

## Prerequisites

Before using the script, make sure you have the following:

1. **Python**: Ensure you have Python installed on your system.

2. **Chromedriver**: Download and install Chromedriver compatible with your Chrome browser. Update the `chromedriver_path` variable in the script with the path to the Chromedriver executable.

3. **Selenium**: Install the Selenium library using `pip`:
   ```
   pip install selenium
   ```

## Configuration

In the script, you need to configure the following variables before running:

- `chromedriver_path`: Set this to the path where your Chromedriver executable is located.

- `username` and `password`: Enter your Instagram username and password in the respective fields.

- `hashtag_list`: Add the hashtags you want to search for and interact with, separated by commas. For example: `['photography', 'traveling', 'pics']`.

## Usage

1. Clone the repository or download the script.

2. Open the script in a text editor and configure the variables mentioned above.

3. Run the script:
   ```
   python instagram_automation.py
   ```

4. The script will open a Chrome browser, log in to your Instagram account, and start automating interactions based on the hashtags you provided.

## Features

- The script iterates through the provided hashtags and interacts with posts:
  - Likes photos (up to 200 in a row).
  - Leaves random comments.
  - Follows users (if not already followed).

- Random intervals are added to simulate more human-like behavior.

## Reporting

The script will print the following information in the console:

- The number of liked photos.
- The number of comments made.
- The number of users followed.

## Disclaimer

This script is intended for educational and informational purposes. Be cautious when using it to interact with social media platforms. Excessive or unauthorized automation on Instagram may violate their terms of service.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
