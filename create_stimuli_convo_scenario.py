import pandas as pd
import numpy as np
from tqdm import tqdm
import itertools

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
            "indirect": "{A} tells {B} that they are the dumbest person that {A} has ever met.",
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

    interactions = target_templates.keys()
    namesA = ["Alice", "Andrew", "A"]
    namesB = ["Bob", "Beatrice", "B"]
    directnesses = ["indirect", "direct"]

    data = []

    for a, b, interaction, directness in tqdm(
        itertools.product(namesA, namesB, interactions, directnesses)
    ):
        bg = background_template
        tg = target_templates[interaction][directness]
        bg = bg.format(A=a, B=b, interaction=interaction)
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
    df.to_csv("data/stimuli/convo_scenario.csv", index=False)

