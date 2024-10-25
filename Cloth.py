import streamlit as st

# Define the chatbot function for Streamlit
def chatbot():
    st.title("Clothing with Dignity - Chatbot")
    st.write("Welcome to the Clothing with Dignity chatbot! How can we assist you today?")

    # Dropdown menu for user to choose an option
    choice = st.selectbox("Select an option", [
        "Learn about the Project",
        "How does the project maintain sustainability?",
        "How to donate clothes?",
        "How to purchase clothes?",
        "Cities where we operate",
        "How can laundromats or businesses partner with you?",
        "Where are the clothes collected from?",
        "How do you package the clothes?",
        "Does your organization provide clothes only to those who can pay the fee?",
        "How can a donor contribute if they wish to donate in cash?",
        "How does your organization ensure the dignity and integrity of recipients?",
        "Can a donor contribute products other than clothes?",
        "Do we ensure the quality of clothes?",
        "What type of clothes do you accept for donation?",
        "How do you ensure donations reach the right people?",
        "Contact Us"
    ])

    # Handle different user choices and display responses
    if choice == "Learn about the Project":
        st.write('''
        "Clothing with Dignity" is a socially-driven initiative aimed at providing clean, dignified, 
        and affordable clothing to underprivileged communities. We believe that everyone deserves 
        to wear clean, presentable clothes, and our project works to empower individuals by 
        offering them well-maintained clothes at a minimal cost.
        ''')

    elif choice == "How does the project maintain sustainability?":
        st.write('''
        We maintain sustainability by charging a small fee (PKR 150 per dress), which covers 
        operational costs such as washing, ironing, and repairs. Additionally, donations and partnerships 
        with local businesses help keep the project running and allow us to expand our services.
        ''')

    elif choice == "How to donate clothes?":
        st.write('''
        Donating clothes is simple! You can drop off gently used clothing at one of our collection 
        points or reach out to us for pickup services. All donated clothes are cleaned, repaired, 
        and packaged before being distributed.
        ''')

    elif choice == "How to purchase clothes?":
        st.write('''
        You can purchase clothes from our initiative at an affordable price of PKR 150 per dress. 
        Each outfit is washed, ironed, and carefully packaged to ensure you receive something dignified and valuable.
        ''')

    elif choice == "Cities where we operate":
        st.write('''
        Currently, we are operating in the following cities:
        - Abbottabad, KPK
        - Rawalpindi, Punjab
        - DG Khan, Punjab
        - Mianwali, Punjab
        - Burewala, Punjab
        - Peshawar, KPK
        - Islamabad
        - Larkana, Sindh
        If you're in any of these areas, feel free to visit our collection points or contact us for more information.
        ''')

    elif choice == "How can laundromats or businesses partner with you?":
        st.write('''
        We welcome partnerships with laundromats and businesses! By providing discounted laundry services, donating clothes, 
        or supporting our project financially, you can make a significant impact. Please reach out to us to discuss partnership opportunities.
        ''')

    elif choice == "Where are the clothes collected from?":
        st.write('''
        We collect gently used clothes from various cities, including:
        - Abbottabad, KPK
        - Rawalpindi, Punjab
        - DG Khan, Punjab
        - Mianwali, Punjab
        - Burewala, Punjab
        - Peshawar, KPK
        - Islamabad
        - Larkana, Sindh
        ''')

    elif choice == "How do you package the clothes?":
        st.write('''
        Each outfit is carefully cleaned, ironed, and packaged to look as dignified as possible. This attention to detail
        helps our recipients feel they are making a dignified purchase, rather than receiving charity.
        ''')

    elif choice == "Does your organization provide clothes only to those who can pay the fee?":
        st.write('''
        Our organization charges a minimal fee to maintain dignity and sustainability. However, for those genuinely unable 
        to pay, we offer clothes free of charge after verifying their situation.
        ''')

    elif choice == "How can a donor contribute if they wish to donate in cash?":
        st.write('''
        If a donor wishes to contribute in cash, they can contact us directly to discuss payment options. All contributions go 
        toward maintaining and expanding our project.
        ''')

    elif choice == "How does your organization ensure the dignity and integrity of recipients?":
        st.write('''
        We are committed to preserving the dignity of everyone involved. By packaging clothes neatly and charging a minimal fee, 
        we enable recipients to feel empowered and respected. We prioritize maintaining this dignity in every interaction and transaction.
        ''')

    elif choice == "Can a donor contribute products other than clothes?":
        st.write('''
        Yes, donors can contribute items other than clothes if they are useful to our donation process. This is an evolving initiative, 
        and we plan to expand to accept other essentials as we grow.
        ''')

    elif choice == "Do we ensure the quality of clothes?":
        st.write('''
        Absolutely, we ensure that every piece of clothing donated meets our quality standards. Clothes are cleaned, ironed, and repaired as 
        needed to make sure they are presentable and dignified.
        ''')

    elif choice == "What type of clothes do you accept for donation?":
        st.write('''
        We accept gently used, good-quality clothing that is free from major damage. This ensures that every item we provide reflects the dignity 
        we aim to give our recipients.
        ''')

    elif choice == "How do you ensure donations reach the right people?":
        st.write('''
        We take care to ensure that all donations reach those in genuine need. By working closely with community leaders, teachers, and local organizations, 
        we identify deserving individuals and families in our target areas.
        ''')

    elif choice == "Contact Us":
        st.write('''
        For further details or questions, please contact us through:
        - WhatsApp: +923125691991
        - Email: dignity.clothing@gmail.com
        - Instagram: @Clothingwithdignity
        - Facebook: Clothing with Dignity
        ''')

# Run the chatbot function
if __name__ == "__main__":
    chatbot()
