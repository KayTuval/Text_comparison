import streamlit as st
from src.comparison import compare_claims
from src.data_preprocessing import parse_claims, apply_order_mapping

# Display the logo

st.title('Patent Claims Comparison')
st.subheader('Be sure not to input any private information')

tab1, tab2 = st.tabs(["Compare Individual Claims", "Compare Claim Sets with Order Mapping"])

with tab1:
    st.header("Compare Individual Claims")
    # Text input for claims
    claim1 = st.text_area('Insert a claim', height=200,
                          placeholder="Enter claim here...")
    claim2 = st.text_area('Insert a claim to compare it with', height=200,
                          placeholder="Enter claim here...")

    # Button to trigger comparison
    if st.button('Compare'):
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

with tab2:
    st.header("Compare Claim Sets with Order Mapping")
    # Text input for original and granted claims
    granted_claims_text = st.text_area('Granted Claims', height=200,
                                        placeholder="Enter claims here...")
    original_claims_text = st.text_area('Original Claims', height=200,
                                       placeholder="Enter claims here...")
    order_mapping = st.text_area('Enter a comma-separated list of integers that represent the new order of the original claims.', height=200, placeholder="For example, if the claims are in the order 1, 2, 3 and you want to rearrange them so that the third claim comes first, the first claim comes second, and the second claim comes last, you would enter 3, 1, 2.")

    # Button to trigger comparison
    if st.button('Compare Sets'):
        try:
            original_claims = parse_claims(original_claims_text)
            granted_claims = parse_claims(granted_claims_text)
            mapping = [int(i) for i in order_mapping.split(',')]
            ordered_original_claims = apply_order_mapping(original_claims, mapping)

            st.write('Comparison Results for Each Claim:')
            for i, (orig_claim, grant_claim) in enumerate(zip(ordered_original_claims, granted_claims)):
                st.write(f"Comparing Claim {i + 1}")
                diff = compare_claims(orig_claim, grant_claim)

                formatted_result = ""
                for word, status in diff:
                    if status == 'unchanged':
                        formatted_result += f"{word} "
                    elif status == 'added':
                        formatted_result += f"<span style='color: green; font-weight: bold;'>{word}</span> "
                    elif status == 'deleted':
                        formatted_result += f"<span style='color: red; text-decoration: line-through;'>{word}</span> "

                st.markdown(formatted_result, unsafe_allow_html=True)
                st.markdown("---")
        except Exception as e:
            st.error(f"An error occurred: {e}")
