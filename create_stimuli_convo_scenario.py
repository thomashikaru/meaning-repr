import pandas as pd
import numpy as np
from tqdm import tqdm
import itertools
from utils import get_2x2

if __name__ == "__main__":
    ### CONVERSATION SCENARIO ###
    background_template = "{A} and {B} are sitting at a table having a conversation. {A} is {interaction} {B}."
    target_templates = {
        "teasing": {
            "indirect": "{A} is playfully mentioning an embarrassing thing that {B} did.",
            "direct": "{A} is making light-hearted jokes at {B}’s expense.",
        },
        "flirting with": {
            "indirect": "{A} is giggling each time {B} says something.",
            "direct": "{A} is playfully signaling romantic interest towards {B}.",
        },
        "respecting": {
            "indirect": "{A} is not interrupting {B}.",
            "direct": "{A} is being considerate towards {B}.",
        },
        "insulting": {
            "indirect": "{A} tells {B} that {B} is the dumbest person that {A} has ever met.",
            "direct": "{A} is saying hurtful things about {B}.",
        },
        "comforting": {
            "indirect": "{A} is patting {B} on the shoulder as {B} cries.",
            "direct": "{A} is trying to make {B} feel better.",
        },
        "envying": {
            "indirect": "{A} tries to act nonchalant when {B} talks about their promotion.",
            "direct": "{A} wishes they were in {B}'s place.",
        },
    }

    directnesses = ["indirect", "direct"]
    subjects = ["Alice", "Bob", "Charlie", "Barack Obama", "Donald Trump", "Mom", "Dad"]
    subject_combos = list(itertools.combinations(subjects, 2))
    data = []

    # the set of concept pairs
    interaction_pairs = [
        ("respecting", "insulting"),
        ("teasing", "comforting"),
        ("flirting with", "envying"),
    ]

    for (interaction1, interaction2) in interaction_pairs:
        print(f"{interaction1}_{interaction2}")
        for i, (directness, (sub1, sub2)) in enumerate(
            itertools.product(directnesses, subject_combos)
        ):
            data.extend(
                get_2x2(
                    background_template.format(
                        A=sub1, B=sub2, interaction=interaction1
                    ),
                    background_template.format(
                        A=sub1, B=sub2, interaction=interaction2
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
    df.to_csv("data/stimuli/convo_scenario.csv", index=False)

