# from transformers import MarianMTModel, MarianTokenizer

# def translate_marian(text: str, src_lang: str = "ja", target_lang: str = "ko") -> str:
#     """
#     MarianMT (Helsinki-NLP) 모델을 사용하여 텍스트 번역

#     :param text: 번역할 원본 텍스트
#     :param src_lang: 원본 언어 코드 (예: 'ja' -> 일본어)
#     :param target_lang: 번역할 언어 코드 (예: 'ko' -> 한국어)
#     :return: 번역된 텍스트
#     """
#     try:
#         model_name = f"Helsinki-NLP/opus-mt-{src_lang}-{target_lang}"
#         tokenizer = MarianTokenizer.from_pretrained(model_name)
#         model = MarianMTModel.from_pretrained(model_name)

#         inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
#         translated = model.generate(**inputs)
#         return tokenizer.decode(translated[0], skip_special_tokens=True)
#     except Exception as e:
#         print(f"⚠️ MarianMT 번
