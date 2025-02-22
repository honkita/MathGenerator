from Quadratic import quadratic

beginning = """
\\documentclass{article}
"""

beginning_commands = """
\\renewcommand{\\familydefault}{\\sfdefault}
\\newcommand{\\ord}{\\operatorname{ord}} %% for ordinals
\\setlength{\\parindent}{0pt}
% Used to disable overfill notifications for hbox
\\begin{document}
\\begin{multicols*}{2}
    \\baselineskip=8\\baselineskip
    \\hfuzz=20pt 
    % Used to disable centering problems
    \\hbadness = 10000
"""

ending = """
\\end{multicols*}
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

def usePackage(package: str, prefix = ""):
    return "\\usepackage" + ("" if prefix == "" else "[" + prefix + "]") + "{" + package + "}\n"


with open("Output.tex", "w") as text_file:
    packages = ""
    for package in normal_packages:
        packages = packages + usePackage(package)
    for (prefix, package) in prefix_packages:
        packages = packages + usePackage(package, prefix)
    text_file.write(beginning + packages + beginning_commands + quadratic(100) + ending)