# from deep_translator import GoogleTranslator

# def translate_google(text: str, src_lang: str = "auto", target_lang: str = "en") -> str:
#     """
#     Google Translate API를 사용하여 텍스트 번역

#     :param text: 번역할 원본 텍스트
#     :param src_lang: 원본 언어 (예: 'ja' -> 일본어, 'auto' -> 자동 감지)
#     :param target_lang: 번역할 언어 (예: 'ko' -> 한국어)
#     :return: 번역된 텍스트
#     """
#     try:
#         return GoogleTranslator(source=src_lang, target=target_lang).translate(text)
#     except Exception as e:
#         print(f"⚠️ Google 번역 실패: {e}")
#         return text  # 번역 실패 시 원문 반환
