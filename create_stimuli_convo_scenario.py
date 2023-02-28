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

    # respecting/insulting
    context1 = "{A} and {B} are sitting at a table having a conversation. {A} is respecting {B}."
    target1 = target_templates["respecting"]
    context2 = "{A} and {B} are sitting at a table having a conversation. {A} is insulting {B}."
    target2 = target_templates["insulting"]

    for directness, (sub1, sub2) in tqdm(
        itertools.product(directnesses, subject_combos)
    ):
        data.extend(
            get_2x2(
                context1.format(A=sub1, B=sub2),
                context2.format(A=sub1, B=sub2),
                target1[directness].format(A=sub1, B=sub2),
                target2[directness].format(A=sub1, B=sub2),
                subject1=sub1,
                subject2=sub2,
                directness=directness,
                stim_classname="respecting_insulting",
            )
        )

    # teasing/comforting
    context1 = (
        "{A} and {B} are sitting at a table having a conversation. {A} is teasing {B}."
    )
    target1 = target_templates["teasing"]
    context2 = "{A} and {B} are sitting at a table having a conversation. {A} is comforting {B}."
    target2 = target_templates["comforting"]

    for directness, (sub1, sub2) in tqdm(
        itertools.product(directnesses, subject_combos)
    ):
        data.extend(
            get_2x2(
                context1.format(A=sub1, B=sub2),
                context2.format(A=sub1, B=sub2),
                target1[directness].format(A=sub1, B=sub2),
                target2[directness].format(A=sub1, B=sub2),
                subject1=sub1,
                subject2=sub2,
                directness=directness,
                stim_classname="teasing_comforting",
            )
        )

    # flirting with/envying
    context1 = "{A} and {B} are sitting at a table having a conversation. {A} is flirting with {B}."
    target1 = target_templates["flirting with"]
    context2 = (
        "{A} and {B} are sitting at a table having a conversation. {A} is envying {B}."
    )
    target2 = target_templates["envying"]

    for directness, (sub1, sub2) in tqdm(
        itertools.product(directnesses, subject_combos)
    ):
        data.extend(
            get_2x2(
                context1.format(A=sub1, B=sub2),
                context2.format(A=sub1, B=sub2),
                target1[directness].format(A=sub1, B=sub2),
                target2[directness].format(A=sub1, B=sub2),
                subject1=sub1,
                subject2=sub2,
                directness=directness,
                stim_classname="flirting_envying",
            )
        )

    df = pd.DataFrame(data)
    df.to_csv("data/stimuli/convo_scenario.csv", index=False)

