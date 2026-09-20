# 📱 OLX iPhone Deal Scraper & Monitor

An automated web scraping pipeline built in Python that monitors the OLX marketplace for underpriced iPhones and sends real-time alert notifications directly to a Discord server.

## 🚀 Features
* **Automated Browsing:** Uses **Selenium WebDriver** to navigate pages and handle cookie pop-ups.
* **Deal Filtering:** Evaluates prices using custom rule-based logic to spot iPhones listed below market value.
* **Duplicate Prevention:** Tracks previously scraped listings in `linki.txt` to ensure alerts are only sent for new listings.
* **Discord Integration:** Sends instant notifications with the item link via a Discord webhook/bot.

## 🛠️ Tech Stack
* **Language:** Python
* **Web Scraping:** Selenium
* **Integrations:** discord.py

## ⚙️ How to Run
1. Clone the repository and navigate to the directory.
2. Install the required Python packages:
   ```bash
   pip install selenium discord
   ```
3. Ensure you have the Chrome WebDriver installed and added to your system PATH.
4. Run the scraper:
   ```bash
   python main.py
   ```
