from deep_translator import GoogleTranslator

def translate_text(input_txt: str, output_txt: str, src_lang="auto", target_lang="en"):
    """
    텍스트 파일을 번역하는 함수
    :param input_txt: 변환된 자막 파일 (.txt)
    :param output_txt: 번역된 자막 파일 (.txt)
    :param src_lang: 원본 언어 (auto: 자동 감지)
    :param target_lang: 번역할 언어 (예: 'en' -> 영어)
    """
    translator = GoogleTranslator(source=src_lang, target=target_lang)
    
    with open(input_txt, "r", encoding="utf-8") as f:
        lines = f.readlines()

    translated_lines = []
    for line in lines:
        if "-->" in line or line.strip() == "":
            translated_lines.append(line)  # 시간 정보는 그대로 유지
        else:
            translated_lines.append(translator.translate(line.strip()) + "\n")

    with open(output_txt, "w", encoding="utf-8") as f:
        f.writelines(translated_lines)

    return output_txt
