# passwords generator

def generate_passwords():
    first_segment = ["first_1","first_2","first_3"]

    second_segment = ["second_1","second_2","second_3"]

    third_segment = ["third_1", "third_2"]

    fourth_segment = ["fourth_1","fourth_2"]

    # Generate all possible combinations
    for first in first_segment:
        for second in second_segment:
            for third in third_segment:
                for fourth in fourth_segment:
                    yield first + second + third + fourth

# Example usage
if __name__ == "__main__":
    passwords_gen = generate_passwords()
    for _ in range(10):
        password = next(passwords_gen)
        print(password)
