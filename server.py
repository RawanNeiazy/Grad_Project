from flask import Flask, request, jsonify
from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer

app = Flask(__name__)

model_name = 'NouranG/Llama-2-7b-humaneval-finetune'

# Load the tokenizer and model once at the start
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

pipe = pipeline(task="text-generation", model=model, tokenizer=tokenizer, max_length=1000)

def generate_test_cases(code):
    functions = [block.strip() for block in code.split("def") if block.strip()]
    test_cases = ""

    for i, function_code in enumerate(functions, start=1):
        prompt = f"""Your task is to generate unit test cases for the following function code: {function_code} and doing the following:
                 1. Explain the purpose of the function briefly.
                 2. Write unit tests to cover various scenarios, including edge cases.
                 3. Include assertions to verify the correctness of the function.
                 4. Handle any potential errors or exceptions gracefully.
"""
        result = pipe(f"<s>[INST] {prompt} [/INST]")
        generated_text = result[0]['generated_text']
        test_cases += f"\nGenerated test cases for Function {i}:\n{generated_text}\n"
    return test_cases

@app.route('/generate-test-cases', methods=['POST'])
def generate_test_cases_route():
    data = request.json
    code = data.get('code')
    
    if not code:
        return jsonify({'error': 'Code is required'}), 400
    
    # Generate test cases using the provided code
    test_cases = generate_test_cases(code)
    
    return jsonify({
        'testCases': test_cases
    })

if __name__ == '__main__':
    app.run(debug=True)
