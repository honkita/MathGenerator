class Question:
    def name() -> str:
        """
        Returns the name of the module

        Returns:
            str: The name of the type of question.
        """
        pass

    def description() -> str:
        """
        Returns the description of the type of problem
        
        Returns:
            str: The description of what to do for the question
        """
        pass
    
    def generator(num_questions: int, low = -8, high = 8) -> str:
        """
        Generates questions of a specific question type

        Args:
            num_questions (int): Number of questions generated
            low (int, optional): _description_. Defaults to -8.
            high (int, optional): _description_. Defaults to 8.

        Returns:
            str: Latex string of questions
        """
        pass