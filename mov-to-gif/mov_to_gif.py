import imageio


def convert_mov_to_gif(input_path: str, output_path: str) -> None:
    with imageio.get_writer(output_path, mode="I") as writer:
        reader = imageio.get_reader(input_path)
        for frames in reader:
            writer.append_data(frames)
    print("Conversion completed successfully")


if __name__ == "__main__":
    mov_file_path = "/Users/christoph_rohde/Desktop/progressbar.mov"
    gif_file_path = "/Users/christoph_rohde/Desktop/progressbar.gif"
    convert_mov_to_gif(mov_file_path, gif_file_path)
