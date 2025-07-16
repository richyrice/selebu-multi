import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def youtube_search_and_watch(keyword, video_url):
    # Konfigurasi Chrome
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sanbox")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    # Inisialisasi WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    
    try:
        # 1. Pencarian Keyword
        driver.get("https://www.youtube.com")
        print(f"Mencari: '{keyword}'...")
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "search_query"))
        )
        search_box.send_keys(keyword + Keys.RETURN)
        time.sleep(5)

        # 2. Scroll 2x
        for _ in range(2):
            driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight)")
            time.sleep(5)

        # 3. Buka Video Spesifik
        print(f"Membuka video: {video_url}")
        driver.get(video_url)
        time.sleep(10)  # Tonton video selama 10 detik

    except Exception as e:
        print(f"Error: {e}")
    finally:
        driver.quit()
        print("Selesai!")

# Contoh penggunaan
youtube_search_and_watch(
    keyword="urang sundal sunda",
    video_url="https://www.youtube.com/watch?v=dR6biqejGfM"
)
