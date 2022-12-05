import numpy as np

def parse_sections(sections):
    sections = [int(num) for num in sections.split('-')]
    return sections

def section_to_range(section):
    return range(section[0], section[1]+1)

def assignment_is_subset(assignment):
    first = assignment[0]
    second = assignment[1]
    return section_subset(first, second) or section_subset(second, first)

def section_subset(section1, section2):
    return section2[0] >= section1[0] and section2[1] <= section1[1]

def assignment_get_overlap(assignment):
    section1 = assignment[0]
    section2 = assignment[1]
    range1 = section_to_range(section1)
    range2 = section_to_range(section2)
    return set(range1).intersection(range2)

with open("input.txt", 'r') as file:
    content = file.read().strip()
    assignments = content.split('\n')
    assignments = [[parse_sections(sections) for sections in assignment.split(',')] for assignment in assignments]

    is_subset = [assignment_is_subset(assignment) for assignment in assignments]

    print("Number of assignments with subset sections:", len([a for a in is_subset if a]))

    overlaps = [assignment_get_overlap(assignment) for assignment in assignments]
    print(overlaps)

    print("Number of assignments with overlap:", len([a for a in overlaps if a]))