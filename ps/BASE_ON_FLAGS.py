from PIL import Image
import os

def overlay_images(base_image_path, flags_directory):
    # Open the base image
    base_image = Image.open(base_image_path)

    # Ensure the FLAGS directory exists
    if not os.path.exists(flags_directory):
        print(f"Error: Directory {flags_directory} not found.")
        return

    # Loop through each file in the FLAGS directory
    for flag_file in os.listdir(flags_directory):
        if flag_file.endswith(".jpg") or flag_file.endswith(".jpeg"):
            flag_path = os.path.join(flags_directory, flag_file)

            # Open the flag image
            flag_image = Image.open(flag_path)

            # Resize the flag image to fit the base image if needed
            flag_image = flag_image.resize(base_image.size, Image.ANTIALIAS)

            # Composite the images
            composite_image = Image.alpha_composite(base_image.convert("RGBA"), flag_image.convert("RGBA"))

            # Save the result
            output_path = os.path.join(flags_directory, f"BASE_{os.path.splitext(flag_file)[0]}.jpg")
            composite_image.save(output_path, "JPEG")

            print(f"Overlay created: {output_path}")

if __name__ == "__main__":
    base_image_path = "BASE.jpg"
    flags_directory = "/FLAGS/"

    overlay_images(base_image_path, flags_directory)
