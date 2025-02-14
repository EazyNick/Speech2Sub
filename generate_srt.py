import srt
from datetime import timedelta

def convert_to_srt(input_txt: str, output_srt: str):
    """
    변환된 자막 텍스트를 SRT 파일로 변환
    :param input_txt: 번역된 자막 파일 (.txt)
    :param output_srt: SRT 포맷으로 저장할 파일 경로
    """
    with open(input_txt, "r", encoding="utf-8") as f:
        lines = f.readlines()

    subtitles = []
    index = 1
    for i in range(0, len(lines), 3):  # 3줄 단위로 시간+텍스트
        if i + 2 >= len(lines):
            break
        time_range = lines[i].strip().split(" --> ")
        start_time = timedelta(seconds=float(time_range[0]))
        end_time = timedelta(seconds=float(time_range[1]))
        text = lines[i + 1].strip()
        
        subtitles.append(srt.Subtitle(index, start_time, end_time, text))
        index += 1

    with open(output_srt, "w", encoding="utf-8") as f:
        f.write(srt.compose(subtitles))

    return output_srt

# if __name__ == "__main__" 테스트 코드 추가
if __name__ == "__main__":
    input_txt = "subtitles/sample_original.txt"  # 변환할 자막 파일 경로
    output_srt = "subtitles/sample_original_translated.srt"  # SRT 포맷으로 저장될 경로

    # 변환 실행
    convert_to_srt(input_txt, output_srt)
    print(f"✅ 변환 완료! 저장된 SRT 파일: {output_srt}")
