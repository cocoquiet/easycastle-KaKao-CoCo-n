from data_transform.transform import Transform_to_txt_csv
import pandas as pd

tt = Transform_to_txt_csv() # tt라는 인스턴스에 Transform_to_txt_csv를 할당
tt.load('korean/2runo\'s-Curse-detection-data.txt') # 데이터 로딩하기
data = tt.read() # 데이터 읽기

# 2runo\'s-Curse-detection-data.txt 에 있는 글자를 읽은후 data의 저장까지 완료 :)