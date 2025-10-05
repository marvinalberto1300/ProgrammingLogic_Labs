import re

def analyze_feedback(feedback):
    print("\n--- Analysis Results ---\n")

    # Original Feedback
    print(f"Original Feedback: {feedback}")
    
    # Trim and lowercase
    trimmed = feedback.strip()
    lowered = trimmed.lower()
    print(f"\nTrimmed & Lowercased Feedback: {lowered}")
    
    # Keyword counts
    refund_count = lowered.count("refund")
    replacement_count = lowered.count("replacement")
    print(f"\nKeyword 'refund': {refund_count}")
    print(f"Keyword 'replacement': {replacement_count}")
    
    # Replace ASAP
    updated = lowered.replace("asap", "as soon as possible")
    print(f"\nUpdated Feedback: {updated}")
    
    # First sentence
    first_sentence = trimmed.split(".")[0]
    print(f"\nFirst Sentence: {first_sentence}")
    
    # Gratitude check
    if "thank you" in lowered or "thanks" in lowered:
        print("\nCustomer expressed gratitude!")
    else:
        print("\nNo gratitude detected.")
    
   # Advanced Analysis
    print("\n--- Advanced Analysis ---\n")
    sentences = re.split(r'(?<=[.!?]) +', trimmed)

    for i, sentence in enumerate(sentences):
        # Find all capitalized words (3+ letters)
        emphasized_words = re.findall(r'\b[A-Z]{3,}\b', sentence)
    
        # Check for 'ASAP' explicitly (even if lowercase later)
        if "ASAP" in sentence:
            print("'ASAP' found in:", sentence)
            if i + 1 < len(sentences):
                print(f"     Following sentence: {sentences[i + 1]}")
    
        # Print each emphasized word separately
        for word in emphasized_words:
            if word != "ASAP":
                print(f"'{word}' found in: {sentence}")
                if i + 1 < len(sentences):
                    print(f"     Following sentence: {sentences[i + 1]}")
    
        # Check for exclamation mark
        if '!' in sentence:
            print("'!' found in:", sentence)
            if i + 1 < len(sentences):
                print(f"     Following sentence: {sentences[i + 1]}")
    
    # Word count
    word_count = len(trimmed.split())
    print(f"\nWord count: {word_count}")
    
def extract_questions_from_file(input_file, output_file):
    questions = []
    total_feedbacks = 0
    try:
        with open(input_file, "r") as f:
            lines = f.readlines()

        for line in lines:
            if "||" not in line:
                continue
            total_feedbacks += 1
            name, feedback = line.strip().split("||")
            sentences = re.split(r'(?<=[.!?]) +', feedback.strip())

            for sentence in sentences:
                if "?" in sentence:
                    question = sentence.strip()
                    questions.append((name.strip(), question))
        with open(output_file, "w") as report:
            report.write("**************************************\n")
            report.write("** Report of Questions by Customers **\n")
            report.write("**************************************\n")
            for i, (name, question) in enumerate(questions, start=1):
                report.write(f"{i}) {name} asked: {question}\n")
            report.write("------------------------------------------------------\n")
            report.write(f"No. of Feedbacks Processed: {total_feedbacks}\n")
            report.write(f"No. of Extracted Questions: {len(questions)}\n")
            report.write("*************************************\n")   
        print(f"\n✅ Report successfully generated in '{output_file}'.")
            # Show the report in the console
        with open(output_file, "r") as report:
            print(report.read())

    except FileNotFoundError:
        print(f"❌ Error: File '{input_file}' not found.")    

def main():
    # Optional: Run file-based question extraction
    run_file_extraction = input("\nWould you like to generate a question report from file? (y/n): ").lower()
    if run_file_extraction == 'y':
        extract_questions_from_file("customer_feedback.txt", "questions_report.txt")
        
    print("*******************************************")
    print("** WELCOME TO CUSTOMER FEEDBACK ANALYZER **")
    print("*******************************************")
    
    while True:
        feedback = input("\nPlease paste customer feedback message here: ")
        analyze_feedback(feedback)
        
        cont = input("\nWould you like to analyze more reviews (Type 'y' to continue or 'n' to exit)?: ").lower()
        if cont != 'y':
            print("\nThank you for using the Customer Feedback Analyzer. Goodbye!")
            break

if __name__ == "__main__":
        main()

input("\nPress Enter to exit...")

