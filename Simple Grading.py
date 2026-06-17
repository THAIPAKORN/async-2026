import sys
def evaluate_grade(score):
    if score >= 80:
        return'Excellent'
    if 50 <= score < 80:
        return 'Pass'
    if score < 50:
        return 'Fail'

    pass

def main():
    test_score = int(input("Enter score: "))
    result = evaluate_grade(test_score)
    print(f"Score: {test_score} -> Grade: {result}")

if __name__ == "__main__":
    main()
