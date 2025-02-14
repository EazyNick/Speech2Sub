# from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# # 모델 로드 (최초 실행 시 다운로드됨)
# model_name = "facebook/nllb-200-distilled-600M"
# tokenizer = AutoTokenizer.from_pretrained(model_name)
# model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

# def translate_nllb(text: str, src_lang: str = "jpn", target_lang: str = "kor") -> str:
#     """
#     NLLB-200 (Meta AI) 모델을 사용하여 텍스트 번역

#     :param text: 번역할 원본 텍스트
#     :param src_lang: 원본 언어 코드 (예: 'jpn' -> 일본어)
#     :param target_lang: 번역할 언어 코드 (예: 'kor' -> 한국어)
#     :return: 번역된 텍스트
#     """
#     try:
#         inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, src_lang=src_lang, tgt_lang=target_lang)
#         translated = model.generate(**inputs)
#         return tokenizer.decode(translated[0], skip_special_tokens=True)
#     except Exception as e:
#         print(f"⚠️ NLLB-200 번역 실패: {e}")
#         return text
