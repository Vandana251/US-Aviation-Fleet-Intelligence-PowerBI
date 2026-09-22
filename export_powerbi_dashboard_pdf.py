"""
Export all 10 Power BI Dashboard pages to high-resolution screenshots and compile into:
1. PowerBI_Aviation_Dashboard_Report.pdf (16:9 Presentation / Document)
2. powerbi_dashboard_slides/ (Individual PNGs for slides / LinkedIn images)
"""

import subprocess
import os
import time
from PIL import Image

EDGE_PATH = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
HTML_FILE = os.path.abspath("aviation_dashboard.html")
OUTPUT_DIR = "powerbi_dashboard_slides"
OUTPUT_PDF = "PowerBI_Aviation_Dashboard_Report.pdf"

os.makedirs(OUTPUT_DIR, exist_ok=True)

print("Capturing 10 Power BI Dashboard Pages using Microsoft Edge Headless...")

image_files = []

for page in range(1, 11):
    output_png = os.path.join(OUTPUT_DIR, f"powerbi_page_{page:02d}.png")
    url = f"file:///{HTML_FILE.replace(os.sep, '/')}?page={page}"
    print(f"  Capturing Page {page:02d} / 10 -> {output_png}...")
    
    cmd = [
        EDGE_PATH,
        "--headless",
        "--disable-gpu",
        "--hide-scrollbars",
        f"--screenshot={output_png}",
        "--window-size=1920,1080",
        url
    ]
    
    subprocess.run(cmd, check=True)
    time.sleep(0.5)
    image_files.append(output_png)

print("\nCompiling all 10 pages into high-resolution Power BI PDF Report...")

# Open images and convert to RGB
pil_images = []
for img_path in image_files:
    if os.path.exists(img_path):
        img = Image.open(img_path).convert('RGB')
        pil_images.append(img)

if pil_images:
    # Save as multi-page PDF
    pil_images[0].save(
        OUTPUT_PDF,
        save_all=True,
        append_images=pil_images[1:],
        quality=95,
        optimize=True
    )
    print(f"[DONE] Successfully created: {OUTPUT_PDF}")
    print(f"[DONE] File size: {os.path.getsize(OUTPUT_PDF) / 1024:.1f} KB")
    print(f"[DONE] Saved {len(pil_images)} individual page images to: {OUTPUT_DIR}/")
else:
    print("[ERROR] No images captured.")
