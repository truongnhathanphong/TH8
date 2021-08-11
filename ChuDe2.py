import streamlit as st
import pandas as pd
import math

st.header("Bài thực hành chủ đề 2")
# Bài 1 (TH8CD201)
st.write("***")
st.subheader(""" Bài 1 (mã bài TH8CD201). Viết chương trình tính diện tích tam giác khi biết độ dài cạnh đáy và chiều cao. 
""")
st.text("Input")
# Tạo bảng input
st.write(pd.DataFrame({
    'STT': [1, 2, 3],
    'a': [10, 20, 30],
    'ha': [5, 6, 7.5]
}))

# Nhập bộ test
Bai1a = st.text_input("(Mã bài TH8CD201). Nhập a")
Bai1ha = st.text_input("(Mã bài TH8CD201). Nhập ha")

# Người dùng nhập kết quả
UserResult1 = st.text_input("Nhập kết quả (mã bài TH8CD201) của bạn vào ô này")
st.write("Kết quả của bạn " + UserResult1)

# Máy tính toán kết quả
if (Bai1ha != "") & (Bai1a != ""):
    ComResult1 = float(Bai1a) * float(Bai1ha) / 2

# So sánh kết quả giữa người và máy
if (UserResult1 != ""):
    if float(UserResult1) == round(ComResult1, 1):
        st.write("Chúc mừng bạn đã vượt qua bộ test này. Hãy tiếp tục")
    else:
        st.write("Bạn cần xem lại chương trình")
st.write("***")

# Bài 2 (TH8CD202)
st.subheader(""" Bài 2 (mã bài TH8CD202). Hãy viết chương trình nhập vào bán kính hình tròn, sau đó tính diện tích hình tròn. 
""")
st.text("Input")
# Tạo bảng input
st.write(pd.DataFrame({
    'STT': [1, 2, 3],
    'R': [10, 20, 30],
}))

# Nhập bộ test
R2 = st.text_input("(Mã bài TH8CD202). Nhập bán kính R")

# Người dùng nhập kết quả
UserResult2 = st.text_input("Nhập kết quả (mã bài TH8CD202) của bạn vào ô này")
st.write("Kết quả của bạn " + UserResult2)

# Máy tính toán kết quả
if R2 != "":
    ComResult2 = 3.14 * float(R2) * float(R2)

# So sánh kết quả giữa người và máy
if (UserResult2 != ""):
    if float(UserResult2) == round(ComResult2, 1):
        st.write("Chúc mừng bạn đã vượt qua bộ test này. Hãy tiếp tục")
    else:
        st.write("Bạn cần xem lại chương trình")
st.write("***")

# Bài 3 (TH8CD203)
st.subheader(""" Bài 3 (mã bài TH8CD203). Hãy viết chương trình nhập vào cạnh hình vuông (c), sau đó tính diện tích hình vuông. 
""")
st.text("Input")
# Tạo bảng input
st.write(pd.DataFrame({
    'STT': [1, 2, 3],
    'c': [10, 20, 30],
}))

# Nhập bộ test
c3 = st.text_input("(Mã bài TH8CD203). Nhập cạnh c")

# Người dùng nhập kết quả
UserResult3 = st.text_input("Nhập kết quả (mã bài TH8CD203) của bạn vào ô này")
st.write("Kết quả của bạn " + UserResult3)

# Máy tính toán kết quả
if c3 != "":
    ComResult3 = float(c3) * float(c3)

# So sánh kết quả giữa người và máy
if (UserResult3 != ""):
    if float(UserResult3) == round(ComResult3, 1):
        st.write("Chúc mừng bạn đã vượt qua bộ test này. Hãy tiếp tục")
    else:
        st.write("Bạn cần xem lại chương trình")
st.write("***")

# Bài 4 (TH8CD204)
st.subheader(""" Bài 4 (mã bài TH8CD204). Hãy viết chương trình nhập vào cạnh hình vuông (c), sau đó tính chu vi hình vuông. 
""")
st.text("Input")
# Tạo bảng input
st.write(pd.DataFrame({
    'STT': [1, 2, 3],
    'c': [10, 20, 30],
}))

# Nhập bộ test
c4 = st.text_input("(Mã bài TH8CD204). Nhập cạnh c")

# Người dùng nhập kết quả
UserResult4 = st.text_input("Nhập kết quả (mã bài TH8CD204) của bạn vào ô này")
st.write("Kết quả của bạn " + UserResult4)

# Máy tính toán kết quả
if c4 != "":
    ComResult4 = 4 * float(c4)

# So sánh kết quả giữa người và máy
if (UserResult4 != ""):
    if float(UserResult4) == round(ComResult4, 1):
        st.write("Chúc mừng bạn đã vượt qua bộ test này. Hãy tiếp tục")
    else:
        st.write("Bạn cần xem lại chương trình")
st.write("***")

# Bài 5 (TH8CD205)
st.subheader(""" Bài 5 (mã bài TH8CD202). Hãy viết chương trình nhập vào bán kính hình tròn, sau đó tính chu vi hình tròn. 
""")
st.text("Input")
# Tạo bảng input
st.write(pd.DataFrame({
    'STT': [1, 2, 3],
    'R': [10, 20, 30],
}))

# Nhập bộ test
R5 = st.text_input("(Mã bài TH8CD205). Nhập bán kính R")

# Người dùng nhập kết quả
UserResult5 = st.text_input("Nhập kết quả (mã bài TH8CD205) của bạn vào ô này")
st.write("Kết quả của bạn " + UserResult5)

# Máy tính toán kết quả
if R5 != "":
    ComResult5 = 2 * 3.14 * float(R5)
# So sánh kết quả giữa người và máy
if (UserResult5 != ""):
    if float(UserResult5) == round(ComResult5, 1):
        st.write("Chúc mừng bạn đã vượt qua bộ test này. Hãy tiếp tục")
    else:
        st.write("Bạn cần xem lại chương trình")
st.write("***")

# Bài 6
st.subheader(""" Bài 6 (mã bài TH8CD206). Hãy viết chương trình nhập vào độ dài ba cạnh của tam giác (a, b, c), sau đó tính chu vi tam giác. 
""")
st.text("Input")
# Tạo bảng input
st.write(pd.DataFrame({
    'STT': [1, 2, 3],
    'a': [3, 6, 9],
    'b': [4, 8, 12],
    'c': [5, 10, 15]
}))

# Nhập bộ test
a6 = st.text_input("(Mã bài TH8CD206). Nhập cạnh a")
b6 = st.text_input("(Mã bài TH8CD206). Nhập cạnh b")
c6 = st.text_input("(Mã bài TH8CD206). Nhập cạnh c")

# Người dùng nhập kết quả
UserResult6 = st.text_input("Nhập kết quả (mã bài TH8CD206) của bạn vào ô này")
st.write("Kết quả của bạn " + UserResult6)

# Máy tính toán kết quả
if (a6 != "") & (b6 != "") & (c6 != ""):
    ComResult6 = float(a6) + float(b6) + float(c6)

# So sánh kết quả giữa người và máy
if (UserResult6 != ""):
    if float(UserResult6) == round(ComResult6, 1):
        st.write("Chúc mừng bạn đã vượt qua bộ test này. Hãy tiếp tục")
    else:
        st.write("Bạn cần xem lại chương trình")
st.write("***")

# Bài 7
st.subheader(""" Bài 7 (mã bài TH8CD207). Hãy viết chương trình nhập vào độ dài đáy lớn (dl), độ dài đáy nhỏ (dn) và chiều cao hình thang (h), sau đó tính diện tích hình thang. 
""")
st.text("Input")
# Tạo bảng input
st.write(pd.DataFrame({
    'STT': [1, 2, 3],
    'dl': [3, 6, 9],
    'dn': [4, 8, 12],
    'h': [5, 10, 15]
}))

# Nhập bộ test
dl7 = st.text_input("(Mã bài TH8CD206). Nhập đáy lớn dl")
dn7 = st.text_input("(Mã bài TH8CD206). Nhập đáy nhỏ dn")
h7 = st.text_input("(Mã bài TH8CD206). Nhập chiều cao h")

# Người dùng nhập kết quả
UserResult7 = st.text_input("Nhập kết quả (mã bài TH8CD207) của bạn vào ô này")
st.write("Kết quả của bạn " + UserResult7)

# Máy tính toán kết quả
if (dl7 != "") & (dn7 != "") & (h7 != ""):
    ComResult7 = (float(dl7) + float(dn7)) * float(c6) / 2;

# So sánh kết quả giữa người và máy
if (UserResult7 != ""):
    if float(UserResult7) == round(ComResult7, 1):
        st.write("Chúc mừng bạn đã vượt qua bộ test này. Hãy tiếp tục")
    else:
        st.write("Bạn cần xem lại chương trình")
st.write("***")

# Bài 8
st.subheader(""" Bài 8 (mã bài TH8CD208). Hãy viết chương trình nhập vào độ dài hai cạnh bên (cb1, cb2), sau đó tính chu vi hình bình hành. 
""")
st.text("Input")
# Tạo bảng input
st.write(pd.DataFrame({
    'STT': [1, 2, 3],
    'cb1': [10, 20, 30],
    'cb2': [5, 6, 7.5]
}))

# Nhập bộ test
cb18 = st.text_input("(Mã bài TH8CD208). Nhập cb1")
cb28 = st.text_input("(Mã bài TH8CD208). Nhập cb2")

# Người dùng nhập kết quả
UserResult8 = st.text_input("Nhập kết quả (mã bài TH8CD208) của bạn vào ô này")
st.write("Kết quả của bạn " + UserResult8)

# Máy tính toán kết quả
if (cb18 != "") & (cb28 != ""):
    ComResult8 = (float(cb18) + float(cb28)) * 2

# So sánh kết quả giữa người và máy
if UserResult8 != "":
    if float(UserResult8) == round(ComResult8, 1):
        st.write("Chúc mừng bạn đã vượt qua bộ test này. Hãy tiếp tục")
    else:
        st.write("Bạn cần xem lại chương trình")
