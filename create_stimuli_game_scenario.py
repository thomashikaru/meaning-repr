import pandas as pd
import numpy as np
from tqdm import tqdm
import itertools

if __name__ == "__main__":
    ### GAME SCENARIO ###
    background_template = "{A} and {B} are playing a game which requires them to score a goal while avoiding {items}. {A} is {interaction} {B} in this game."
    target_templates = {
        "helping": {
            "indirect": "{A} is removing the {items} from {B}'s way.",
            "direct": "{A} is making it easier for {B} to score goals.",
        },
        "hindering": {
            "indirect": "{A} is placing the {items} in {B}’s way.",
            "direct": "{A} is making it harder for {B} to score goals.",
        },
        "cooperating with": {
            "indirect": "{A} is removing the {items} from {B}’s way.",
            "direct": "{A} wants {B} to score goals.",
        },
        "competing with": {
            "indirect": "{A} is placing the {items} in {B}’s way.",
            "direct": "{A} does not want {B} to score goals.",
        },
        "evading": {
            "indirect": "{A} is running in the opposite direction from {B}. ",
            "direct": "{A} is trying to escape {B}.",
        },
        "chasing": {
            "indirect": "{A} is running in the direction of {B}.",
            "direct": "{A} is trying to catch {B}.",
        },
        "learning from": {
            "indirect": "{A} is getting better at the game by watching {B}.",
            "direct": "{B} is showing {A} how to play this game.",
        },
        "teaching": {
            "indirect": "{B} is getting better at the game by watching {A}.",
            "direct": "{A} is showing {B} how to play this game.",
        },
        "deceiving": {
            "indirect": "{A} is hiding the ball from {B} behind one of the {items}.",
            "direct": "{A} is tricking {B} in this game.",
        },
        "coercing": {
            "indirect": "{B} has to do what {A} wants although {B} doesn’t want to.",
            "direct": "{A} is forcing {B} to play the game.",
        },
        "imitating": {
            "indirect": "When {B} performs an action, {A} does the same thing.",
            "direct": "{A} is copying {B}’s actions.",
        },
    }

    items = ["obstacles", "blocks", "daxes"]
    interactions = target_templates.keys()
    namesA = ["Alice", "Andrew", "A"]
    namesB = ["Bob", "Beatrice", "B"]
    directnesses = ["indirect", "direct"]

    data = []

    for a, b, item, interaction, directness in tqdm(
        itertools.product(namesA, namesB, items, interactions, directnesses)
    ):
        bg = background_template
        tg = target_templates[interaction][directness]
        bg = bg.format(A=a, B=b, items=item, interaction=interaction)
        tg = tg.format(A=a, B=b, items=item)
        data.append(
            {
                "background": bg,
                "target": tg,
                "A": a,
                "B": b,
                "interaction": interaction,
                "item": item,
                "directness": directness,
            }
        )

    df = pd.DataFrame(data)
    df.to_csv("data/stimuli/game_scenario.csv", index=False)

