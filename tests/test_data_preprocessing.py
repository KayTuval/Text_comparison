import unittest
from src.data_preprocessing import parse_claims, apply_order_mapping


class TestDataPreprocessing(unittest.TestCase):
    maxDiff = None  # To see the full diff in case of a test failure

    def test_parse_claims(self):
        text = """1. A connector section for a liquid transfer apparatus, the
        connector section comprising: an outer body having a proximal end adapted to be attached to syringe and an open distal
        end; at least one hollow needle fixedly attached to the
        proximal end of the body of the connector section, the
        needle having at least one port at a lower end thereof
        adjacent to a pointed distal tip thereof that allows fluid
        communication between the exterior and the hollow interior
        of the needle; and a septum holder located inside of the outer
        body of the connector section, the septum holder comprising
        at least two parts, wherein the at least two parts of the
        septum holder comprise a body part and a septum support
        that are moveable towards and away from ach other, and a
        septum attached to the septum support, wherein the body
        part and septum support are configured to be locked to each
        other at the end of the movement towards ach other in a
        position in which the septum is closest to the body part
        wherein the body part releasably holds the septum holder in
        an unblocked configuration in which a fluid-flow through the
        at last on port of the hollow needle is allowed, and the
        movement of the body part and the septum support away
        from each other is locked in a blocked configuration in
        which the fluid-flow through the at least one port of the
        hollow needle is blocked.

        2. The connector section of claim 1, wherein the body part
        and the septum support comprise components configured to
        releasably hold the septum support in the unblocked con-
        figuration and to allow it to be moved relative to the body
        part and to be locked in the blocked configuration.

        3. The connector section according to claim 1, wherein the
        septum support comprises a septum seat and the septum
        support comprising opening to accommodate an insert comprising at least one bore that forms a seat of a needle valve."""

        expected = [
            "1. A connector section for a liquid transfer apparatus, the connector section comprising: an outer body having a proximal end adapted to be attached to syringe and an open distal end; at least one hollow needle fixedly attached to the proximal end of the body of the connector section, the needle having at least one port at a lower end thereof adjacent to a pointed distal tip thereof that allows fluid communication between the exterior and the hollow interior of the needle; and a septum holder located inside of the outer body of the connector section, the septum holder comprising at least two parts, wherein the at least two parts of the septum holder comprise a body part and a septum support that are moveable towards and away from ach other, and a septum attached to the septum support, wherein the body part and septum support are configured to be locked to each other at the end of the movement towards ach other in a position in which the septum is closest to the body part wherein the body part releasably holds the septum holder in an unblocked configuration in which a fluid-flow through the at last on port of the hollow needle is allowed, and the movement of the body part and the septum support away from each other is locked in a blocked configuration in which the fluid-flow through the at least one port of the hollow needle is blocked.",
            "2. The connector section of claim 1, wherein the body part and the septum support comprise components configured to releasably hold the septum support in the unblocked con- figuration and to allow it to be moved relative to the body part and to be locked in the blocked configuration.",
            "3. The connector section according to claim 1, wherein the septum support comprises a septum seat and the septum support comprising opening to accommodate an insert comprising at least one bore that forms a seat of a needle valve."
        ]

        parsed_claims = parse_claims(text)
        # Normalize spaces for comparison
        normalized_parsed_claims = [' '.join(claim.split()) for claim in parsed_claims]
        normalized_expected = [' '.join(claim.split()) for claim in expected]

        self.assertEqual(normalized_parsed_claims, normalized_expected)

    def test_parse_claims_empty(self):
        text = ""
        with self.assertRaises(ValueError):
            parse_claims(text)

    def test_apply_order_mapping(self):
        claims = ["Claim 1", "Claim 2", "Claim 3"]
        mapping = [3, 1, 2]
        expected = ["Claim 3", "Claim 1", "Claim 2"]
        self.assertEqual(apply_order_mapping(claims, mapping), expected)

    def test_apply_order_mapping_out_of_range(self):
        claims = ["Claim 1", "Claim 2", "Claim 3"]
        mapping = [4, 1, 2]
        with self.assertRaises(IndexError):
            apply_order_mapping(claims, mapping)


if __name__ == '__main__':
    unittest.main()
