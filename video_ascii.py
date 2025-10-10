# Terminal Video Player - Full Color & High Quality
# Usage: python video_player.py video.mp4 [--audio] [--subs] [--quality high/medium/low]

import cv2
import sys
import time
import subprocess
import srt
import datetime
import shutil
import os

def rgb_to_ansi(r, g, b):
    """Convert RGB to ANSI true color."""
    return f"\033[38;2;{r};{g};{b}m"

def reset_color():
    """Reset color."""
    return "\033[0m"

def frame_to_color_blocks(frame, width, height, use_half_blocks=True):
    """Convert frame to colored blocks using true color."""
    resized = cv2.resize(frame, (width, height), interpolation=cv2.INTER_AREA)

    output = ""
    if use_half_blocks:

        for y in range(0, height - 1, 2):
            for x in range(width):

                b1, g1, r1 = resized[y, x]

                b2, g2, r2 = resized[y + 1, x]

                fg = rgb_to_ansi(r1, g1, b1)
                bg = f"\033[48;2;{r2};{g2};{b2}m"
                output += f"{bg}{fg}{reset_color()}"
            output += "\n"
    else:

        for row in resized:
            for pixel in row:
                b, g, r = pixel
                color = rgb_to_ansi(r, g, b)
                output += f"{color}{reset_color()}"
            output += "\n"

    return output

def load_subtitles(video_path):
    """Load .srt subtitle file."""
    base, _ = os.path.splitext(video_path)
    srt_file = base + ".srt"
    if os.path.exists(srt_file):
        try:
            with open(srt_file, "r", encoding="utf-8") as f:
                return list(srt.parse(f.read()))
        except:
            pass
    return []

def get_current_sub(subs, current_time):
    """Get current timestamp."""
    for sub in subs:
        if sub.start <= current_time <= sub.end:
            return sub.content
    return ""

def clear_screen():
    """Clear."""
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()

def hide_cursor():
    """Hide cursor."""
    sys.stdout.write("\033[?25l")
    sys.stdout.flush()

def show_cursor():
    """Show cursor."""
    sys.stdout.write("\033[?25h")
    sys.stdout.flush()

def get_video_info(video_path):
    """Get video."""
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        return None

    info = {
        'fps': cap.get(cv2.CAP_PROP_FPS) or 24,
        'width': int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
        'height': int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)),
        'frames': int(cap.get(cv2.CAP_PROP_FRAME_COUNT)),
        'duration': int(cap.get(cv2.CAP_PROP_FRAME_COUNT) / (cap.get(cv2.CAP_PROP_FPS) or 24))
    }
    cap.release()
    return info

def format_time(seconds):
    """Format."""
    mins = int(seconds // 60)
    secs = int(seconds % 60)
    return f"{mins:02d}:{secs:02d}"

def play_video(video_path, play_audio=False, show_subs=False, quality="high"):
    

    term = os.environ.get('TERM', '')
    if 'truecolor' not in term and '256color' not in term:
        print("  Warning: Your terminal may not support true colors.")
        print("   For best results, use a modern terminal (iTerm2, Windows Terminal, Konsole, etc.)")
        time.sleep(2)

    info = get_video_info(video_path)
    if not info:
        print(f" Error: Cannot open video file '{video_path}'")
        return

    print(f" Video: {os.path.basename(video_path)}")
    print(f" Resolution: {info['width']}x{info['height']}")
    print(f"  Duration: {format_time(info['duration'])}")
    print(f"  FPS: {info['fps']:.2f}")
    print(f" Quality: {quality.upper()}")
    print(f"\n  Press Ctrl+C to stop\n")
    time.sleep(2)

    subs = load_subtitles(video_path) if show_subs else []

    audio_proc = None
    if play_audio:
        try:
            audio_proc = subprocess.Popen(
                ["ffplay", "-nodisp", "-autoexit", "-loglevel", "quiet", video_path],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
        except FileNotFoundError:
            print("  ffplay not found. Install FFmpeg for audio support.")
            time.sleep(1)

    term_cols, term_rows = shutil.get_terminal_size(fallback=(120, 40))

    if quality == "high":

        display_width = term_cols
        display_height = (term_rows - 4) * 2  

    elif quality == "medium":
        display_width = term_cols
        display_height = term_rows - 4
    else:  # low
        display_width = term_cols // 2
        display_height = (term_rows - 4) // 2

    video_aspect = info['width'] / info['height']
    terminal_aspect = display_width / (display_height * 2)  

    if terminal_aspect > video_aspect:

        display_width = int(display_height * 2 * video_aspect)
    else:

        display_height = int(display_width / (2 * video_aspect))

    cap = cv2.VideoCapture(video_path)
    fps = info['fps']
    frame_delay = 1 / fps

    hide_cursor()
    clear_screen()

    frame_count = 0
    start_time = time.time()

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            frame_count += 1
            current_ms = cap.get(cv2.CAP_PROP_POS_MSEC)
            current_time = datetime.timedelta(milliseconds=current_ms)

            use_half_blocks = (quality == "high")
            colored_frame = frame_to_color_blocks(frame, display_width, display_height, use_half_blocks)

            progress = frame_count / info['frames']
            bar_width = display_width
            filled = int(bar_width * progress)
            bar = f"[{'=' * filled}{' ' * (bar_width - filled)}]"

            time_info = f"{format_time(current_ms / 1000)} / {format_time(info['duration'])}"

            sub_text = ""
            if subs:
                sub_text = get_current_sub(subs, current_time)

            output = "\033[H"  

            output += colored_frame
            output += "\n"
            output += f"{bar} {progress * 100:.1f}%\n"
            output += f"  {time_info}  |   Frame {frame_count}/{info['frames']}\n"

            if sub_text:

                sub_lines = sub_text.split('\n')
                for line in sub_lines:
                    padding = max(0, (display_width - len(line)) // 2)
                    output += " " * padding + line + "\n"

            sys.stdout.write(output)
            sys.stdout.flush()

            elapsed = time.time() - start_time
            expected_time = frame_count * frame_delay
            sleep_time = expected_time - elapsed

            if sleep_time > 0:
                time.sleep(sleep_time)

    except KeyboardInterrupt:
        pass
    finally:
        cap.release()
        show_cursor()
        if audio_proc:
            audio_proc.terminate()
            audio_proc.wait()
        print("\n\n Playback stopped.")

def main():
    if len(sys.argv) < 2:
        print(" Terminal Video Player - Full Color Edition")
        print("\nUsage: python video_player.py <video_file> [options]")
        print("\nOptions:")
        print("  --audio              Play audio (requires ffplay)")
        print("  --subs               Show subtitles (.srt file)")
        print("  --quality high       High quality (default, uses half-blocks)")
        print("  --quality medium     Medium quality")
        print("  --quality low        Low quality (faster)")
        print("\nExamples:")
        print("  python video_player.py movie.mp4 --audio --subs")
        print("  python video_player.py video.mp4 --quality high --audio")
        print("\n Tip: Use a terminal that supports true colors for best results!")
        print("   (Windows Terminal, iTerm2, Konsole, Alacritty, etc.)")
        sys.exit(1)

    video_file = sys.argv[1]

    if not os.path.exists(video_file):
        print(f" Error: File '{video_file}' not found.")
        sys.exit(1)

    audio_flag = any(arg.lower() in ["--audio", "audio=on"] for arg in sys.argv)
    subs_flag = any(arg.lower() in ["--subs", "subs=on"] for arg in sys.argv)

    quality = "high"
    for i, arg in enumerate(sys.argv):
        if arg.lower() == "--quality" and i + 1 < len(sys.argv):
            q = sys.argv[i + 1].lower()
            if q in ["high", "medium", "low"]:
                quality = q

    play_video(video_file, play_audio=audio_flag, show_subs=subs_flag, quality=quality)

if __name__ == "__main__":
    main()