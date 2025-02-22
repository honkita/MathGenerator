import random

def randomInt(zero = False):
    high = 8
    low = -8
    i = random.randrange(low, high + 1)
    return i if i != 0 or zero else randomInt()

def randomTrig():
    trig_functions = ["sin", "cos", "tan", "csc", "sec", "cot"]
    i = random.randrange(0, len(trig_functions))
    return trig_functions[i]

def randomK():
    sign = [ "", "-"]
    k = [
        "\\frac{\\pi}{6}x", 
        "\\frac{\\pi}{5}x",
        "\\frac{\\pi}{4}x", 
        "\\frac{\\pi}{3}x", 
        "\\frac{\\pi}{2}", 
        "\\pi x", 
        "\\frac{3\\pi}{2}x", 
        "2\\pi x", 
        "3\\pi x", 
        "4\\pi x",
        "x",
        "2x",
        "3x",
        "4x",
        "6x",
        "\\frac{x}{6}", 
        "\\frac{x}{5}",
        "\\frac{x}{4}", 
        "\\frac{x}{3}", 
        "\\frac{x}{2}"
    ]
    j = random.randrange(0, len(sign))
    i = random.randrange(0, len(k))
    return sign[j] + k[i]

def phaseShift():
    sign = [ " + ", " - "]
    k = [
        "\\frac{\\pi}{6}", 
        "\\frac{\\pi}{5}",
        "\\frac{\\pi}{4}", 
        "\\frac{\\pi}{3}", 
        "\\frac{\\pi}{2}", 
        "\\pi", 
        "\\frac{3\\pi}{2}", 
        "2\\pi", 
        "3\\pi", 
        "4\\pi",
        "1"
    ]
    j = random.randrange(0, len(sign))
    i = random.randrange(0, len(k))
    return sign[j] + k[i]

def main():
    questions = []
    for i in range(100):
        
        while True:
            a = randomInt()
            a_sign = "" if a >= 0 else "-" 
            trig = randomTrig()
            k = randomK()
            ps = phaseShift()
            c = randomInt(True)
            c_sign = " + " if c > 0 else (" - " if c < 0 else "")  
            
            current_question = [a, trig, k, ps, c]
            if current_question not in questions:
                questions.append(current_question)
                print(str(i + 1) + ". \\(f(x) = " + 
                      a_sign + str(abs(a) if abs(a) != 1 else "") + 
                      "\\" + trig + "(" + 
                      k + ps +
                      ")" + 
                      c_sign + str(abs(c) if abs(c) != 0 else "") + 
                    "\\) \\\\")
                break
        
        
        

main()