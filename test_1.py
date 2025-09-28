from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import pandas as pd

# 1. Prepare Training Data
# In a real scenario, this would be a much larger and more diverse dataset
# of secure and insecure code examples.
data = {
    'code': [
        "print('Hello')",
        "result = eval('2 + 2')",
        "import os; os.system('ls')",
        "def safe_function(): pass",
        "user_input = input(); exec(user_input)", # another insecure example
        "x = 10; y = 20; print(x + y)",
        "import subprocess; subprocess.run(['echo', 'hello'])" # Insecure if user input is passed
    ],
    'is_vulnerable': [
        0, # print('Hello') - not vulnerable
        1, # eval('2 + 2') - vulnerable
        1, # os.system('ls') - vulnerable
        0, # safe_function() - not vulnerable
        1, # exec(user_input) - vulnerable
        0, # print(x + y) - not vulnerable
        1  # subprocess.run - potentially vulnerable if arguments are not sanitized
    ]
}
df = pd.DataFrame(data)

# 2. Create and Train the ML Model
# Using a pipeline for text vectorization and classification
model = make_pipeline(TfidfVectorizer(), MultinomialNB())
model.fit(df['code'], df['is_vulnerable'])

# 3. Predict Vulnerabilities in New Code
new_code_snippets = [
    "safe_calculation = 10 * 5",
    "user_command = 'rm -rf /'; import os; os.system(user_command)",
    "print('Secure code here')"
]

predictions = model.predict(new_code_snippets)

# 4. Interpret Results
print("Vulnerability Assessment Results:")
for i, code_snippet in enumerate(new_code_snippets):
    status = "Vulnerable" if predictions[i] == 1 else "Not Vulnerable"
    print(f"Code: '{code_snippet}' -> Status: {status}")
