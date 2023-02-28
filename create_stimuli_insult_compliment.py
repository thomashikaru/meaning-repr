import pandas as pd
import numpy as np
from tqdm import tqdm
import itertools


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


if __name__ == "__main__":
    ### INSULTS/COMPLIMENTS ###
    background_template = "{A} is talking about their {third_party} with {B}. {B} knows that {A}'s {third_party} {context}. {B} tells {A} 'You're just like your {third_party}'."
    target_templates = {
        "insulting": {
            "indirect": "{A}'s feelings are hurt.",
            "direct": "{B} meant this as an insult.",
        },
        "complimenting": {
            "indirect": "{A} smiles at {B}.",
            "direct": "{B} meant this as a compliment.",
        },
    }
    contexts = {
        "insulting": [
            "is abusive and violent",
            "abandoned {A}",
            "is unemployed and financially struggling",
            "does not have a good relationship with {A}",
            "spent several years in prison",
        ],
        "complimenting": [
            "is respected in the community",
            "recently won an award",
            "received a medal for bravery",
            "excelled academically and athletically",
            "is highly successful in the business world",
        ],
    }

    num_contexts = len(next(iter(contexts.values())))

    interactions = target_templates.keys()
    namesA = ["Alice", "Andrew", "A"]
    namesB = ["Bob", "Beatrice", "B"]
    directnesses = ["indirect", "direct"]
    third_parties = ["father", "mother", "brother", "sister", "partner"]

    data = []

    for a, b, interaction, directness, third_party, context_idx in tqdm(
        itertools.product(
            namesA,
            namesB,
            interactions,
            directnesses,
            third_parties,
            range(num_contexts),
        )
    ):
        bg = background_template
        tg = target_templates[interaction][directness]
        con = contexts[interaction][context_idx]
        con = con.format(A=a, B=b)
        bg = bg.format(
            A=a, B=b, interaction=interaction, context=con, third_party=third_party
        )
        tg = tg.format(A=a, B=b)
        data.append(
            {
                "background": bg,
                "target": tg,
                "A": a,
                "B": b,
                "interaction": interaction,
                "directness": directness,
            }
        )

    df = pd.DataFrame(data)
    df.to_csv("data/stimuli/insult_compliment.csv", index=False)

