# 🔗 LinkedIn Automation Tool: Expand Your Network, Effortlessly

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/Selenium-Automated%20Browser-brightgreen.svg)](https://www.selenium.dev/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-informational.svg)](https://www.linkedin.com/)
[![Maintainability](https://api.codeclimate.com/v1/badges/e812551f554544577884/maintainability)](https://codeclimate.com/github/your-repo/your-project) [![Coverage](https://img.shields.io/coveralls/github/your-repo/your-project.svg?style=flat-square)](https://coveralls.io/github/your-repo/your-project) ## 🚀 Level Up Your LinkedIn Networking

Tired of spending countless hours manually connecting with potential clients, partners, or candidates on LinkedIn?  This powerful Python script, driven by Selenium, automates your LinkedIn outreach, helping you to:

* **Expand your network faster:** Connect with hundreds of relevant professionals in a fraction of the time.
* **Target your ideal connections:** Reach out to specific profiles based on your search criteria.
* **Personalize your approach:** Send customized connection requests with tailored notes.
* **Save valuable time:** Focus on what matters most – building relationships and closing deals.

**This isn't just a script; it's your automated LinkedIn growth engine.**

## ✨ Key Features

* **Intelligent Automation:** Uses Selenium to simulate real user behavior, bypassing LinkedIn's anti-automation measures.
* **Customizable Connection Requests:** Includes the ability to add personalized notes to your connection requests, increasing acceptance rates.
* **Error Handling & Resilience:** Gracefully handles common issues like popups and connection limits, ensuring smooth operation.
* **Efficiency & Speed:** Streamlines the connection process, allowing you to connect with a large number of people quickly and efficiently.
* **Simple Setup:** Easy to install and configure, with clear instructions.
* **Detailed Logging:** Provides console output of the connection process.

## ⚙️ How It Works

This script leverages the Selenium WebDriver to control a Chrome browser, automating the following steps:

1.  **Login:** Securely logs into your LinkedIn account using your provided credentials.
2.  **Navigate:** Goes to your LinkedIn "My Network" page to find potential connections.
3.  **Find and Connect:**
    * Locates "Connect" buttons on the page.
    * Clicks each button to send a connection request.
    * Detects if an "Add a note" popup appears.
    * If a note is required, adds a personalized message (which you can customize).
    * Sends the connection request.
4.  **Error Handling:** Skips connections if a popup or overlay prevents the button from being clicked.
5.  **Completion:** Displays a "Done sending requests" message and closes the browser.

## 🎯 Target Audience

This tool is perfect for:

* **Sales Professionals:** Generate leads and connect with potential clients.
* **Recruiters:** Find and connect with top talent.
* **Business Development Managers:** Expand your network and build strategic partnerships.
* **Entrepreneurs:** Connect with investors, mentors, and industry experts.
* **Anyone looking to grow their LinkedIn network efficiently and effectively!**

## 🛠️ Installation

1.  **Prerequisites:**
    * [Python 3.6+](https://www.python.org/downloads/) installed on your system.
    * [Google Chrome](https://www.google.com/chrome/) browser installed.
    * (Optional but Recommended) A Python virtual environment (e.g., `venv`, `conda`) to keep your dependencies isolated.

2.  **Install Dependencies:**

    ```bash
    pip install selenium getpass
    ```

3.  **Download ChromeDriver:**
    * Download the ChromeDriver that matches your Chrome version from [https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads).
    * Extract the `chromedriver` executable and place it in a directory that is in your system's `PATH` (e.g., `/usr/local/bin` on Linux/macOS, or the `Scripts` directory of your Python installation on Windows), or in the same directory as your script.

## 🚀 Quick Start

1.  **Clone the Repository (Optional):**
    * If you have the code in a git repository, clone it:
        ```bash
        git clone [https://github.com/your-repo/your-project.git](https://github.com/your-repo/your-project.git)  # Replace with your repo URL
        cd your-project
        ```

2.  **Run the Script:**

    ```bash
    python your_script_name.py  # Replace with the actual name of your Python script (e.g., main.py)
    ```

3.  **Follow the Prompts:**
    * The script will prompt you to enter your LinkedIn email and password.  Your password will be hidden for security.
    * The script will then automate the connection process.

## ⚙️ Configuration

* **Personalize Your Connection Message:** Modify the `note_box.send_keys()` line in the script to change the message sent with your connection requests.  For example:

    ```python
    note_box.send_keys("Hi [Name], I'm impressed with your work in [Industry].  I'd love to connect and learn more.")
    ```

* **Target Specific Connections:** Modify the script to navigate to a specific LinkedIn search or group page to target your connection requests more precisely.  Change the `driver.get()` calls.

## ⚠️ Disclaimer & Important Notes

* **Use Responsibly:** This script is intended to help you grow your LinkedIn network efficiently.  Please use it responsibly and respect LinkedIn's terms of service.  Avoid excessive or spammy behavior, which could lead to account restrictions.
* **Account Security:** The script requires you to enter your LinkedIn credentials.  While the password input is hidden, ensure you are running the script in a secure environment.  Consider using a dedicated LinkedIn account for automation purposes.
* **LinkedIn Changes:** LinkedIn's website structure may change, which could cause the script to break.  I am committed to maintaining the script and providing updates as needed.  If you encounter issues, please report them.
* **Rate Limiting:** LinkedIn has connection request limits.  This script does not implement rate limiting, so it's crucial to use it with caution and avoid sending too many requests in a short period.  You can add `time.sleep()` calls to slow down the process.

## 🤝 Contributing

Contributions, bug reports, and feature requests are welcome!  Please feel free to open an issue or submit a pull request.

## 📄 License

[MIT License](LICENSE)  ## 📞 Contact

[Your Name/Company Name]
[Your Website/Email/LinkedIn Profile]

---

**Ready to supercharge your LinkedIn networking?** Give the LinkedIn Automation Tool a try and experience the power of automated growth!
