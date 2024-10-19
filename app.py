import streamlit as st

# Title of the app
st.title("Simple Calculator")

# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

# Input numbers from user
num1 = st.number_input("Enter first number:", step=1.0)
num2 = st.number_input("Enter second number:", step=1.0)

# Select operation
operation = st.selectbox("Choose an operation", ("Add", "Subtract", "Multiply", "Divide"))

# Perform the calculation based on the selected operation
if st.button("Calculate"):
    if operation == "Add":
        result = add(num1, num2)
        st.success(f"The result is: {result}")
    elif operation == "Subtract":
        result = subtract(num1, num2)
        st.success(f"The result is: {result}")
    elif operation == "Multiply":
        result = multiply(num1, num2)
        st.success(f"The result is: {result}")
    elif operation == "Divide":
        result = divide(num1, num2)
        st.success(f"The result is: {result}")
