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
        n_a, n_b, n_c = 0, 0, 0
        # variables for the denominator
        d_a, d_b, d_c = 0, 0, 0
        
        while True:
            n_val1 = randomInt()
            n_val2 = randomInt()
            n_val3 = randomInt()
            n_val4 = randomInt()
            
            d_val1 = randomInt()
            d_val2 = randomInt()
            d_val3 = randomInt()
            d_val4 = randomInt()

           
            n_a = n_val1 * n_val2
            n_a_sign = "" if n_a >= 0 else "-" 
            n_b = n_val1 * n_val3 + n_val2 * n_val4
            n_b_sign = " + " if n_b > 0 else (" - " if n_b != 0 else "") 
            n_c = n_val3 * n_val4
            n_c_sign = " + " if n_c > 0 else " - " 

            d_a = d_val1 * d_val2
            d_a_sign = "" if d_a >= 0 else "-" 
            d_b = d_val1 * d_val3 + d_val2 * d_val4
            d_b_sign = " + " if d_b > 0 else (" - " if d_b != 0 else "") 
            d_c = d_val3 * d_val4
            d_c_sign = " + " if d_c > 0 else " - " 
            
            current_question = [n_a, n_b, n_c, d_a, d_b, d_c]
            if current_question not in questions:
                questions.append(current_question)
                print(str(i + 1) + ". \\(f(x) = \\frac {" + 
                    n_a_sign + str(abs(n_a) if abs(n_a) != 1 else "") + "x^2"  + 
                    n_b_sign + str(abs(n_b) if abs(n_b) != 1 and abs(n_b) != 0 else "") + 
                    ("x" if abs(n_b) != 0 else "") + 
                    n_c_sign + str(abs(n_c)) + 
                    "}" + "{" + 
                    d_a_sign + str(abs(d_a) if abs(d_a) != 1 else "") + "x^2"  + 
                    d_b_sign + str(abs(d_b) if abs(d_b) != 1 and abs(d_b) != 0 else "") + 
                    ("x" if abs(d_b) != 0 else "") + 
                    d_c_sign + str(abs(d_c)) + 
                    "}\\) \\\\")
                break
        
        
        

main()