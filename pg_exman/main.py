import argparse
from db_manager import DBManager
from extension_manager import ExtensionManager

def parse_arguments():
    # argparse를 사용하여 명령줄 인자 처리
    pass

def main():
    args = parse_arguments()
    db_manager = DBManager(args.connection_string)
    extension_manager = ExtensionManager(db_manager)
    
    # 사용자가 선택한 작업(확장 조회, 설치, 업데이트, 제거) 실행

if __name__ == "__main__":
    main()
