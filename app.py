import streamlit as st

# Define the calculator function
def calculator():
    st.title("Simple Calculator")

    # Select the operation using a dropdown (selectbox)
    operation = st.selectbox("Choose an operation:", ["Addition", "Subtraction", "Multiplication", "Division"])
    
    # Input fields for numbers
    num1 = st.number_input("Enter the first number", format="%f")
    num2 = st.number_input("Enter the second number", format="%f")
    
    # Perform the calculation when the button is pressed
    if st.button("Calculate"):
        if operation == "Addition":
            result = num1 + num2
            st.success(f"Result: {num1} + {num2} = {result}")
            
        elif operation == "Subtraction":
            result = num1 - num2
            st.success(f"Result: {num1} - {num2} = {result}")
            
        elif operation == "Multiplication":
            result = num1 * num2
            st.success(f"Result: {num1} * {num2} = {result}")
            
        elif operation == "Division":
            if num2 != 0:
                result = num1 / num2
                st.success(f"Result: {num1} / {num2} = {result}")
            else:
                st.error("Error: Division by zero is not allowed.")

# Run the calculator app
if __name__ == "__main__":
    calculator()
