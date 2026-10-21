"""JSON 읽기·전체 검사·저장. 실패를 빈 목록 또는 성공으로 위장하지 않습니다."""
import json
from pathlib import Path
from models import from_record, to_record, name_key
from io_support import write_json_atomic
REJECT_DUPLICATES = True

def validate_records(records):
    # TODO VALIDATE: 최상위 List·각 레코드·중복 이름을 전체 검사하고 독립적인 레코드 목록을 반환하세요.
    raise NotImplementedError("TODO VALIDATE")

def load_records(path):
    # TODO LOAD: UTF-8 JSON을 읽으세요. 파일 없음만 []로 처리하고 손상은 ValueError로 전달한 뒤 전체 검사하세요.
    raise NotImplementedError("TODO LOAD")

def save_records(path, records):
    # 제공 코드 SAVE: 전체 검사를 먼저 수행하고 제공된 write_json_atomic(path, records)로 저장하세요. 실패를 숨기지 마세요.
    validated = validate_records(records)
    write_json_atomic(Path(path), validated)
    # 성공 메시지는 함수가 정상 반환된 뒤 main에서만 출력합니다.
