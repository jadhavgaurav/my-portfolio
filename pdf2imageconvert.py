import os
from pdf2image import convert_from_path

# 🔧 Configuration
pdf_folder = "certificates"        # Change this to your folder path
output_folder = os.path.join(pdf_folder, "images")  # Output folder for images
poppler_path = r"C:\\poppler-24.08.0\\Library\bin"      # Required on Windows

# 📂 Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# 🔁 Loop through all PDF files in the folder
for filename in os.listdir(pdf_folder):
    if filename.lower().endswith(".pdf"):
        pdf_path = os.path.join(pdf_folder, filename)
        pdf_name = os.path.splitext(filename)[0]

        print(f"📄 Converting: {filename}")
        # Convert each page to image
        images = convert_from_path(pdf_path, dpi=300, poppler_path=poppler_path)

        # Save images
        for i, image in enumerate(images):
            image_filename = f"{pdf_name}_page_{i+1}.jpg"
            image_path = os.path.join(output_folder, image_filename)
            image.save(image_path, "JPEG")

        print(f"✅ Finished: {filename}")

print("🎉 All PDFs converted to JPG images.")
