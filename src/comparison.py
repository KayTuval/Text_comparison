import difflib
import re


def normalize_text(text):
    """
    Normalize text by separating punctuation from words.
    """
    return re.findall(r'\w+|[^\w\s]', text, re.UNICODE)


def compare_claims(claim1: str, claim2: str, debug=False):
    """
    Compares two claims and returns the differences in a structured format.

    Args:
        claim1 (str): The first claim.
        claim2 (str): The second claim.
        debug (bool): If True, print debug information.

    Returns:
        List[Tuple[str, str]]: A list of tuples, each containing a segment of text and its type ('unchanged', 'added', 'deleted').
    """
    # Normalize the claims by separating words and punctuation
    claim1_words = normalize_text(claim1)
    claim2_words = normalize_text(claim2)

    if debug:
        print(f"Claim 1 words: {claim1_words}")
        print(f"Claim 2 words: {claim2_words}")

    # Use SequenceMatcher to find the differences between the two claims
    matcher = difflib.SequenceMatcher(None, claim1_words, claim2_words)
    result = []

    # Iterate through the matching blocks and differences
    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if debug:
            print(f"Tag: {tag}, claim1[{i1}:{i2}] = {claim1_words[i1:i2]}, claim2[{j1}:{j2}] = {claim2_words[j1:j2]}")

        # Process the opcodes and categorize the changes
        if tag == 'equal':
            for word in claim1_words[i1:i2]:
                result.append((word, 'unchanged'))
        elif tag == 'insert':
            for word in claim2_words[j1:j2]:
                result.append((word, 'added'))
        elif tag == 'delete':
            for word in claim1_words[i1:i2]:
                result.append((word, 'deleted'))
        elif tag == 'replace':
            for word in claim1_words[i1:i2]:
                result.append((word, 'deleted'))
            for word in claim2_words[j1:j2]:
                result.append((word, 'added'))

    if debug:
        print(f"Result: {result}")
    return result


# Test compare_claims function with debug enabled
claim1 = "A connector section."
claim2 = "A connector section for a liquid transfer device."

print(f"Comparison result: {compare_claims(claim1, claim2, debug=True)}")
