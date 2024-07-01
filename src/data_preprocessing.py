from typing import List
import re


def parse_claims(text: str) -> List[str]:
    """
    Splits the input text into individual claims based on claim numbers.

    Args:
        text (str): The input text containing claims.

    Returns:
        List[str]: A list of individual claims.

    Raises:
        ValueError: If the input text is empty.
    """
    if not text.strip():
        raise ValueError("Input text is empty.")

    # Split the text by claim numbers using regex
    claims = re.split(r'\s*(?=\d+\.\s)', text.strip())
    return [claim.strip() for claim in claims if claim.strip()]


def apply_order_mapping(original_claims: List[str], mapping: List[int]) -> List[str]:
    """
    Rearranges the original claims based on the provided order mapping.

    Args:
        original_claims (List[str]): List of original claims.
        mapping (List[int]): List of indices indicating the new order of claims.

    Returns:
        List[str]: List of claims rearranged according to the mapping.

    Raises:
        IndexError: If an index in the mapping is out of range.
    """
    if not all(1 <= i <= len(original_claims) for i in mapping):
        raise IndexError("Mapping contains indices out of range.")
    return [original_claims[i - 1] for i in mapping]
