import streamlit as st
import sympy as sp

st.title("Calculator")
st.write("This is a simple calculator app")

ans = 0
st.session_state["display"] = st.session_state.get("display", "")


def show_display(display):
    """displays the input"""
    st.success(display)


def calculate():
    """sends the input to sympy for evaluation"""
    global ans
    try:
        ans = sp.sympify(st.session_state["display"])
        ans = sp.simplify(ans)
        st.success(f"Answer = {ans}")
    except Exception as e:
        st.write("Error: ", e)


main, sidebutton = st.columns(2)
with main:
    st.text_input("Enter your expression",
                  value=st.session_state.get('display', ""), key="input_text")

with sidebutton:
    # create a space
    st.write("")
    st.write("")
    Calculate = st.button("Calculate")

if Calculate:
    calculate()

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
    st.session_state.display = st.session_state.display + "1"
    show_display(st.session_state.display)
    st.experimental_rerun()
    # create the rest of the button actions
if button2:
    st.session_state.display = st.session_state.display + "2"
    show_display(st.session_state.display)
    st.experimental_rerun()
if button3:
    st.session_state.display = st.session_state.get('display', '') + "3"
    show_display(st.session_state.display)
    st.experimental_rerun()
if button4:
    st.session_state.display = st.session_state.get('display', '') + "4"
    show_display(st.session_state.display)
    st.experimental_rerun()
if button5:
    st.session_state.display = st.session_state.get('display', '') + "5"
    show_display(st.session_state.display)
    st.experimental_rerun()
if button6:
    st.session_state.display = st.session_state.get('display', '') + "6"
    st.experimental_rerun()
if button7:
    st.session_state.display = st.session_state.get('display', '') + "7"
    st.experimental_rerun()
if button8:
    st.session_state.display = st.session_state.get('display', '') + "8"
    st.experimental_rerun()
if button9:
    st.session_state.display = st.session_state.get('display', '') + "9"
    st.experimental_rerun()
if button0:
    st.session_state.display = st.session_state.get('display', '') + "0"
    st.experimental_rerun()
if buttonc:
    st.session_state.display = ""
    st.experimental_rerun()
if button_plus:
    st.session_state.display = st.session_state.get('display', '') + "+"
    st.experimental_rerun()
if button_minus:
    st.session_state.display = st.session_state.get('display', '') + "-"
    st.experimental_rerun()
if button_multiply:
    st.session_state.display = st.session_state.get('display', '') + "*"
    st.experimental_rerun()
if button_divide:
    st.session_state.display = st.session_state.get('display', '') + "/"
    st.experimental_rerun()


if equals:
    calculate()
