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

    data = []

    # helping/hindering
    context1 = "{A} and {B} are playing a game which requires them to score a goal while avoiding {items}. {A} is helping {B} in this game."
    target1 = target_templates["helping"]
    context2 = "{A} and {B} are playing a game which requires them to score a goal while avoiding {items}. {A} is hindering {B} in this game."
    target2 = target_templates["hindering"]

    subjects = ["Alice", "Bob", "Charlie", "Barack Obama", "Donald Trump", "Mom", "Dad"]
    objects = ["obstacles", "objects", "blocks", "cubes", "spikes", "daxes", "blickets"]
    subject_combos = itertools.combinations(subjects, 2)

    for directness, (sub1, sub2), object in tqdm(
        itertools.product(directnesses, subject_combos, objects)
    ):
        data.extend(
            get_2x2(
                context1.format(A=sub1, B=sub2, items=object),
                context2.format(A=sub1, B=sub2, items=object),
                target1[directness].format(A=sub1, B=sub2, items=object),
                target2[directness].format(A=sub1, B=sub2, items=object),
                subject1=sub1,
                subject2=sub2,
                object1=object,
                directness=directness,
                stim_classname="helping_hindering",
            )
        )

    # cooperating with/competing with
    context1 = "{A} and {B} are playing a game which requires them to score a goal while avoiding {items}. {A} is cooperating with {B} in this game."
    target1 = target_templates["cooperating with"]
    context2 = "{A} and {B} are playing a game which requires them to score a goal while avoiding {items}. {A} is competing with {B} in this game."
    target2 = target_templates["competing with"]

    subjects = ["Alice", "Bob", "Charlie", "Barack Obama", "Donald Trump", "Mom", "Dad"]
    objects = ["obstacles", "objects", "blocks", "cubes", "spikes", "daxes", "blickets"]
    subject_combos = itertools.combinations(subjects, 2)

    for directness, (sub1, sub2), object in tqdm(
        itertools.product(directnesses, subject_combos, objects)
    ):
        data.extend(
            get_2x2(
                context1.format(A=sub1, B=sub2, items=object),
                context2.format(A=sub1, B=sub2, items=object),
                target1[directness].format(A=sub1, B=sub2, items=object),
                target2[directness].format(A=sub1, B=sub2, items=object),
                subject1=sub1,
                subject2=sub2,
                object1=object,
                directness=directness,
                stim_classname="cooperating_competing",
            )
        )

    # evading/chasing
    context1 = "{A} and {B} are playing a game which requires them to score a goal while avoiding {items}. {A} is evading {B} in this game."
    target1 = target_templates["evading"]
    context2 = "{A} and {B} are playing a game which requires them to score a goal while avoiding {items}. {A} is chasing {B} in this game."
    target2 = target_templates["chasing"]

    subjects = ["Alice", "Bob", "Charlie", "Barack Obama", "Donald Trump", "Mom", "Dad"]
    objects = ["obstacles", "objects", "blocks", "cubes", "spikes", "daxes", "blickets"]
    subject_combos = itertools.combinations(subjects, 2)

    for directness, (sub1, sub2), object in tqdm(
        itertools.product(directnesses, subject_combos, objects)
    ):
        data.extend(
            get_2x2(
                context1.format(A=sub1, B=sub2, items=object),
                context2.format(A=sub1, B=sub2, items=object),
                target1[directness].format(A=sub1, B=sub2, items=object),
                target2[directness].format(A=sub1, B=sub2, items=object),
                subject1=sub1,
                subject2=sub2,
                object1=object,
                directness=directness,
                stim_classname="evading_chasing",
            )
        )

    # learning from/teaching
    context1 = "{A} and {B} are playing a game which requires them to score a goal while avoiding {items}. {A} is learning from {B} in this game."
    target1 = target_templates["learning from"]
    context2 = "{A} and {B} are playing a game which requires them to score a goal while avoiding {items}. {A} is teaching {B} in this game."
    target2 = target_templates["teaching"]

    subjects = ["Alice", "Bob", "Charlie", "Barack Obama", "Donald Trump", "Mom", "Dad"]
    objects = ["obstacles", "objects", "blocks", "cubes", "spikes", "daxes", "blickets"]
    subject_combos = itertools.combinations(subjects, 2)

    for directness, (sub1, sub2), object in tqdm(
        itertools.product(directnesses, subject_combos, objects)
    ):
        data.extend(
            get_2x2(
                context1.format(A=sub1, B=sub2, items=object),
                context2.format(A=sub1, B=sub2, items=object),
                target1[directness].format(A=sub1, B=sub2, items=object),
                target2[directness].format(A=sub1, B=sub2, items=object),
                subject1=sub1,
                subject2=sub2,
                object1=object,
                directness=directness,
                stim_classname="learning_teaching",
            )
        )

    df = pd.DataFrame(data)
    df.to_csv("data/stimuli/game_scenario.csv", index=False)

