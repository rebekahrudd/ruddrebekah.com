from PIL import Image

# Open the image
# image_path = "dashed-line-airplane.webp"  # Change this to your image path

# profile picture
image_path = "profile.jpg"  # Change this to your image path
image = Image.open(image_path)

# Define the cropping area (left, top, right, bottom)

# area for dashed-line-airplane.webp
# crop_area = (100, 375, 900, 600)  # Adjust these values as needed

# dimensions for profile picture
crop_area = (1000, 200, 4200, 3200)  

# Crop the image
cropped_image = image.crop(crop_area)

# Save the cropped image
cropped_image.save("cropped_profile.jpg", "JPEG")

# Show the cropped image (optional)
cropped_image.show()

print("Cropping completed! Saved as 'cropped.jpg'.")
