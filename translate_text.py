import os
# from translators.google_translator import translate_google
from translators.argos_translator import translate_argos
# from translators.marian_translator import translate_marian
# from translators.nllb_translator import translate_nllb

# 사용 가능한 번역기 목록
TRANSLATORS = {
    # "google": translate_google,
    "argos": translate_argos,
    # "marian": translate_marian,
    # "nllb": translate_nllb
}

def translate_text(input_txt: str, output_txt: str, translator_name="argos", src_lang="ja", target_lang="ko"):
    """
    번역할 텍스트 파일을 읽고, 선택한 번역기로 번역하여 저장하는 함수
    :param input_txt: 변환된 자막 파일 (.txt)
    :param output_txt: 번역된 자막 파일 (.txt)
    :param translator_name: 사용할 번역기 (google, argos, marian, nllb)
    :param src_lang: 원본 언어 (예: 'ja' -> 일본어)
    :param target_lang: 번역할 언어 (예: 'ko' -> 한국어)
    """
    if translator_name not in TRANSLATORS:
        raise ValueError(f"⚠️ 지원되지 않는 번역기: {translator_name}. 사용 가능: {list(TRANSLATORS.keys())}")

    translator = TRANSLATORS[translator_name]

    with open(input_txt, "r", encoding="utf-8") as f:
        lines = f.readlines()

    translated_lines = []
    for line in lines:
        if "-->" in line or line.strip() == "":  # 시간 정보는 그대로 유지
            translated_lines.append(line)
        else:
            translated_text = translator(line.strip())  # ✅ 자동으로 일본어 → 영어 → 한국어 변환
            translated_lines.append(translated_text + "\n")

    with open(output_txt, "w", encoding="utf-8") as f:
        f.writelines(translated_lines)

    print(f"✅ 번역 완료! 저장된 파일: {output_txt}")
    return output_txt

# 실행 예제
if __name__ == "__main__":
    import argostranslate.package

    installed_packages = argostranslate.package.get_installed_packages()
    print("설치된 번역 모델 목록:")
    for pkg in installed_packages:
        print(f"   - {pkg.from_code} -> {pkg.to_code}")

    translate_text("subtitles/sample_original.txt", "subtitles/sample_translated.txt", translator_name="argos")