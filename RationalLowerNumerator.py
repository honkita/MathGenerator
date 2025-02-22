import random

def randomInt(zero = False):
    high = 8
    low = -8
    i = random.randrange(low, high + 1)
    return i if i != 0 or zero else randomInt()

def main():
    questions = []
    for i in range(100):
        # variables for the numerator
        n_m, n_b = 0, 0
        # variables for the denominator
        d_a, d_b, d_c = 0, 0, 0
        
        while True:
            d_val1 = randomInt()
            d_val2 = randomInt()
            d_val3 = randomInt()
            d_val4 = randomInt()

           
            n_m = randomInt(True)
            n_m_sign = "" if n_m >= 0 else "-" 
            n_b = randomInt(True)
            n_b_sign = " + " if n_b > 0 else (" - " if n_b != 0 else "") 

            d_a = d_val1 * d_val2
            d_a_sign = "" if d_a >= 0 else "-" 
            d_b = d_val1 * d_val3 + d_val2 * d_val4
            d_b_sign = " + " if d_b > 0 else (" - " if d_b != 0 else "") 
            d_c = d_val3 * d_val4
            d_c_sign = " + " if d_c > 0 else " - " 
            current_question = [n_m, n_b, d_a, d_b, d_c]
            if current_question not in questions and n_m != 0 and n_b != 0:
                questions.append(current_question)
                print(str(i + 1) + ". \\(f(x) = \\frac {" + 
                    n_m_sign + str(abs(n_m) if abs(n_m) != 1 else "") + "x" + 
                    n_b_sign + str(abs(n_b)) + 
                    "}" + "{" + 
                    d_a_sign + str(abs(d_a) if abs(d_a) != 1 else "") + "x^2"  + 
                    d_b_sign + str(abs(d_b) if abs(d_b) != 1 and abs(d_b) != 0 else "") + 
                    ("x" if abs(d_b) != 0 else "") + 
                    d_c_sign + str(abs(d_c)) + 
                    "}\\) \\\\")
                break
        
        
        

main()