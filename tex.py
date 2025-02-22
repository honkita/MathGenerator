"""
Imports for all different types of questions
"""
import Question
from Quadratic import Quadratic
from RationalLowerNumerator import RationalLowerNumerator
from RationalSame import RationalSame
from Trig import Trig
from typing import final


## Modify this to add or remove types of questions or change the number of questions generated
questions = [
    (Quadratic, 100), 
    (RationalLowerNumerator, 100), 
    (RationalSame, 100),
    (Trig, 100)
    ]

## Do NOT modify any of the variables labeled with final. These are needed for Latex generation
filename : final = "Output.tex"
folder : final = "./files/"

beginning : final = """
\\documentclass{article}
"""

beginning_commands : final = """
\\renewcommand{\\familydefault}{\\sfdefault}
\\newcommand{\\ord}{\\operatorname{ord}} %% for ordinals
\\setlength{\\parindent}{0pt}
% Used to disable overfill notifications for hbox
\\begin{document}
"""

beginning_multicols : final = """
    \\begin{multicols*}{2}
    \\baselineskip=8\\baselineskip
    \\hfuzz=20pt 
    % Used to disable centering problems
    \\hbadness = 10000
"""

ending_multicols : final = """
    \\end{multicols*}
"""

ending : final = """
\\end{document}
"""

normal_packages : final = [
    "amsmath", 
    "diagbox", 
    "upgreek", 
    "spverbatim", 
    "multicol", 
    "listings", 
    "color"
    ]

prefix_packages : final = [
    ("makeroom", "cancel"), 
    ("a4paper, portrait, margin=0.5in", "geometry"),
    ("sfdefault,lf", "carlito")
    ]

def use_package(package: str, prefix = ""):
    return "\\usepackage" + ("" if prefix == "" else "[" + prefix + "]") + "{" + package + "}\n"

def module_parser(module: Question, question_count = 100):
    return "\\section*{"+ module.name()+ "}\n" + module.description() + beginning_multicols + module.generator(question_count) + ending_multicols
    


def question_generator():
    question_gen = ""
    for (question, num) in questions:
        question_gen = question_gen + module_parser(question, num)
    return question_gen
    
with open(folder + filename, "w") as text_file:
    packages = ""
    for package in normal_packages:
        packages = packages + use_package(package)
    for (prefix, package) in prefix_packages:
        packages = packages + use_package(package, prefix)
    text_file.write(
        beginning + 
        packages + 
        beginning_commands + 
        question_generator() +
        ending)