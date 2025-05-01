from PIL import Image

# Open the image
# image_path = "dashed-line-airplane.webp"  # Change this to your image path

# profile picture
image_path = "profile.jpg"  # Change this to your image path
# image_path = "dashed-line-airplane.webp"  # Change this to your image path

image = Image.open(image_path)

# Define the cropping area (left, top, right, bottom)

# area for dashed-line-airplane.webp
# crop_area = (100, 375, 900, 600)  # Adjust these values as needed
# crop_area = (50, 162, 450, 300)  # Adjust these values as needed

# dimensions for profile picture
crop_area = (1000, 200, 4200, 3200)  

# Crop the image
cropped_image = image.crop(crop_area)

# plane resizer
# resized_img = image.resize((300, 100))

# portfolio resizer
resized_img = cropped_image.resize((300, 300))


# Save the cropped image
# resized_img.save("cropped_airplain_small.webp", "WEBP")
resized_img.save("cropped_profile_small.jpg", "JPEG")

# Show the cropped image (optional)
# cropped_image.show()

print("Cropping completed! Saved as 'cropped.jpg'.")
