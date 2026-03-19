import streamlit as st
import plotly.graph_objects as go

# ЭТА СТРОЧКА — ТЕСТ. Если она появится в браузере, значит мы победили!

# Настройка страницы
st.set_page_config(page_title="Колесо Баланса", layout="wide")

st.title("🎡 Мое Интерактивное Колесо Баланса")

# Список секторов
labels = ['Здоровье', 'Финансы', 'Карьера', 'Саморазвитие', 'Духовность', 'Отдых', 'Отношения', 'Семья']

# Боковая панель
values = []
st.sidebar.header("Настройка уровней (0-10)")
for label in labels:
    val = st.sidebar.slider(label, 0, 10, 5)
    values.append(val)

# Создаем график через Plotly
fig = go.Figure()

fig.add_trace(go.Scatterpolar(
    r=values + [values[0]],
    theta=labels + [labels[0]],
    fill='toself',
    fillcolor='rgba(136, 216, 208, 0.5)',
    line=dict(color='#45ada8', width=2),
    marker=dict(size=8)
))

fig.update_layout(
    polar=dict(
        radialaxis=dict(visible=True, range=[0, 10]),
    ),
    showlegend=False,
    height=600
)

# Выводим график
st.plotly_chart(fig, use_container_width=True)