def simple_hash(s, table_size):
    """
    아주 단순한 문자열 해시 함수 예시
    s: 입력 문자열
    table_size: 해시 값을 매핑할 테이블의 크기 (버킷 수)
    """
    hash_value = 0
    i = 1
    for char in s:
        print(f"{hash_value} * 31 + {ord(char)}") 
        hash_value = (hash_value * 31 + ord(char))
        # 31은 일반적으로 해시 함수에서 사용되는 소수 중 하나입니다.
        # ord(char)는 문자의 ASCII 값을 반환합니다.
        # % table_size는 해시 값을 지정된 범위 내로 제한합니다.
        print(f"{i}번째 현재 해시 값 = {hash_value}")
        i = i + 1

    return f"{hash_value:04d}"

# 예시 사용
table_size = 10000 # 0부터 9까지의 인덱스를 가진다고 가정

print(f"해시값 for 'a': {simple_hash('dddd', table_size)}")