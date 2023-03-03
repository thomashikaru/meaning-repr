def get_2x2(context1, context2, target1, target2, **kwargs):
    data = []
    data.append(
        {"context": context1, "target": target1, "condition": "congruent", **kwargs}
    )
    data.append(
        {"context": context2, "target": target2, "condition": "congruent", **kwargs}
    )
    data.append(
        {"context": context1, "target": target2, "condition": "incongruent", **kwargs}
    )
    data.append(
        {"context": context2, "target": target1, "condition": "incongruent", **kwargs}
    )
    return data
