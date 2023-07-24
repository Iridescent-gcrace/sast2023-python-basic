import streamlit as st
import pandas as pd
import numpy as np

# 设置页面标题
st.title('Streamlit 示例：简单的数据应用')

# 创建一个按钮，点击后显示提示信息
q = st.button('点击这里查看提示')

if q:
    st.write('这是一个简单的示例应用。你可以在左侧栏选择不同的选项来查看不同的数据。')

# 创建一个侧边栏选择框，用于选择不同的数据展示选项
option = st.sidebar.selectbox(
    '选择数据展示选项:',
    ('数据概览', '折线图', '柱状图')
)

# 创建一个虚拟数据集
data = pd.DataFrame({
    '日期': pd.date_range(start='2023-07-01', periods=10, freq='D'),
    '销量': np.random.randint(10, 100, 10)
})

# 根据用户选择的选项，展示不同的数据
if option == '数据概览':
    st.write('### 数据概览')
    st.dataframe(data)
elif option == '折线图':
    st.write('### 折线图')
    st.line_chart(data.set_index('日期'))
elif option == '柱状图':
    st.write('### 柱状图')
    st.bar_chart(data.set_index('日期'))
