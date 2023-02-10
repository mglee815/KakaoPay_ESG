import sys
import json
import openpyxl
import configparser
from tqdm import tqdm

from excel import *
from crawler import get_data

keyword = ''
result_path = ''

if __name__ == "__main__":
    keyword = input("키워드를 입력하세요 : ") -> # "원하는 키워드"
    result_path = "../../data/cilen.xlsx" #  -> ./result.xlsx
    print('============================')
    print('키워드 :', keyword)
    print('결과물 :', result_path)
    print('============================')

    try:
        make_excel(result_path)
        print('엑셀 파일 생성됨.')
    except PermissionError:
        print('엑셀 파일 생성 불가. 열려 있는 엑셀 파일을 종료해주세요.')
        sys.exit(1)
    print('============================')

    start_idx = 1
    with tqdm(total=100, ncols=80, desc='작업 진행') as pbar:
        for item in get_data(keyword):
            start_idx = append_excel(result_path, item, start_idx)
            pbar.update(1)
    print('============================')
    print('작업 완료됨. 프로그램을 종료해주세요.')
    input()