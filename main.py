import youtube
import fetchresults


def main():
    video_id = "ptQUAjKx6c0"
    captions = youtube.get_video_captions(video_id)
    print(captions)
    if captions is None:
        print("Unable to fetch captions. Exiting.")
        return

    start_and_end_timing = fetchresults.extract_shorts(captions)

    for start_time, end_time in start_and_end_timing:
        print(f"Start Time: {round(start_time)}, End Time: {round(end_time)}")


if __name__ == "__main__":
    main()
