import streamlit as st

# #  button
# st.header('버튼 실습 1')
# def button_write():
#     st.write('버튼 실행!')
#
# st.button('Reset', type="primary")
# st.button('activate', on_click=button_write)

# code
st.header('코드 실습')
code = '''
#  button
st.header('버튼 실습 1')
def button_write():
    st.write('버튼 실행!')

st.button('Reset', type="primary")
st.button('activate', on_click=button_write)
'''

st.code(code, language='python')

# 출력 시 if문을 실행 -> 버튼
st.header('버튼 실습 2')
st.button('Reset', type="primary")
if st.button('activate'):
    st.write('버튼 실행!!!')

# checkbox(체크 박스)
st.header('checkbox (체크 박스) 실습')
active = st.checkbox('I agree!')

if active:
    st.write('Great!!')


# toggle (토글)
st.header('toggle (토글) 실습')
toggle = st.toggle('Turn on the switch', value=True)
if toggle:
    st.write('switch is turned on!')
else:
    st.write('Switch is turned off!')

# selectbox (선택 박스)
st.header('selectbox (선택 박스) 실습 1')
option = st.selectbox(
    label='당신의 선택은??',
    options=['Car', 'Airplane', 'Train', 'ship']
)
st.write(f'당신의 선택 : {option}')


# selectbox (선택 박스)
st.header('selectbox (선택 박스) 실습 2')
option2 = st.selectbox(
    label='당신의 선택은??',
    options=['Car', 'Airplane', 'Train', 'ship'],
    index=None,
    placeholder='교통수단을 선택하시오.'
)
st.write(f'당신의 선택 : {option2}')


# radio (라디오)
st.header('radio (라디오) 실습')
option3 = st.radio(
    'What is your favorite movie genre',
    ['Comedy', 'Drama', 'Documentary'],
    captions=['Lauph out Loud', 'Get the popcorn', 'Naver stop learning']
)
if option3:
    st.text(f'당신의 선택: {option3}')


# multiselect (다중 선택)
st.header('multiselect (다중 선택) 실습 ')
option4 = st.multiselect(
    label='당신의 선택은??',
    options = ['Car', 'Airplane', 'Train', 'ship'],
    placeholder='교통 수단을 선택하시오.'
)
st.text(f'당신의 선택 : {option4}')


# slider (슬라이더)
st.header('slider (슬라이더) 실습 1')
score = st.slider('Your score is...', 0, 100, 1)
st.text(f'score : {score}')

st.header('slider (슬라이더) 실습 2')
from datetime import time

start_time, end_time = st.slider(
    'Working time is ...',
    min_value=time(0), max_value=time(23),
    value=(time(8), time(18)),
    format='HH:MM'
)
st.text(f'Working time : {start_time}, {end_time}')


# text input
st.header('text input 실습 1')
string = st.text_input(
    'Movie title',
    placeholder='write down the title of your favorite movie',
    max_chars=32
)
if string:
    st.text(f'Your answer is {string}')


# password 인자 사용
st.header('text input 실습 2')
string = st.text_input(
    'Movie title',
    placeholder='write down the title of your favorite movie',
    max_chars=32,
    type='password'
)
if string:
    st.text(f'Your answer is {string}')


import pandas as pd

# file uploader
st.header('file uploader 실습')
file = st.file_uploader(
    'Choose a file',
    type='csv',
    accept_multiple_files=False
)
if file is not None: # 파일이 있다면
    df = pd.read_csv(file)
    st.write(df)


# chart
st.header('chart 실습')
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset('tips')

fig, ax = plt.subplots()
sns.histplot(df, x='total_bill', ax=ax, hue='time')

st.pyplot(fig) # streamlit 대시보드에 표현


# image
st.header('image 실습')

from PIL import Image
img = Image.open('./output/bugs_image/1위_Smoke.jpg')
st.image(img, width=300, caption='Image from Naver')


#  sidebar
st.title('This is main page')

with st.sidebar:
    st.title('This is sidebar')
    side_option = st.multiselect(
        label='Your selection is',
        options=['lebao', 'Aibao', 'Fubao', 'Ruibao', 'Huibao'],
        placeholder='select panda!!'
    )


# tap
st.header('tap 실습')
tab1, tab2 = st.tabs(['Table', 'Graph'])

df = pd.read_csv('./input/midwest.csv')

with tab1:
    st.table(df.head(3))

with tab2:
    fig, ax = plt.subplots()
    sns.scatterplot(data=df, ax=ax)
    st.pyplot(fig)


# expander
st.header('expander 실습')
df = pd.read_csv('./input/midwest.csv')

fig, ax = plt.subplots()
sns.scatterplot(data=df, ax=ax)
st.pyplot(fig)

with st.expander('표를 보여줘!~~~ 빨리!!!'):
    st.table(df.head(10))
