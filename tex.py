"""
Imports for all different types of questions
"""
import Question
from Quadratic import Quadratic
from RationalLowerNumerator import RationalLowerNumerator
from RationalSame import RationalSame
from Trig import Trig

beginning = """
\\documentclass{article}
"""

beginning_commands = """
\\renewcommand{\\familydefault}{\\sfdefault}
\\newcommand{\\ord}{\\operatorname{ord}} %% for ordinals
\\setlength{\\parindent}{0pt}
% Used to disable overfill notifications for hbox
\\begin{document}
"""

beginning_multicols = """
    \\begin{multicols*}{2}
    \\baselineskip=8\\baselineskip
    \\hfuzz=20pt 
    % Used to disable centering problems
    \\hbadness = 10000
"""

ending_multicols = """
    \\end{multicols*}
"""

ending = """
\\end{document}
"""

normal_packages = [
    "amsmath", 
    "diagbox", 
    "upgreek", 
    "spverbatim", 
    "multicol", 
    "listings", 
    "color"
    ]

prefix_packages = [
    ("makeroom", "cancel"), 
    ("a4paper, portrait, margin=0.5in", "geometry"),
    ("sfdefault,lf", "carlito")
    ]

def use_package(package: str, prefix = ""):
    return "\\usepackage" + ("" if prefix == "" else "[" + prefix + "]") + "{" + package + "}\n"

def module_parser(module: Question, question_count = 100):
    return "\\section*{"+ module.name()+ "}\n" + module.description() + beginning_multicols + module.generator(question_count) + ending_multicols
    
module_parser(Quadratic)

filename = "Output.tex"
folder = "./files/"

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
        module_parser(Quadratic) + 
        module_parser(RationalLowerNumerator) +
        module_parser(RationalSame) +
        module_parser(Trig) +
        ending)