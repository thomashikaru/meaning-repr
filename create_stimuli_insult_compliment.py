import pandas as pd
import numpy as np
from tqdm import tqdm
import itertools
from utils import get_2x2, sort_colnames


if __name__ == "__main__":
    ### INSULTS/COMPLIMENTS ###

    # together these form the background/context
    background_template = "{A} is talking about their {third_party} with {B}. {B} knows that {A}'s {third_party} {context}. {B} tells {A} 'You're just like your {third_party}'."
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

    # this is the target
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

    interactions = list(target_templates.keys())
    subjects = ["Alice", "Bob", "Charlie", "Barack Obama", "Donald Trump", "Mom", "Dad"]
    subject_combos = list(itertools.combinations(subjects, 2))
    namesA = ["Alice", "Andrew", "A"]
    namesB = ["Bob", "Beatrice", "B"]
    directnesses = ["indirect", "direct"]
    third_parties = ["father", "mother", "brother", "sister", "partner"]

    data = []

    interaction1, interaction2 = interactions[0], interactions[1]
    for i, (directness, (sub1, sub2), third_party, context_idx) in enumerate(
        itertools.product(
            directnesses, subject_combos, third_parties, range(num_contexts)
        )
    ):
        data.extend(
            get_2x2(
                background_template.format(
                    A=sub1,
                    B=sub2,
                    interaction=interaction1,
                    third_party=third_party,
                    context=contexts[interaction1][context_idx],
                ),
                background_template.format(
                    A=sub1,
                    B=sub2,
                    interaction=interaction2,
                    third_party=third_party,
                    context=contexts[interaction2][context_idx],
                ),
                target_templates[interaction1][directness].format(A=sub1, B=sub2),
                target_templates[interaction2][directness].format(A=sub1, B=sub2),
                subject1=sub1,
                subject2=sub2,
                directness=directness,
                item=i,
                stim_classname=f"{interaction1}_{interaction2}",
            )
        )

    df = pd.DataFrame(data)
    df = sort_colnames(df)
    df.to_csv("data/social_interactions/insult_compliment.csv", index=False)

