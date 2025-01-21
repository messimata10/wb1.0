import streamlit as st
import pandas as pd
import numpy as np

def main():
    # 基础页面配置
    st.set_page_config(
        page_title="金融分析平台",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    st.title("金融数据分析平台")
    
    # 简单的侧边栏
    with st.sidebar:
        st.header("选项")
        mode = st.radio(
            "选择模式",
            ["数据概览", "风险分析"]
        )
    
    # 主内容区
    if mode == "数据概览":
        st.header("数据概览")
        
        # 生成示例数据
        data = {
            "月份": ["1月", "2月", "3月", "4月", "5月"],
            "收入": [100, 120, 150, 140, 160],
            "支出": [80, 85, 90, 95, 100]
        }
        df = pd.DataFrame(data)
        
        # 显示数据表格
        st.dataframe(df)
        
        # 显示基础统计信息
        col1, col2 = st.columns(2)
        with col1:
            st.metric("总收入", f"{sum(data['收入'])}")
        with col2:
            st.metric("总支出", f"{sum(data['支出'])}")
            
    else:
        st.header("风险分析")
        risk_score = st.slider("风险评分", 0, 100, 50)
        
        if risk_score < 30:
            st.success("低风险")
        elif risk_score < 70:
            st.warning("中等风险")
        else:
            st.error("高风险")

if __name__ == "__main__":
    main()
