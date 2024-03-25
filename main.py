from transformers import pipeline

def generate_instructions(recipe_name):
    # Load the pipeline for text generation
    text_generator = pipeline("text-generation", model="gpt2")

    # Define prompt for instruction generation
    prompt = f"Get detailed step-by-step instructions for making {recipe_name}. Include all necessary steps from preparing ingredients to cooking the dish."

    # Generate instructions with added constraints
    instructions = text_generator(
        prompt,
        max_length=600,
        do_sample=True,
        temperature=0.7,
        repetition_penalty=1.2,
        truncation=True,
        num_return_sequences=1
    )[0]["generated_text"].strip()

    return instructions

def main():
    while True:
        print("Hello! Which recipe would you like to see today?")
        recipe_name = input("Enter the name of the recipe: ")

        instructions = generate_instructions(recipe_name)

        if "Sorry, detailed instructions for this recipe could not be found." in instructions:
            print(instructions)
        else:
            print(f"\nHow to make the {recipe_name}:")
            print(instructions)
            break

    while True:
        satisfaction = input("\nAre you satisfied with the provided details? (yes/no): ")
        if satisfaction.lower() == "yes":
            more_recipes = input("Do you want to check another recipe? (yes/no): ")
            if more_recipes.lower() == "yes":
                continue
            else:
                print("Thank you for using the recipe bot!")
                break
        elif satisfaction.lower() == "no":
            print("Okay, let's try a different approach.")
            main()
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    main()
