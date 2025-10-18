import streamlit as st
import base64
import requests
from io import BytesIO

st.set_page_config(page_title="徐老板的祝福", page_icon="🌏")

st.title("徐傲然祝您八方来财")
st.subheader("是不是很招笑")
st.write("想笑就笑")

def image_to_base64_from_url(url):
    """从网络URL获取图片并转换为base64"""
    try:
        # 设置超时时间
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # 如果请求失败会抛出异常
        
        # 转换为base64
        image_base64 = base64.b64encode(response.content).decode()
        
        # 根据图片类型设置MIME类型
        if url.lower().endswith('.png'):
            mime_type = "image/png"
        else:
            mime_type = "image/jpeg"
            
        return f"data:{mime_type};base64,{image_base64}"
    except requests.exceptions.Timeout:
        st.error("⏰ 图片加载超时，请检查网络连接")
        return None
    except requests.exceptions.RequestException as e:
        st.error(f"🌐 网络错误: {e}")
        return None
    except Exception as e:
        st.error(f"❌ 图片处理失败: {e}")
        return None

# 使用base64显示图片
image_url = "https://github.com/1125576393-png/attempt/blob/main/fdf5dd03f1e49af64447cc8d2079a0d4.jpg?raw=true"

# 显示加载状态
with st.spinner("🖼️ 正在加载图片..."):
    base64_image = image_to_base64_from_url(image_url)

if base64_image:
    # 使用markdown显示base64图片
    st.markdown(
        f'<img src="{base64_image}" alt="八方来财" style="width:100%; border-radius:10px;">', 
        unsafe_allow_html=True
    )
    st.caption("八方来财")
else:
    # 备用方案：尝试直接显示
    st.warning("⚠️ 使用备用方案加载图片...")
    try:
        st.image(image_url, caption="八方来财", use_container_width=True)
    except:
        st.error("🎯 图片加载失败，请检查：")
        st.write("1. 网络连接")
        st.write("2. 图片链接是否正确")
        st.write("3. 稍后刷新页面重试")

# 用户交互部分
st.write("---")
letter = st.text_input("请留下一段你写的话:")
if st.button("点击回复"):
    if letter:
        st.success(f"是的，你的这段话，{letter}！说的真对 👋")
    else:
        st.warning("请先输入一段话")

# 添加网络状态提示
st.sidebar.write("---")
st.sidebar.subheader("系统状态")
try:
    test_response = requests.get("https://www.github.com", timeout=5)
    st.sidebar.success("✅ 网络连接正常")
except:
    st.sidebar.warning("🌐 网络连接较慢")
