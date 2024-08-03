from PIL import Image
import os

def combine_images(image_paths, max_width=1000, padding=5):
    # Load all images
    images = [Image.open(img).convert("RGBA") for img in image_paths]
    
    # Calculate the total height and width required for the combined image
    rows = []
    current_row = []
    current_width = 0
    max_height_in_row = 0
    
    for img in images:
        if current_width + img.width + padding > max_width:
            # Finish the current row and start a new row
            rows.append((current_row, max_height_in_row))
            current_row = []
            current_width = 0
            max_height_in_row = 0
        
        current_row.append(img)
        current_width += img.width + padding
        if img.height > max_height_in_row:
            max_height_in_row = img.height
    
    # Add the last row
    rows.append((current_row, max_height_in_row))
    
    # Calculate total dimensions
    total_height = sum(row[1] + padding for row in rows) - padding
    total_width = max_width
    
    # Create a new image with the calculated dimensions
    combined_img = Image.new('RGBA', (total_width, total_height), color=(255, 255, 255, 0))
    
    y_offset = 0
    for row, height in rows:
        x_offset = 0
        for img in row:
            combined_img.paste(img, (x_offset, y_offset))
            x_offset += img.width + padding
        y_offset += height + padding
    
    return combined_img

# Usage example
image_folder = input('/path/to/your/images: ')
name_image = input('name_combine_image.png: ')

image_paths = [os.path.join(image_folder, img) for img in os.listdir(image_folder) if img.endswith(('png', 'jpg', 'jpeg'))]
combined_image = combine_images(image_paths)
combined_image.save(f'{name_image}.png')
combined_image.show()
