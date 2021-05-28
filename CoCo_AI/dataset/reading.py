from data_preprocessing.files_transform import Transform_to_txt_csv
import pandas as pd
tt = Transform_to_txt_csv() # tt라는 인스턴스에 Transform_to_txt_csv를 할당
tt.load('korean/2runo\'s-Curse-detection-data.txt') # 데이터 로딩하기
data = tt.read() # 데이터 읽기
ls = list(data.split('\n'))
out = []
for i in ls:
    out.append(i.split('|'))

sentence_ls = []
targetls = []

for i in out:
    sentence_ls.append(i[0])
    targetls.append(i[1])

df = pd.DataFrame(columns=['sentence', 'target'],
                  data = {
                      'sentence' : sentence_ls,
                      'target' : targetls
                  })
df.to_csv('korean/2runo\'s-swear.csv')