from RandomNumber import randomInt
from Question import Question

class Quadratic(Question):
    def name():
        return "Quadratics"

    def description():
        return "Factor without using the quadratic formula."
    
    def generator(num_questions, low = -8, high = 8):
        questions = []
        printed_str = ""
        for i in range(num_questions):
            a, b, c = 0, 0, 0
            
            while True:
                val1 = randomInt(low, high)
                val2 = randomInt(low, high)
                val3 = randomInt(low, high)
                val4 = randomInt(low, high)


                a = val1 * val2
                a_sign = "" if a > 0 else "-" 
                b = val1 * val3 + val2 * val4
                b_sign = " + " if b > 0 else " - " 
                c = val3 * val4
                c_sign = " + " if c > 0 else " - " 
                current_question = [a, b, c]
                if current_question not in questions:
                    questions.append(current_question)
                    middle = ""
                    if b != 0:
                        middle = b_sign + str(abs(b) if abs(b) != 1 else "") + "x"
                    printed_str = printed_str + "\t" + str(i + 1) + ". \\( " + a_sign + str(abs(a) if abs(a) != 1 else "") + "x^2" +  middle + c_sign + str(abs(c)) + " \\) \\\\\n"
                    break
            
        return printed_str
