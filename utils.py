COL_ORDER = ["item", "stim_classname", "directness", "condition", "context", "target"]


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


def sort_colnames(df):
    def find(x):
        if x in COL_ORDER:
            return COL_ORDER.index(x)
        else:
            return len(COL_ORDER)

    return df.reindex(sorted(df.columns, key=find), axis=1)
