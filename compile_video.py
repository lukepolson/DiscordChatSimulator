import os

def gen_vid(filename):
    input_folder = 'chat/'

    # Get all image files in the input folder
    image_files = sorted([f for f in os.listdir(input_folder) if f.endswith('.png')])

    durations = []
    with open(filename, encoding="utf8") as f:
        name_up_next = True
        
        lines = f.read().splitlines()
        for line in lines:
            if line == '':
                name_up_next = True
                continue
            elif line[0] == '#' and not line[1] == '!':
                continue
            elif name_up_next == True:
                name_up_next = False
                continue
            else:
                durations.append(line.split('$^')[1])
                
                
    # Create a text file to store the image paths
    with open('image_paths.txt', 'w') as file:    
        count = 0
        for image_file in image_files:
            file.write(f"file '{input_folder}{image_file}'\noutpoint {durations[count]}\n")
            count += 1

    video_width = 1280
    video_height = 720

    # Generate the video using the text file containing image paths and calculated frame rate
    os.system(f"ffmpeg -f concat -i image_paths.txt -vcodec libx264 -crf 25 -vf 'scale={video_width}:{video_height}:force_original_aspect_ratio=decrease,pad={video_width}:{video_height}:(ow-iw)/2:(oh-ih)/2' -pix_fmt yuv420p output.mp4")

    # Remove the temporary text file
    os.remove('image_paths.txt')