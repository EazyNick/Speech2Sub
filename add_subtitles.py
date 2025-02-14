import subprocess
import os

def add_subtitles(video_path: str, srt_path: str, output_path: str):
    """
    FFmpeg를 사용하여 SRT 자막을 비디오에 삽입하는 함수

    :param video_path: 원본 비디오 파일 경로
    :param srt_path: SRT 자막 파일 경로
    :param output_path: 출력할 번역된 비디오 경로
    """
    # Windows에서 전체 경로 사용해야 함
    video_path = os.path.abspath(video_path)
    srt_path = os.path.abspath(srt_path)
    output_path = os.path.abspath(output_path)

    if not os.path.exists(video_path):
        raise FileNotFoundError(f"❌ 비디오 파일을 찾을 수 없습니다: {video_path}")
    if not os.path.exists(srt_path):
        raise FileNotFoundError(f"❌ 자막 파일을 찾을 수 없습니다: {srt_path}")

    # 경로를 올바른 형식으로 변환 (슬래시로 변경)
    video_path = os.path.abspath(video_path).replace('\\', '/')
    srt_path = os.path.abspath(srt_path).replace('\\', '/')
    output_path = os.path.abspath(output_path).replace('\\', '/')

    # 자막 경로에서 백슬래시를 두 번 처리 (FFmpeg에서 인식되도록)
    srt_path = srt_path.replace(':', '\\\\:')

    # 수정된 FFmpeg 명령어
    command = [
       "ffmpeg", 
       "-i", video_path,
       "-vf", f"subtitles={srt_path}:original_size=1280x720",
       "-c:a", "copy", 
       output_path
   ]
    # ffmpeg -i "D:/Python/Speech2Sub/input_videos/sample.mp4" -vf "subtitles=D\\:/sample_translated.srt:original_size=1280x720" -c:a copy "D:/Python/Speech2Sub/output_videos/sample_translated.mp4"

    try:
        subprocess.run(command, check=True)
        print(f"✅ 자막 추가 완료! 저장된 파일: {output_path}")
    except subprocess.CalledProcessError as e:
        print(f"❌ FFmpeg 실행 오류: {e}")
    except FileNotFoundError:
        print("❌ FFmpeg를 찾을 수 없습니다. FFmpeg가 설치되었는지 확인해주세요.")

if __name__ == "__main__":
    video_filename = "sample.mp4"
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    INPUT_DIR = os.path.join(BASE_DIR, "input_videos")
    OUTPUT_DIR = os.path.join(BASE_DIR, "output_videos")
    SUBTITLE_DIR = os.path.join(BASE_DIR, "subtitles")

    video_path = os.path.join(INPUT_DIR, video_filename)
    base_name = os.path.splitext(video_filename)[0]

    # 자막 파일 경로를 유동적으로 설정
    srt_file = os.path.join(SUBTITLE_DIR, f"{base_name}_translated.srt")
    output_video = os.path.join(OUTPUT_DIR, f"{base_name}_translated.mp4")

    add_subtitles(video_path, srt_file, output_video)