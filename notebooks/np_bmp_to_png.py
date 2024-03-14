from PIL import Image
import os
from pathlib import Path

def convert_images(in_folder: Path,out_folder, ext):
    # Loop through all files in the input folder
    for in_file in in_folder.glob(ext):
        # if filename.endswith('.tiff'):
            # Open the TIFF image
        # in_file = os.path.join(in_folder, filename)
        img = Image.open(in_file.as_posix())
        out_file = out_folder/Path(in_file.name).with_suffix('.png')
        # Convert and save as PNG in the same folder
        # output_filename = os.path.splitext(filename)[0] + '.png'
        # output_path = os.path.join(in_folder, output_filename)
        img.save(out_file, 'PNG')

        # Remove the original TIFF file
        # os.remove(in_file)

    print(f"Conversion completed. TIFF files from {in_folder} replaced with PNG in {out_folder}")


if __name__ == "__main__":
    in_folder = Path("/home/rs/21CS91R01/datasets/FVC2006/Dbs/DB3_A/")
    # out_folder = Path("/home/rs/21CS91R01/research/fixed-length-fingerprint-extractors/flx/data/iso_encoder_decoder/anguli_imagenet_ist/")
    out_folder = Path("/home/rs/21CS91R01/research/fixed-length-fingerprint-extractors/flx/data/iso_encoder_decoder/FVC2006_DB3A_ist/")
    # convert_images("/home/rs/21CS91R01/research/fixed-length-fingerprint-extractors/notebooks/fvc_dataset/FVC2006DB2_A")
    ext = "*.bmp"
    convert_images(in_folder,out_folder, ext)

