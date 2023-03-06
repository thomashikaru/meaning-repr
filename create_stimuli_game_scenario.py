import pandas as pd
import numpy as np
from tqdm import tqdm
import itertools
from utils import get_2x2, sort_colnames


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

    directnesses = ["indirect", "direct"]
    subjects = ["Alice", "Bob", "Charlie", "Barack Obama", "Donald Trump", "Mom", "Dad"]
    subject_combos = list(itertools.combinations(subjects, 2))
    objects = ["obstacles", "objects", "blocks", "cubes", "spikes", "daxes", "blickets"]
    data = []

    # the set of concept pairs
    interaction_pairs = [
        ("helping", "hindering"),
        ("cooperating with", "competing with"),
        ("evading", "chasing"),
        ("learning from", "teaching"),
    ]

    for (interaction1, interaction2) in interaction_pairs:
        print(f"{interaction1}_{interaction2}")
        for i, (directness, (sub1, sub2), object) in enumerate(
            itertools.product(directnesses, subject_combos, objects)
        ):
            data.extend(
                get_2x2(
                    background_template.format(
                        A=sub1, B=sub2, items=object, interaction=interaction1
                    ),
                    background_template.format(
                        A=sub1, B=sub2, items=object, interaction=interaction2
                    ),
                    target_templates[interaction1][directness].format(
                        A=sub1, B=sub2, items=object
                    ),
                    target_templates[interaction2][directness].format(
                        A=sub1, B=sub2, items=object
                    ),
                    subject1=sub1,
                    subject2=sub2,
                    object1=object,
                    directness=directness,
                    item=i,
                    stim_classname=f"{interaction1}_{interaction2}",
                )
            )

    df = pd.DataFrame(data)
    df = sort_colnames(df)
    df.to_csv("data/stimuli/game_scenario.csv", index=False)

