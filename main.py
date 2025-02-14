import os
from speech_to_text import transcribe_audio
from translate_text import translate_text
from generate_srt import convert_to_srt
from add_subtitles import add_subtitles

# 현재 스크립트가 있는 디렉토리 기준으로 경로 설정
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # 현재 main.py가 있는 폴더 경로
INPUT_DIR = os.path.join(BASE_DIR, "input_videos")
OUTPUT_DIR = os.path.join(BASE_DIR, "output_videos")
SUBTITLE_DIR = os.path.join(BASE_DIR, "subtitles")

# 가상환경 활성화 명령어 (Windows 기준)
# conda activate video-translator-env

def process_video(video_filename: str, target_lang="en"):
    """
    비디오 파일을 처리하여 자막을 번역하고 삽입하는 함수

    :param video_filename: 입력 비디오 파일 이름 (예: "sample.mp4")
    :param target_lang: 번역할 대상 언어 (예: "ko" -> 한국어)
    """
    video_path = os.path.join(INPUT_DIR, video_filename)
    
    if not os.path.exists(video_path):
        raise FileNotFoundError(f"❌ 파일을 찾을 수 없습니다: {video_path}")

    base_name = os.path.splitext(video_filename)[0]  # 확장자 제거한 파일명
    txt_file = os.path.join(SUBTITLE_DIR, f"{base_name}_original.txt")
    translated_txt = os.path.join(SUBTITLE_DIR, f"{base_name}_translated.txt")
    srt_file = os.path.join(SUBTITLE_DIR, f"{base_name}.srt")
    output_video = os.path.join(OUTPUT_DIR, f"{base_name}_translated.mp4")

    print(f"🎬 처리 중: {video_path}")
    
    transcribe_audio(video_path, txt_file)
    translate_text(txt_file, translated_txt, target_lang=target_lang)
    convert_to_srt(translated_txt, srt_file)
    add_subtitles(video_path, srt_file, output_video)

    print(f"✅ 번역 완료! 파일 저장: {output_video}")

# 실행 예시
if __name__ == "__main__":
    process_video("sample.mp4", target_lang="ko")
