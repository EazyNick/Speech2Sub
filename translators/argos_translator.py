import argostranslate.package
import argostranslate.translate
import os

import argostranslate.package
import argostranslate.translate

def setup_argos():
    """
    Japanese -> English, English -> Korean 모델을 다운로드 및 설치
    """
    argostranslate.package.update_package_index()
    available_packages = argostranslate.package.get_available_packages()
    installed_packages = argostranslate.package.get_installed_packages()

    # ✅ 필요한 모델 리스트
    required_models = [
        ("ja", "en"),  # 일본어 → 영어
        ("en", "ko")   # 영어 → 한국어
    ]

    # ✅ 모델 다운로드 및 설치
    for from_lang, to_lang in required_models:
        if any(pkg.from_code == from_lang and pkg.to_code == to_lang for pkg in installed_packages):
            print(f"✅ {from_lang} -> {to_lang} 번역 모델이 이미 설치되어 있습니다.")
        else:
            for package in available_packages:
                if package.from_code == from_lang and package.to_code == to_lang:
                    print(f"📥 번역 모델 다운로드 중: {package}")
                    package.install()

    print("✅ Japanese -> English, English -> Korean 번역 모델 설치 완료!")

def translate_argos(text: str) -> str:
    """
    Japanese -> English -> Korean 번역 (Argos Translate)

    :param text: 번역할 일본어 원본 텍스트
    :return: 한국어로 번역된 텍스트
    """
    try:
        # ✅ 자동으로 번역 모델 설치
        setup_argos()

        # ✅ Step 1: 일본어 → 영어 번역
        english_text = argostranslate.translate.translate(text, "ja", "en")
        if not english_text:
            raise ValueError("⚠️ 일본어 → 영어 번역 실패")

        # ✅ Step 2: 영어 → 한국어 번역
        korean_text = argostranslate.translate.translate(english_text, "en", "ko")
        if not korean_text:
            raise ValueError("⚠️ 영어 → 한국어 번역 실패")

        return korean_text

    except Exception as e:
        print(f"⚠️ Argos 다단계 번역 실패: {e}")
        return text  # 번역 실패 시 원본 유지


# ✅ 테스트 실행
if __name__ == "__main__":
    print(translate_argos("こんにちは、元気ですか？"))  # 예상 출력: "안녕하세요, 잘 지내시나요?"

