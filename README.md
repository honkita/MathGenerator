[![](https://raw.githubusercontent.com/honkita/MD-Links/main/Pixel_GitHub.svg)](https://github.com/honkita) [![](https://raw.githubusercontent.com/honkita/MD-Links/main/Pixel_Link.svg)](https://elitelu.com) [![](https://raw.githubusercontent.com/honkita/MD-Links/main/Pixel_LinkedIn.svg)](https://www.linkedin.com/in/elitelu/)

# MathGen

![](https://raw.githubusercontent.com/honkita/MD-Links/main/Pixel_Maintained.svg)

## About

This application generates a Latex file with randomly generated questions, which varies from Quadratic factoring and Rational function questions.

## Prerequisites to Run

To run this, you will need the following:

- Python 3 (Developed using Python 3.9.13)
- Latex distribution (Recommended to also use PDFLatex since it allows for convinient PDF generation)

## Types of Questions

All the question files use **Question** as an Interface. This means that each question class must have the following:

| Function                                     | Description                                                                                                                                 |
| -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| name()                                       | Returns the name of the question type                                                                                                       |
| description()                                | Returns the description of what to do for the question                                                                                      |
| generator(num_questions, low = -8, high = 8) | Generates **#num_questions** questions. **low** and **high** are the values for the random number generation and is not mandatory to enter. |

With these functions, here are each of the question types currently implemented:

| File                    | About                                                                                                     | What to do                                                                                                                                                   |
| ----------------------- | --------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Quadratic​              | Quadratic factoring questions in the form $ax^2+bx+c$. Does not require the use of the quadratic formula. | Factor the questions and find the roots **without** using the quadratic formula                                                                              |
| RationalSame            | Rational functions in the form $\frac{dx^2+ex+f}{ax^2+bx+c}$.                                             | Determine the asymptotes (vertical and horizontal), x-intercept, y-intercept, behaviours (end and asymptotic), holes, along with a sketch with a few points. |
| RationalLowerNumerator​ | Rational functions in the form $\frac{mx+d}{ax^2+bx+c}$.                                                  | Determine the asymptotes (vertical and horizontal), y-intercept, behaviours (end and asymptotic), holes, along with a sketch with a few points.              |
| Trig                    | Trigonometry functions with $\sin$, $\cos$, $\tan$, $\csc$, $\sec$, and $\cot$.                           | Determine the amplitude, peak (max), trough (min), period and phase shift. Graph afterwards.                                                                 |
