다음은 `README.md` 파일 내용이야. 그대로 복사해서 사용하면 돼! 🚀  

---

```markdown
# 🎥 Video Translator: 자동 영상 번역 & 자막 삽입

이 프로젝트는 동영상의 음성을 텍스트로 변환(STT)하고, 자동 번역 후, 자막(SRT)을 생성하여 영상에 삽입하는 파이프라인을 제공합니다.  
OpenAI Whisper 모델과 Google Translate API를 활용하며, FFmpeg로 자막을 동영상에 합성합니다.

---

## 🛠 기능
✅ **STT(Speech-to-Text)**: OpenAI Whisper를 사용하여 음성을 텍스트로 변환  
✅ **자동 번역**: Google Translator API를 활용하여 원하는 언어로 번역  
✅ **SRT 자막 생성**: 번역된 텍스트를 SRT 형식으로 변환  
✅ **자막 삽입**: FFmpeg를 사용하여 번역된 자막을 영상에 추가  

---

## 🚀 설치 및 실행 방법

### 1️⃣ **Conda 가상환경 생성**
먼저, 가상환경을 생성하고 활성화하세요.

```bash
conda create -n video-translator-env python=3.9
conda activate video-translator-env
```

---

### 2️⃣ **필요한 라이브러리 설치**
`requirements.txt` 파일을 사용하여 필요한 패키지를 설치합니다.

```bash
pip install -r requirements.txt
```

필요한 패키지는 다음과 같습니다:
- `whisper` (음성을 텍스트로 변환)
- `torch` (Whisper 모델 실행)
- `deep-translator` (Google 번역 API)
- `srt` (SRT 파일 생성 및 관리)
- `ffmpeg-python` (FFmpeg를 파이썬에서 제어)

---

### 3️⃣ **FFmpeg 설치**
FFmpeg가 필요하므로 아래 방법으로 설치하세요.

#### ✅ **Windows**
1. [FFmpeg 공식 사이트](https://ffmpeg.org/download.html)에서 다운로드  
2. 압축을 풀고 `ffmpeg.exe`를 환경 변수(`PATH`)에 추가

#### ✅ **Mac (Homebrew)**
```bash
brew install ffmpeg
```

#### ✅ **Ubuntu/Linux**
```bash
sudo apt update
sudo apt install ffmpeg
```

설치 후 FFmpeg가 정상적으로 동작하는지 확인:
```bash
ffmpeg -version
```

--- 

### 4️⃣ **번역 실행**
아래 명령어를 실행하여 동영상을 번역하고 자막을 추가합니다.

```bash
python translate_video.py --video input_videos/sample.mp4 --target_lang ko
```

✅ 실행이 완료되면 `output_videos/` 폴더에 번역된 자막이 포함된 영상이 저장됩니다.  

#### 🛠 매개변수 설명
- `--video` → 번역할 동영상 파일 경로  
- `--target_lang` → 번역할 대상 언어 (예: `en` → 영어, `ko` → 한국어, `ja` → 일본어)  

#### 📌 실행 예제
```bash
python translate_video.py --video input_videos/movie.mp4 --target_lang en
```
위 명령어를 실행하면 `movie.mp4`의 음성을 영어로 번역한 후, 자막을 추가한 영상이 `output_videos/movie_translated.mp4`로 저장됩니다.

---

## 🎯 실행 흐름
1. **음성 → 텍스트 변환 (STT)** (`speech_to_text.py`)
2. **텍스트 번역** (`translate_text.py`)
3. **SRT 자막 파일 생성** (`generate_srt.py`)
4. **자막을 비디오에 추가** (`add_subtitles.py`)

---

## 📌 예제 실행 결과
- 원본 파일: `input_videos/sample.mp4`
- 변환된 텍스트 파일: `subtitles/sample_original.txt`
- 번역된 자막 파일: `subtitles/sample_translated.srt`
- 최종 번역된 동영상: `output_videos/sample_translated.mp4`

---

## 🔗 참고 링크
- [FFmpeg 공식 홈페이지](https://ffmpeg.org/)
- [Whisper 모델 설명](https://github.com/openai/whisper)
- [Deep Translator 공식 문서](https://pypi.org/project/deep-translator/)

---

## 📢 문의
궁금한 점이나 개선 제안이 있으면 언제든지 연락 주세요! 🚀  
email - kkkygsos@naver.com
