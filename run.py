import os
import requests
import json

SRC_DIR = "./src/orgChartApi"
PROMPT_PATH = "./prompts/gen_test.yaml"
TEST_OUTPUT = "./tests/test_main.cpp"
OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "codellama"

def read_prompt():
    with open(PROMPT_PATH, 'r') as f:
        return f.read()

def read_cpp_code():
    files = []
    for root, _, filenames in os.walk(SRC_DIR):
        for filename in filenames:
            if filename.endswith((".cc", ".h", ".hh")):  # include .cc, .h, .hh
                path = os.path.join(root, filename)
                try:
                    with open(path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        files.append((filename, content))
                except Exception as e:
                    print(f"Error reading {path}: {e}")
    return files


def call_ollama(prompt):
    payload = {
        "model": OLLAMA_MODEL,
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)
    if response.status_code == 200:
        return response.json()["response"]
    else:
        print("Error calling Ollama:", response.text)
        return ""

def generate_tests():
    instructions = read_prompt()
    code_files = read_cpp_code()

    with open(TEST_OUTPUT, "w", encoding="utf-8") as out:
        for filename, code in code_files:
            print(f"Generating tests for {filename}...")
            prompt = f"{instructions}\n\n---\nFilename: {filename}\n\n{code}"
            test_code = call_ollama(prompt)
            out.write(f"// Tests for {filename}\n")
            out.write(test_code + "\n\n")

if __name__ == "__main__":
    generate_tests()
    print("✅ Tests generated in tests/test_main.cpp")