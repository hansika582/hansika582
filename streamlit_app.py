import streamlit as st

# Title of the app
st.title("Simple Calculator")

# Input fields for the numbers and operation
num1 = st.number_input("Enter the first number", format="%.2f")
num2 = st.number_input("Enter the second number", format="%.2f")
operation = st.selectbox("Select an operation", ("Add", "Subtract", "Multiply", "Divide"))

# Perform calculations
if operation == "Add":
    result = num1 + num2
elif operation == "Subtract":
    result = num1 - num2
elif operation == "Multiply":
    result = num1 * num2
elif operation == "Divide":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero."

# Display the result
st.write("Result:", result)
