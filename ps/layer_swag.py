from PIL import Image
import os

def overlay_images(flags_directory, jersey_directory, base_image_path, output_directory):
    # Ensure the FLAGS directory exists
    if not os.path.exists(flags_directory):
        print(f"Error: Directory {flags_directory} not found.")
        return

    # Ensure the JERSEY directory exists
    if not os.path.exists(jersey_directory):
        print(f"Error: Directory {jersey_directory} not found.")
        return

    # Ensure the BASE image exists
    if not os.path.exists(base_image_path):
        print(f"Error: BASE image {base_image_path} not found.")
        return

    # Loop through each file in the FLAGS directory
    for i, flag_file in enumerate(os.listdir(flags_directory)):
        if flag_file.endswith(".jpg") or flag_file.endswith(".jpeg"):
            flag_path = os.path.join(flags_directory, flag_file)

            # Open the flag image
            flag_image = Image.open(flag_path)

            # Ensure the flag image is in RGBA mode
            flag_image = flag_image.convert("RGBA")

            # Loop through each file in the JERSEY directory
            for j, jersey_file in enumerate(os.listdir(jersey_directory)):
                if jersey_file.endswith(".png"):
                    jersey_path = os.path.join(jersey_directory, jersey_file)

                    # Open the jersey image
                    jersey_image = Image.open(jersey_path)

                    # Ensure the jersey image is in RGBA mode
                    jersey_image = jersey_image.convert("RGBA")

                    # Open the base image
                    base_image = Image.open(base_image_path)

                    # Ensure the base image is in RGBA mode
                    base_image = base_image.convert("RGBA")

                    # Resize the flag and jersey images to fit the base image if needed
                    flag_image = flag_image.resize(base_image.size, Image.BICUBIC)
                    jersey_image = jersey_image.resize(base_image.size, Image.BICUBIC)

                    # Create a new image with an "RGBA" mode for the composite
                    composite_image = Image.new("RGBA", base_image.size, (0, 0, 0, 0))

                    # Paste the flag image onto the composite image with transparency
                    composite_image.paste(flag_image, (0, 0), flag_image)

                    # Paste the jersey image onto the composite image with transparency
                    composite_image.paste(jersey_image, (0, 0), jersey_image)

                    # Paste the base image onto the composite image using the alpha channel as a mask
                    composite_image.paste(base_image, (0, 0), base_image)

                    # Convert to "RGB" before saving (JPEG does not support alpha channel)
                    composite_image = composite_image.convert("RGB")

                    # Save the result to the output directory with a sequential name
                    output_path = os.path.join(output_directory, f"eufella{i:02d}_{j:02d}.jpg")
                    composite_image.save(output_path, "JPEG")

                    print(f"Overlay created: {output_path}")

if __name__ == "__main__":
    script_directory = os.path.dirname(os.path.realpath(__file__))
    flags_directory = os.path.join(script_directory, "FLAGS")
    jersey_directory = os.path.join(script_directory, "JERSEY")
    base_image_path = os.path.join(script_directory, "BASE.png")
    output_directory = os.path.join(script_directory, "out")

    # Ensure the output directory exists, create if it doesn't
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    overlay_images(flags_directory, jersey_directory, base_image_path, output_directory)
