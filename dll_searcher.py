import os
import re

# 찾고 싶은 단어 패턴 (대사라고 생각될 만한 긴 문장 위주)
# 최소 4글자 이상의 영문/숫자/문장부호 뭉치를 찾습니다.
string_pattern = re.compile(rb'[A-Za-z0-9\s\.,!\?\'"]{10,}')

dll_files = [f for f in os.listdir('.') if f.endswith('.dll')]

for dll in dll_files:
    print(f"--- [{dll}] 분석 중 ---")
    try:
        with open(dll, 'rb') as f:
            content = f.read()
            # 텍스트 데이터 추출
            strings = string_pattern.findall(content)
            
            # 상위 10개만 출력해서 대사인지 확인
            found_count = 0
            for s in strings:
                text = s.decode('ascii', errors='ignore').strip()
                # 게임 설정값이 아닌 실제 문장 같은 것만 필터링
                if len(text) > 20 and ' ' in text:
                    print(f"✅ 발견: {text}")
                    found_count += 1
                if found_count >= 10: break
            
            if found_count == 0:
                print("   (이 파일엔 대사로 보이는 문장이 없습니다.)")
    except Exception as e:
        print(f"   에러 발생: {e}")