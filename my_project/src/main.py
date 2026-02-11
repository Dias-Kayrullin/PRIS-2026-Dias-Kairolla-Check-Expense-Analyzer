import streamlit as st
from mock_data import test_receipt as default_receipt
from logic import check_receipt_rules

st.set_page_config(page_title="Анализ чеков — Rule-Based система", layout="wide")

st.title("Rule-Based Система анализа чеков 🧾")

st.write("Изменяйте параметры тестового чека и проверяйте, проходит ли он правила.")

# Сайдбар для ввода данных
with st.sidebar:
    st.header("Параметры чека")
    
    total_amount = st.number_input(
        "Общая сумма чека (₸)",
        min_value=0.0,
        value=float(default_receipt["total_amount"]),
        step=100.0
    )
    
    has_alcohol = st.checkbox(
        "Содержит алкоголь?",
        value=default_receipt["has_alcohol"]
    )
    
    category = st.text_input(
        "Категория чека",
        value=default_receipt["category_text"]
    )
    
    items_count = st.number_input(
        "Количество позиций",
        min_value=1,
        value=default_receipt["items_count"],
        step=1
    )

# Кнопка запуска
if st.button("Проверить чек по правилам", type="primary"):
    # Собираем текущие данные
    current_data = {
        "category_text": category,
        "total_amount": total_amount,
        "items_count": items_count,
        "has_alcohol": has_alcohol,
        "tags": default_receipt["tags"]  # пока фиксированные, можно позже сделать редактируемыми
    }
    
    # Получаем результат
    result = check_receipt_rules(current_data)
    
    # Красиво выводим
    if "✅" in result:
        st.success(result)
    elif "⛔️" in result:
        st.error(result)
    else:
        st.warning(result)
    
    # Показываем, какие данные были проверены
    st.write("**Проверенные данные:**")
    st.json(current_data)