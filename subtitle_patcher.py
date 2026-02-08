import os
import shutil

# 경로 설정
ORIGINAL_DIR = "원본_en"
TRANSLATED_DIR = "번역_ko"
OUTPUT_DIR = "결과_en"

if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

def patch_subtitles():
    print("--- 자막 데이터 이식 시작 ---")
    
    # 원본 파일 목록 가져오기
    orig_files = [f for f in os.listdir(ORIGINAL_DIR) if f.endswith('.srt')]
    patched_count = 0
    skipped_count = 0

    for file_name in orig_files:
        orig_path = os.path.join(ORIGINAL_DIR, file_name)
        trans_path = os.path.join(TRANSLATED_DIR, file_name)
        out_path = os.path.join(OUTPUT_DIR, file_name)

        # 번역본 폴더에 똑같은 이름의 파일이 있는지 확인
        if os.path.exists(trans_path):
            # 번역본이 있으면 번역본을 결과 폴더로 복사 (이름은 원본 이름 유지)
            shutil.copy2(trans_path, out_path)
            print(f"✅ 이식 완료: {file_name}")
            patched_count += 1
        else:
            # 번역본이 없으면 원본 그대로 복사 (게임 튕김 방지)
            shutil.copy2(orig_path, out_path)
            print(f"⚠️ 번역본 없음 (원본 유지): {file_name}")
            skipped_count += 1

    print("-" * 30)
    print(f"결과 요약: 총 {len(orig_files)}개 중 {patched_count}개 한글화 완료!")
    if skipped_count > 0:
        print(f"미번역 파일 {skipped_count}개는 영어 원본으로 유지되었습니다.")
    print(f"파일들이 '{OUTPUT_DIR}' 폴더에 생성되었습니다.")

if __name__ == "__main__":
    patch_subtitles()