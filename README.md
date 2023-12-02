
## Mini Project: Web Scraping with Selenium

### Description
This mini-project focuses on web scraping using Selenium, aiming to retrieve specific information from web pages related to football headlines. The project employs Python and Selenium to automate the browsing process and extract data from a sports news website.

### Objective
The primary goal of this mini-project is to showcase:
- **Web Scraping**: Utilizing Selenium for automated data extraction from web pages.
- **Data Collection**: Gathering football headlines, including titles, subtitles, and links, for analysis or further processing.
- **Pipeline Development**: Demonstrating a simple data pipeline to collect, process, and store scraped information.

### File Structure
```
.
├── main.py     # Main Python script for web scraping
├── README.md                  # Project documentation
└── headline-headless.csv      # CSV file to store scraped data
```

### Usage
1. **Setup**:
   - Install Python and required libraries (`requirements.txt`).
   - Ensure Chrome WebDriver is installed and configured properly.

2. **Generating the Executable:**:
   - Use PyInstaller to create an executable:
    ```bash
    pyinstaller --onefile main.py
    ```
3. **Output**:
   - After generating the executable file, the extracted data will be saved in `f'{os.path.dirname(sys.executable)}/headline-{today}.csv'`.
---

