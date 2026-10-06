DIMENSIONS=("dialect_authenticity","semantic_accuracy","contextual_understanding","cultural_relevance","naturalness","grammar_morphology","intent_preservation")
def validate_scores(scores):
    if set(scores)!=set(DIMENSIONS): raise ValueError("Scores must contain exactly all seven dimensions.")
    for k,v in scores.items():
        if not isinstance(v,int) or not 1<=v<=5: raise ValueError(f"{k} must be an integer from 1 to 5")
    return True
def summarize(scores):
    validate_scores(scores)
    total=sum(scores.values())
    return {"total":total,"max_total":35,"average":round(total/7,2)}
