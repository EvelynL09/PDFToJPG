import os
from pdf2image import convert_from_path

# Set the input and output directories
input_dir = './input/'
output_dir = './output/'

# Loop through all PDF files in the input directory
for pdf_file in os.listdir(input_dir):
    if pdf_file.endswith('.pdf'):
        # Extract the name of the PDF file
        pdf_name = os.path.splitext(pdf_file)[0]

        # Convert the PDF to a list of PIL images
        pdf_path = os.path.join(input_dir, pdf_file)
        images = convert_from_path(pdf_path)

        # Loop through the images and save each one as a JPG
        for i, image in enumerate(images):
            # Create the output file name
            if len(images) > 1:
                output_name = f'{pdf_name}_{i+1}.jpg'
            else:
                output_name = f'{pdf_name}.jpg'
            output_path = os.path.join(output_dir, output_name)

            # Save the image as a JPG
            image.save(output_path, 'JPEG')
