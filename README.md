# Dead Reset Localization Patch for macOS

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Unity](https://img.shields.io/badge/unity-%23000000.svg?style=for-the-badge&logo=unity&logoColor=white)
![macOS](https://img.shields.io/badge/mac%20os-000000?style=for-the-badge&logo=apple&logoColor=white)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)

이 프로젝트는 FMV 게임 **'Dead Reset'**의 최신 버전(v1.0.5 이상) 및 Apple Silicon(M1/M2/M3/M4) 맥북 환경에서 발생하는 한글 패치 크래시 문제를 해결하고, 안전하게 한글 자막을 이식하기 위한 툴세트와 패치 파일을 제공합니다.

---

## ✨ 특징 (Features)

* **macOS 최적화**: 윈도우용 에셋 덮어쓰기로 인한 강제 종료(Crash) 문제를 해결했습니다.
* **폰트 직접 이식**: `UnityPy`를 사용하여 원본 에셋 내부에 한글 유니코드 폰트를 직접 주입하여 `ㅁㅁㅁ` 깨짐 현상을 방지합니다.
* **자동 자막 치환**: 300여 개의 자막 파일(`srt`)을 원본 파일명을 유지하며 자동으로 매칭 및 교체합니다.
* **Apple Silicon 지원**: 최신 M4 Max 맥북을 포함한 모든 macOS 환경에서 안정적으로 작동합니다.

---

## 🛠️ 포함된 스크립트 (Toolsets)

본 레포지토리에는 패치 제작에 사용된 파이썬 스크립트가 포함되어 있습니다.

* `font_patcher.py`: `resources.assets` 내의 폰트 데이터를 한글 지원 폰트(`.ttf`)로 교체합니다.
* `subtitle_patcher.py`: 영어 원본 자막 폴더와 번역된 자막 폴더를 비교하여 자동으로 이식된 `en.zip`을 생성합니다.
* `final_scanner.py`: 유니티 에셋 내의 `TextAsset` 위치를 추적하는 도구입니다.

---

## 🚀 패치 적용 방법 (Installation)

가장 쉽고 빠른 방법은 [Releases](https://github.com/사용자계정/레포이름/releases) 페이지에서 완성된 패치 파일을 다운로드하는 것입니다.

1. **패치 다운로드**: `Releases`에서 `DeadReset_KR_Patch.zip`을 다운로드합니다.
2. **폰트 데이터 적용**: 
   - `DeadReset.app/Contents/Resources/Data/` 경로에 `resources.assets` 파일을 덮어씌웁니다.
3. **자막 파일 적용**:
   - `DeadReset.app/Contents/Resources/Data/StreamingAssets/Subtitles/` 경로에 한글화된 `en.zip` 파일을 교체합니다.
4. **게임 설정**:
   - 게임 실행 후 **Options > Language**를 **"English"**로 설정하세요. (영어 설정에서 한글 자막이 출력됩니다.)

---

## ⚠️ 주의사항 (Notes)

* **인터페이스**: 안정성을 위해 메뉴 인터페이스는 영문으로 유지되며 자막만 한글로 나옵니다.
* **언어 설정**: "English" 설정 외의 다른 언어(중국어 등) 선택 시 폰트 문제로 글자가 깨질 수 있습니다.
* **백업 권장**: 패치 적용 전 반드시 원본 `resources.assets` 파일을 백업해 두시기 바랍니다.

---

## ⚖️ 저작권 및 면책 조항 (License & Disclaimer)

* 본 패치는 개인적인 학습 및 연구 목적으로 제작되었습니다.
* 게임의 저작권은 원작사인 **Wales Interactive**에 있으며, 패치 사용으로 인해 발생하는 모든 책임은 사용자에게 있습니다.

---

**제작**: [yunsuper]