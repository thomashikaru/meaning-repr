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
    ### NON PHYSICAL PROPERTIES SCENARIO ###
    data = []

    # value (financial)
    context1 = "At the store {A} wanted to buy either {obj1} or {obj2}, but only had enough money to buy {obj1}."
    target1 = "{obj2} costs more than {obj1}."
    context2 = "At the store {A} wanted to buy either {obj1} or {obj2}, but only had enough money to buy {obj2}."
    target2 = "{obj1} costs more than {obj2}."

    subjects = ["Alice", "Bob", "Charlie", "Barack Obama", "Donald Trump", "Mom", "Dad"]
    objects = ["an apple", "an orange", "a pineapple", "a dax", "a blicket"]
    object_combos = itertools.combinations(objects, 2)

    for subject, (obj1, obj2) in tqdm(itertools.product(subjects, object_combos)):
        data.extend(
            get_2x2(
                context1.format(A=subject, obj1=obj1, obj2=obj2),
                context2.format(A=subject, obj1=obj1, obj2=obj2),
                target1.format(A=subject, obj1=obj1, obj2=obj2),
                target2.format(A=subject, obj1=obj1, obj2=obj2),
                subject1=subject,
                object1=obj1,
                object2=obj2,
                stim_classname="value_financial",
            )
        )

    # value (subjective)
    context1 = (
        "{B} gave {A} a choice of gifts between {obj1} or {obj2}. {A} picked {obj1}."
    )
    target1 = "{A} valued {obj1} more than {obj2}."
    context2 = (
        "{B} gave {A} a choice of gifts between {obj1} or {obj2}. {A} picked {obj2}."
    )
    target2 = "{A} valued {obj2} more than {obj1}."

    subjects = ["Alice", "Barack Obama", "Donald Trump", "Mom", "Dad"]
    objects = ["a thermos", "a mug", "a watch", "a dax", "a blicket"]
    subject_combos = itertools.combinations(subjects, 2)
    object_combos = itertools.combinations(objects, 2)

    for (sub1, sub2), (obj1, obj2) in tqdm(
        itertools.product(subject_combos, object_combos)
    ):
        data.extend(
            get_2x2(
                context1.format(A=sub1, B=sub2, obj1=obj1, obj2=obj2),
                context2.format(A=sub1, B=sub2, obj1=obj1, obj2=obj2),
                target1.format(A=sub1, B=sub2, obj1=obj1, obj2=obj2),
                target2.format(A=sub1, B=sub2, obj1=obj1, obj2=obj2),
                subject1=sub1,
                subject2=sub2,
                object1=obj1,
                object2=obj2,
                stim_classname="value_subjective",
            )
        )

    # ownership
    context1 = "{A} has the right to sell {obj1}."
    target1 = "{A} owns {obj1}"
    context2 = "{A} has the right to buy {obj1}."
    target2 = "{A} doesn't own {obj1}."

    subjects = ["Alice", "Barack Obama", "Donald Trump", "Mom", "Dad"]
    objects = ["the car", "the house", "the computer", "the dax", "the blicket"]

    for subject, object in tqdm(itertools.product(subjects, objects)):
        data.extend(
            get_2x2(
                context1.format(A=subject, obj1=object),
                context2.format(A=subject, obj1=object),
                target1.format(A=subject, obj1=object),
                target2.format(A=subject, obj1=object),
                subject1=subject,
                object1=object,
                stim_classname="ownership",
            )
        )

    # age of house
    context1 = "{A} lived in the {obj1} house when the {obj2} house was being built."
    target1 = "The {obj1} house is older than the {obj2} house."
    context2 = "{A} lived in the {obj2} house when the {obj1} house was being built."
    target2 = "The {obj2} house is older than the {obj1} house."

    subjects = ["Alice", "Barack Obama", "Donald Trump", "Mom", "Dad"]
    objects = ["wooden", "brick", "thatched", "stone", "terracotta"]
    object_combos = itertools.combinations(objects, 2)

    for subject, (obj1, obj2) in tqdm(itertools.product(subjects, object_combos)):
        data.extend(
            get_2x2(
                context1.format(A=subject, obj1=obj1, obj2=obj2),
                context2.format(A=subject, obj1=obj1, obj2=obj2),
                target1.format(A=subject, obj1=obj1, obj2=obj2),
                target2.format(A=subject, obj1=obj1, obj2=obj2),
                subject1=subject,
                object1=obj1,
                object2=obj2,
                stim_classname="age_of_house",
            )
        )

    # save dataframe to CSV
    df = pd.DataFrame(data)
    df.to_csv("data/stimuli/nonphysical_properties.csv", index=False)

