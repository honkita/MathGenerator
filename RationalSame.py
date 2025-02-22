from RandomNumber import randomInt
from Question import Question

class RationalSame(Question):
    def name():
        return "Rational Functions (Same Degree)"

    def description():
        return "Sketch the graphs and determine the asymptotes, the holes, the domain, and the range."
    
    def generator(num_questions, low = -8, high = 8):
        questions = []
        printed_str = ""
        for i in range(num_questions):
            # variables for the numerator
            n_a, n_b, n_c = 0, 0, 0
            # variables for the denominator
            d_a, d_b, d_c = 0, 0, 0
            
            while True:
                n_val1 = randomInt(low, high)
                n_val2 = randomInt(low, high)
                n_val3 = randomInt(low, high)
                n_val4 = randomInt(low, high)
                
                d_val1 = randomInt(low, high)
                d_val2 = randomInt(low, high)
                d_val3 = randomInt(low, high)
                d_val4 = randomInt(low, high)

            
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
                    printed_str = printed_str + "\t" + (str(i + 1) + ". \\(f(x) = \\frac {" + 
                        n_a_sign + str(abs(n_a) if abs(n_a) != 1 else "") + "x^2"  + 
                        n_b_sign + str(abs(n_b) if abs(n_b) != 1 and abs(n_b) != 0 else "") + 
                        ("x" if abs(n_b) != 0 else "") + 
                        n_c_sign + str(abs(n_c)) + 
                        "}" + "{" + 
                        d_a_sign + str(abs(d_a) if abs(d_a) != 1 else "") + "x^2"  + 
                        d_b_sign + str(abs(d_b) if abs(d_b) != 1 and abs(d_b) != 0 else "") + 
                        ("x" if abs(d_b) != 0 else "") + 
                        d_c_sign + str(abs(d_c)) + 
                        "}\\) \\\\\n")
                    break
        return printed_str