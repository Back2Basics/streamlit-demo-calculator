import streamlit as st
import sympy as sp

st.title("Calculator")
st.write("This is a simple calculator app")

ans = 0

def show_display(display):
    """displays the input"""
    st.success(display)

def calculate(display):
    """sends the input to sympy for evaluation"""
    global ans
    try:
        ans = sp.sympify(display)
        ans = sp.simplify(ans)
        st.success(f"Answer = {ans}")
    except Exception as e:
        st.write("Error: ", e)


main, sidebutton= st.columns(2)
with main:
    display = st.text_input("Enter your expression", value="0", key="display")
with sidebutton:
    #create a space
    st.write("")
    st.write("")
    Calculate = st.button("Calculate")

if Calculate:
    calculate(display)

left, middle, right, operators, *_ = st.columns(13)
with left:
    button1 = st.button("1")
    button4 = st.button("4")
    button7 = st.button("7")
    buttonc = st.button("c")

with middle:
    button2 = st.button("2")
    button5 = st.button("5")
    button8 = st.button("8")
    button0 = st.button("0")

with right:
    button3 = st.button("3")
    button6 = st.button("6")
    button9 = st.button("9")
    equals = st.button("=")

with operators:
    button_plus = st.button("+.")
    button_minus = st.button("-.")
    button_multiply = st.button("*.")
    button_divide = st.button("/")

if button1:
    display = display + "1"
# create the rest of the button actions
if button2:
    display = display + "2"
if button3:
    display = display + "3"
if button4:
    display = display + "4"
if button5:
    display = display + "5"
if button6:
    display = display + "6"
if button7:
    display = display + "7"
if button8:
    display = display + "8"
if button9:
    display = display + "9"
if button0:
    display = display + "0"
if buttonc:
    display = "0"
if button_plus:
    display = display + "+"
if button_minus:
    display = display + "-"
if button_multiply:
    display = display + "*"
if button_divide:
    display = display + "/"
    st.session_state['display']= display
    show_display(display)


if equals:
    calculate(display)

