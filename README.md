# Rotate Horizontal Photos to Vertical

This Python script automatically rotates horizontal photos to vertical orientation. It processes all JPEG images in an input folder that start with "IMG_" and saves the rotated (or original if already vertical) images to an output folder.

## Features

- Automatically detects horizontal images
- Rotates horizontal images 90 degrees clockwise
- Preserves vertical images without rotation
- Processes multiple images in batch
- Uses relative paths for easy portability

## Requirements

- Python 3.x
- Pillow library

## Installation

1. Clone this repository or download the script.
2. Install the required Pillow library:

   ```
   pip install Pillow
   ```

## Usage

1. Create an `input_images` folder in the same directory as the script.
2. Place your JPEG images (with names starting with "IMG_") in the `input_images` folder.
3. Run the script:

   ```
   python rotate.py
   ```

4. Rotated (and unrotated vertical) images will be saved in an `output_images` folder.

## How it works

1. The script identifies the directory it's running from.
2. It looks for an `input_images` folder in that directory.
3. All files in `input_images` that start with "IMG_" and end with ".jpg" are processed.
4. Each image is checked to see if it's horizontal (width > height).
5. Horizontal images are rotated 90 degrees clockwise.
6. Vertical images are left as-is.
7. All processed images are saved to the `output_images` folder.

## Functions

- `main()`: Orchestrates the entire process.
- `get_image_files(folder)`: Returns a list of image files in the specified folder.
- `open_image(image_path)`: Opens an image file using PIL.
- `is_horizontal(image)`: Checks if an image is horizontal.
- `rotate_image(image)`: Rotates an image 90 degrees clockwise.
- `save_image(image, output_folder, filename)`: Saves an image to the output folder.

## Note

Ensure you have the necessary permissions to read from the input folder and write to the output folder.

## License

This project is open source and available under the [MIT License](LICENSE).
