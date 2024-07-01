import streamlit as st
from src.comparison import compare_claims
from src.data_preprocessing import parse_claims, apply_order_mapping

# Display the logo
st.title('Text Comparison')
st.subheader('Be sure not to input any private information')

st.header("Compare Text")

# Create two columns
col1, col2 = st.columns(2)

# Text input for claims in two columns
with col1:
    claim1 = st.text_area('Insert text', height=200, placeholder="Enter text here...")

with col2:
    claim2 = st.text_area('Insert text to compare it with', height=200, placeholder="Enter text here...")

# Button to trigger comparison
if st.button('Compare'):
    try:
        if claim1 and claim2:
            diff = compare_claims(claim1, claim2)

            # Display results
            st.write('Comparison Result:')
            formatted_result = ""
            for word, status in diff:
                if status == 'unchanged':
                    formatted_result += f"{word} "
                elif status == 'added':
                    formatted_result += f"<span style='color: green; font-weight: bold;'>{word}</span> "
                elif status == 'deleted':
                    formatted_result += f"<span style='color: red; text-decoration: line-through;'>{word}</span> "

            st.markdown(formatted_result, unsafe_allow_html=True)
        else:
            st.error('Please enter both claims.')
    except Exception as e:
        st.error(f"An error occurred: {e}")
