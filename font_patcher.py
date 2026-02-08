import UnityPy
import os

# 설정
ASSETS_FILE = "resources.assets"    # 원본 파일
NEW_FONT_PATH = "myfont.ttf"        # 폴더에 넣은 한글 폰트 파일명
OUTPUT_FILE = "resources.assets.new"

def patch_font():
    if not os.path.exists(NEW_FONT_PATH):
        print(f"❌ 에러: '{NEW_FONT_PATH}' 파일이 폴더에 없습니다.")
        return

    # 새 폰트 바이너리 데이터 읽기
    with open(NEW_FONT_PATH, "rb") as f:
        new_font_data = f.read()

    env = UnityPy.load(ASSETS_FILE)
    found_count = 0

    print("--- 폰트 수색 및 교체 시작 ---")
    for obj in env.objects:
        # Font 타입 자산만 타겟팅
        if obj.type.name == "Font":
            try:
                data = obj.read()
                # 필드 이름이 name인지 m_Name인지 확인하며 가져오기
                font_name = getattr(data, "name", getattr(data, "m_Name", "Unknown Font"))
                print(f"🔎 발견: {font_name} (교체 중...)")
                
                # 핵심: 폰트 데이터 교체
                if hasattr(data, "m_FontData"):
                    data.m_FontData = new_font_data
                    data.save() # 변경 사항 저장
                    found_count += 1
                else:
                    print(f"⚠️ {font_name}은 데이터 구조가 달라 스킵합니다.")
            except Exception as e:
                print(f"⚠️ 처리 중 오류 발생: {e}")
                continue

    if found_count > 0:
        # 최종 파일 저장
        with open(OUTPUT_FILE, "wb") as f:
            f.write(env.file.save())
        print(f"\n✅ 성공! 총 {found_count}개의 폰트를 교체했습니다.")
        print(f"🚀 생성된 '{OUTPUT_FILE}'의 이름을 'resources.assets'로 바꿔서 게임 폴더에 넣으세요.")
    else:
        print("\n❌ 교체할 수 있는 Font 에셋을 찾지 못했습니다.")

if __name__ == "__main__":
    patch_font()