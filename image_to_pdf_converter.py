from PIL import Image
import os

# 📁 Folder containing images
image_folder = "certificates"  # Update this path
output_folder = os.path.join(image_folder, "pdfs")
os.makedirs(output_folder, exist_ok=True)

# 📄 Supported image extensions
image_extensions = [".jpg", ".jpeg", ".png"]

# 🔁 Convert each image to individual PDF
for filename in os.listdir(image_folder):
    if os.path.splitext(filename)[1].lower() in image_extensions:
        image_path = os.path.join(image_folder, filename)
        image = Image.open(image_path).convert("RGB")

        pdf_filename = os.path.splitext(filename)[0] + ".pdf"
        pdf_path = os.path.join(output_folder, pdf_filename)

        image.save(pdf_path, "PDF")
        print(f"✅ Converted: {filename} → {pdf_filename}")

print("🎉 All images converted to individual PDFs.")
