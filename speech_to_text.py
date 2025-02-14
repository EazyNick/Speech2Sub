import whisper
import os

def transcribe_audio(video_path: str, output_txt: str):
    """
    동영상에서 오디오를 추출하고 텍스트로 변환하는 함수
    :param video_path: 변환할 동영상 파일 경로
    :param output_txt: 변환된 텍스트 저장 파일
    """
    model = whisper.load_model("medium")  # 모델 크기 선택 가능 (tiny, base, small, medium, large)
    
    # 동영상에서 오디오 변환 (Whisper는 직접 mp4를 처리 가능)
    result = model.transcribe(video_path)
    
    # 변환된 텍스트 저장
    with open(output_txt, "w", encoding="utf-8") as f:
        for segment in result['segments']:
            start = segment['start']
            end = segment['end']
            text = segment['text']
            f.write(f"{start:.2f} --> {end:.2f}\n{text}\n\n")

    return output_txt

# ✅ 직접 실행 테스트
if __name__ == "__main__":
    input_video = "input_videos/sample.mp4"  # 변환할 동영상 파일 경로
    output_text = "subtitles/sample_original.txt"  # 변환된 텍스트 저장 파일

    # 디렉터리 생성 (없을 경우)
    os.makedirs(os.path.dirname(output_text), exist_ok=True)

    # ✅ 테스트 실행
    transcribe_audio(input_video, output_text)