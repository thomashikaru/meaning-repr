import pandas as pd
import numpy as np
from tqdm import tqdm
import itertools
from utils import get_2x2, sort_colnames


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

    for i, (subject, (obj1, obj2)) in enumerate(
        itertools.product(subjects, object_combos)
    ):
        data.extend(
            get_2x2(
                context1.format(A=subject, obj1=obj1, obj2=obj2),
                context2.format(A=subject, obj1=obj1, obj2=obj2),
                target1.format(A=subject, obj1=obj1, obj2=obj2),
                target2.format(A=subject, obj1=obj1, obj2=obj2),
                subject1=subject,
                object1=obj1,
                object2=obj2,
                item=i,
                stim_classname="value_financial",
                directness="indirect",
            )
        )

    context1 = "At the store {A} looked at the price tags of {obj1} and {obj2}, and saw that the price on {obj1} was lower."
    target1 = "{obj2} costs more than {obj1}."
    context2 = "At the store {A} looked at the price tags of {obj1} and {obj2}, and saw that the price on {obj2} was lower."
    target2 = "{obj1} costs more than {obj2}."

    subjects = ["Alice", "Bob", "Charlie", "Barack Obama", "Donald Trump", "Mom", "Dad"]
    objects = ["an apple", "an orange", "a pineapple", "a dax", "a blicket"]
    object_combos = itertools.combinations(objects, 2)

    for i, (subject, (obj1, obj2)) in enumerate(
        itertools.product(subjects, object_combos)
    ):
        data.extend(
            get_2x2(
                context1.format(A=subject, obj1=obj1, obj2=obj2),
                context2.format(A=subject, obj1=obj1, obj2=obj2),
                target1.format(A=subject, obj1=obj1, obj2=obj2),
                target2.format(A=subject, obj1=obj1, obj2=obj2),
                subject1=subject,
                object1=obj1,
                object2=obj2,
                item=i,
                stim_classname="value_financial",
                directness="direct",
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

    for i, ((sub1, sub2), (obj1, obj2)) in enumerate(
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
                item=i,
                stim_classname="value_subjective",
                directness="indirect",
            )
        )

    context1 = "{B} asked {A} whether they {obj1} or {obj2} would make a better gift. {A} said 'I would prefer {obj1}'."
    target1 = "{A} valued {obj1} more than {obj2}."
    context2 = "{B} asked {A} whether they {obj1} or {obj2} would make a better gift. {A} said 'I would prefer {obj2}'."
    target2 = "{A} valued {obj2} more than {obj1}."

    subjects = ["Alice", "Barack Obama", "Donald Trump", "Mom", "Dad"]
    objects = ["a thermos", "a mug", "a watch", "a dax", "a blicket"]
    subject_combos = itertools.combinations(subjects, 2)
    object_combos = itertools.combinations(objects, 2)

    for i, ((sub1, sub2), (obj1, obj2)) in enumerate(
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
                item=i,
                stim_classname="value_subjective",
                directness="direct",
            )
        )

    # ownership
    context1 = "{A} tends to describe the {obj1} as 'my {obj1}'."
    target1 = "{A} owns the {obj1}"
    context2 = "{A} does not typically describe the {obj1} as 'my {obj1}'."
    target2 = "{A} doesn't own the {obj1}."

    subjects = ["Alice", "Barack Obama", "Donald Trump", "Mom", "Dad"]
    objects = ["car", "house", "computer", "dax", "blicket"]

    for i, (subject, object) in enumerate(itertools.product(subjects, objects)):
        data.extend(
            get_2x2(
                context1.format(A=subject, obj1=object),
                context2.format(A=subject, obj1=object),
                target1.format(A=subject, obj1=object),
                target2.format(A=subject, obj1=object),
                subject1=subject,
                object1=object,
                item=i,
                stim_classname="ownership",
                directness="indirect",
            )
        )

    context1 = "{A} has the right to sell the {obj1}."
    target1 = "{A} owns the {obj1}"
    context2 = "{A} has the right to buy the {obj1}."
    target2 = "{A} doesn't own the {obj1}."

    subjects = ["Alice", "Barack Obama", "Donald Trump", "Mom", "Dad"]
    objects = ["car", "house", "computer", "dax", "blicket"]

    for i, (subject, object) in enumerate(itertools.product(subjects, objects)):
        data.extend(
            get_2x2(
                context1.format(A=subject, obj1=object),
                context2.format(A=subject, obj1=object),
                target1.format(A=subject, obj1=object),
                target2.format(A=subject, obj1=object),
                subject1=subject,
                object1=object,
                item=i,
                stim_classname="ownership",
                directness="direct",
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

    for i, (subject, (obj1, obj2)) in enumerate(
        itertools.product(subjects, object_combos)
    ):
        data.extend(
            get_2x2(
                context1.format(A=subject, obj1=obj1, obj2=obj2),
                context2.format(A=subject, obj1=obj1, obj2=obj2),
                target1.format(A=subject, obj1=obj1, obj2=obj2),
                target2.format(A=subject, obj1=obj1, obj2=obj2),
                subject1=subject,
                object1=obj1,
                object2=obj2,
                item=i,
                stim_classname="age_of_house",
                directness="indirect",
            )
        )

    context1 = "{A} built the {obj1} house in {year} and then built the {obj2} house ten years later."
    target1 = "The {obj1} house is older than the {obj2} house."
    context2 = "{A} built the {obj2} house in {year} and then built the {obj1} house ten years later."
    target2 = "The {obj2} house is older than the {obj1} house."

    subjects = ["Alice", "Barack Obama", "Donald Trump", "Mom", "Dad"]
    objects = ["wooden", "brick", "thatched", "stone", "terracotta"]
    object_combos = itertools.combinations(objects, 2)
    years = [1275, 1875, 1975, 2015, 2075, 3075]

    for i, (subject, (obj1, obj2), year) in enumerate(
        itertools.product(subjects, object_combos, years)
    ):
        data.extend(
            get_2x2(
                context1.format(A=subject, obj1=obj1, obj2=obj2, year=year),
                context2.format(A=subject, obj1=obj1, obj2=obj2, year=year),
                target1.format(A=subject, obj1=obj1, obj2=obj2, year=year),
                target2.format(A=subject, obj1=obj1, obj2=obj2, year=year),
                subject1=subject,
                object1=obj1,
                object2=obj2,
                year=year,
                item=i,
                stim_classname="age_of_house",
                directness="direct",
            )
        )

    # save dataframe to CSV
    df = pd.DataFrame(data)
    df = sort_colnames(df)
    df.to_csv("data/nonphysical_properties/nonphysical_properties.csv", index=False)

