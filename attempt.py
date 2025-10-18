import streamlit as st

st.set_page_config(page_title="徐老板的祝福", page_icon="🌏")

st.title("徐傲然祝您八方来财")
st.subheader("是不是很招笑")
st.write("想笑就笑")

st.image("https://raw.githubusercontent.com/1125576393/attempt/main/fdf5dd03f1e49af64447cc8d2079a0d4.jpg", caption="八方来财", use_container_width=True)

letter = st.text_input("请留下一段你写的话:")
if st.button("点击回复"):
    st.success(f"是的，你的这段话，{letter}！说的真对 👋")


