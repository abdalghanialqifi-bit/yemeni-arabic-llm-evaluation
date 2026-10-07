# Evaluation Prompt Templates

## Response evaluation

Evaluate the model response against the user's Yemeni Arabic input. Return:

- one 1–5 score for each benchmark dimension;
- zero or more failure categories;
- a concise explanation for every score below 5;
- whether the response preserves the user's intent;
- whether the wording is natural for the specified Yemeni context.

Do not assume that one Yemeni region represents every Yemeni speaker. If regional information is missing, explicitly mark uncertainty instead of inventing a universal rule.

## Pairwise comparison

Given two model responses to the same input, compare them on dialect authenticity, semantic accuracy, cultural relevance, naturalness, and intent preservation. Explain which response is preferable and identify concrete failure modes in the weaker response.
