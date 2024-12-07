import os
import requests
from bs4 import BeautifulSoup

# URL ของเพจที่มีภาพ
url = "https://www.facebook.com/share/p/19jd1eFptS/"  # ปรับ URL ตามของคุณ

# โฟลเดอร์สำหรับจัดเก็บภาพ
output_folder = "downloaded_images"
os.makedirs(output_folder, exist_ok=True)

# ดึง HTML ของเพจ
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# ค้นหาลิงก์ภาพ
image_tags = soup.find_all("img")
for index, img in enumerate(image_tags):
    img_url = img.get("src")
    if img_url:
        # ดาวน์โหลดภาพ
        img_data = requests.get(img_url).content
        filename = os.path.join(output_folder, f"11-{index}.png")
        with open(filename, "wb") as f:
            f.write(img_data)
        print(f"ดาวน์โหลด: {filename}")
