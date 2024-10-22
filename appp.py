import streamlit as st

# Define the chatbot function for Streamlit
def chatbot():
    st.title("Clothing with Dignity - Chatbot")
    
    st.write("Welcome to the Clothing with Dignity chatbot! How can we assist you today?")
    
    # Dropdown menu for user to choose an option
    choice = st.selectbox("Select an option", 
                          ["Learn about the Project", 
                           "How does the project maintain sustainability?", 
                           "How to donate clothes?", 
                           "How to purchase clothes?", 
                           "Cities where we operate", 
                           "How can laundromats or businesses partner with you?", 
                           "Contact Us"])

    # Handle different user choices
    if choice == "Learn about the Project":
        st.write('''
        "Clothing with Dignity" is a socially-driven initiative aimed at providing clean, dignified, 
        and affordable clothing to underprivileged communities. We believe that everyone deserves 
        to wear clean and presentable clothes, and our project works to empower individuals by 
        offering them well-maintained clothes at a minimal cost.
        ''')
    
    elif choice == "How does the project maintain sustainability?":
        st.write('''
        The project maintains sustainability by charging a small fee (PKR 150 per dress), which covers 
        operational costs such as washing, ironing, and repairs. Additionally, donations and partnerships 
        with local businesses help us keep the initiative running and allow us to expand our services.
        ''')
    
    elif choice == "How to donate clothes?":
        st.write('''
        Donating clothes is easy! You can drop off your gently used clothing at one of our collection 
        points or reach out to us for pickup services. We ensure that all donated clothes are carefully 
        cleaned, repaired, and packaged before being distributed to our beneficiaries.
        ''')
    
    elif choice == "How to purchase clothes?":
        st.write('''
        You can purchase clothes from our initiative at a very affordable price of PKR 150 per dress. 
        The clothes are well-maintained, washed, ironed, and repaired as needed. This ensures that 
        you are buying something of dignity and value.
        ''')
    
    elif choice == "Cities where we operate":
        st.write('''
        Currently, we are operating in the following cities:
        - Abbottabad, KPK
        - Rawalpindi
        - DG Khan
        - Mianwali
        - Burewala
        - Peshawar
        If you're in any of these cities, feel free to visit our collection points or contact us for more information.
        ''')
    
    elif choice == "How can laundromats or businesses partner with you?":
        st.write('''
        We welcome partnerships with local laundromats and businesses! If you're interested in collaborating, 
        you can help by providing discounted laundry services, donating clothing, or supporting our project 
        financially. Please contact us for more information on how we can work together.
        ''')
    
    elif choice == "Contact Us":
        st.write('''
        For any inquiries, please contact us via email at dignity.clothing@gmail.com or reach out through 
        our social media channels.
        ''')

# Run the chatbot function
if __name__ == "__main__":
    chatbot()
