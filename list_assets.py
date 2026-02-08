import UnityPy

# 원본 .assets 파일 경로
path = "globalgamemanagers.assets"
env = UnityPy.load(path)

print(f"--- {path} 내부 리소스 목록 ---")
count = 0

for obj in env.objects:
    # 텍스트 파일(TextAsset)만 분석
    if obj.type.name == "TextAsset":
        try:
            # 버전에 따라 접근 방식이 다를 수 있어 read() 후 속성 확인
            data = obj.read()
            # m_Name 혹은 name 속성 확인
            name = getattr(data, "name", getattr(data, "m_Name", "Unknown"))
            script_len = len(getattr(data, "script", b""))
            
            print(f"파일명: {name} | 크기: {script_len} bytes")
            count += 1
        except Exception as e:
            continue

if count == 0:
    print("TextAsset을 찾지 못했습니다. 파일 경로를 다시 확인해주세요.")
else:
    print(f"\n총 {count}개의 텍스트 자산을 찾았습니다.")