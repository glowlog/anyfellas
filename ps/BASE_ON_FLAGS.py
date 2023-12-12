from PIL import Image
import os

def overlay_images(base_image_path, flags_directory):
    # Open the base image with an alpha channel
    base_image = Image.open(base_image_path).convert("RGBA")

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

            # Ensure the flag image is in RGBA mode
            flag_image = flag_image.convert("RGBA")

            # Resize the flag image to fit the base image if needed
            flag_image = flag_image.resize(base_image.size, Image.BICUBIC)

            # Create a new image with an "RGBA" mode for the composite
            composite_image = Image.new("RGBA", base_image.size, (0, 0, 0, 0))

            # Paste the flag image onto the composite image with transparency
            composite_image.paste(flag_image, (0, 0), flag_image)

            # Paste the base image onto the composite image using the alpha channel of the base image
            composite_image.paste(base_image, (0, 0), base_image)

            # Convert to "RGB" before saving (JPEG does not support alpha channel)
            composite_image = composite_image.convert("RGB")

            # Save the result
            output_path = os.path.join(flags_directory, f"BASE_{os.path.splitext(flag_file)[0]}.jpg")
            composite_image.save(output_path, "JPEG")

            print(f"Overlay created: {output_path}")

if __name__ == "__main__":
    script_directory = os.path.dirname(os.path.realpath(__file__))
    base_image_path = os.path.join(script_directory, "BASE.png")
    flags_directory = os.path.join(script_directory, "FLAGS")

    overlay_images(base_image_path, flags_directory)

