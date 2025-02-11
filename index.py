import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Tiêu đề trang web
st.title("Trang Web Streamlit Đơn Giản")

# Giới thiệu
st.write("""
    Chào mừng bạn đến với trang web Streamlit đầu tiên của tôi!
    Đây là một trang web đơn giản được xây dựng bằng Streamlit.
""")

# Thêm đầu vào từ người dùng
name = st.text_input("Nhập tên của bạn:")
if name:
    st.write(f"Chào {name}, cảm ơn bạn đã ghé thăm trang web của tôi!")

# Slider để chọn giá trị
age = st.slider("Chọn tuổi của bạn", 1, 100, 25)
st.write(f"Tuổi của bạn là {age}.")

# Hiển thị hình ảnh
st.write("Dưới đây là một bức tranh bạn có thể xem:")

# Tạo hình ảnh giả lập và hiển thị
img = np.random.rand(100, 100)
st.image(img, caption="Ảnh ngẫu nhiên", use_column_width=True)

# Vẽ biểu đồ
st.write("Dưới đây là biểu đồ hàm số sin(x):")

# Dữ liệu vẽ biểu đồ
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Vẽ biểu đồ
fig, ax = plt.subplots()
ax.plot(x, y, label='sin(x)', color='b')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Biểu đồ hàm sin(x)')
ax.legend()

# Hiển thị biểu đồ trong Streamlit
st.pyplot(fig)

# Thêm một số tính năng bổ sung như nút bấm
if st.button('Click me'):
    st.write('Bạn đã nhấn nút!')