# pip install ffmpeg-python
import os
from pathlib import Path

#COMPLETELY LOSSLESS IMAGE DOWNSCALER
#SUPPORTS HDR!
#MAIN USE IS FOR AVIF HDR IMAGES
#but AFAIK: Supports JPG, PNG and TIFF
def main():
    # "./your_folder" looks at folder in the same director as the script
    input_folder = r"./input/"
    longest_edge = 1000  # px
    #quality on a scale of 0-24, 0 being lossless
    #14 is a good option for smaller file size with only slight visual loss
    quality = 0
    # "neighbor" is highest quality but can introduce moire, use "lanczos" for no moire
    scaling_filter = "neighbor"

    # DON'T NEED TO CHANGE OUTPUT
    output = Path("./downscaled_images")
    output.mkdir(parents=True, exist_ok=True)

    processed_count = 0
    for entry_name in os.listdir(input_folder):
        if entry_name == ".DS_Store":
            continue
        entry_path = os.path.join(input_folder, entry_name)
        if os.path.isfile(entry_path):
            print(f"Found file: {entry_path}")
            downscale_image(entry_path, entry_name, output, longest_edge, quality, scaling_filter)
            processed_count += 1

    print("Successfully processed ", processed_count, " images")
def downscale_image(input_path, input_name, output_folder, longest_edge, quality, scaling_filter):
    output_path = os.path.join(output_folder, input_name)
    import ffmpeg
    (
        ffmpeg
        .input(input_path)
        .filter('scale', f"if(gt(iw,ih),{longest_edge},-1)", f"if(gt(ih,iw),{longest_edge},-1)", flags=scaling_filter)
        .output(output_path, sws_flags=scaling_filter, lossless=1, **{'q:v': 1}, crf=quality)
        #.global_args("-v", "quiet")  # add global flags
        .run()
    )

if __name__ == "__main__":
    main()