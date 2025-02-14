import os
from speech_to_text import transcribe_audio
from translate_text import translate_text
from generate_srt import convert_to_srt
from add_subtitles import add_subtitles

# 가상환경 활성화 명령어 conda activate video-translator-env

def process_video(video_path: str, target_lang="en"):
    base_name = os.path.splitext(os.path.basename(video_path))[0]
    txt_file = f"subtitles/{base_name}_original.txt"
    translated_txt = f"subtitles/{base_name}_translated.txt"
    srt_file = f"subtitles/{base_name}.srt"
    output_video = f"output_videos/{base_name}_translated.mp4"

    transcribe_audio(video_path, txt_file)
    translate_text(txt_file, translated_txt, target_lang=target_lang)
    convert_to_srt(translated_txt, srt_file)
    add_subtitles(video_path, srt_file, output_video)

    print(f"✅ 번역 완료! 파일 저장: {output_video}")

# 실행 예시
if __name__ == "__main__":
    process_video("input_videos/sample.mp4", target_lang="ko")
