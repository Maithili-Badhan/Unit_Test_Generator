# 📘 AI-Powered Unit Test Generator for C++ Projects

This project builds a unit test generator for C++ applications using a local LLM (via [Ollama](https://ollama.com)). It uses the [`orgChartApi`](https://github.com/keploy/orgChartApi) C++ project as a case study.

The tool:

* Parses all `.cc` and `.h` files in a target C++ project
* Sends them to a local LLM (e.g. LLaMA, CodeLlama, Mistral via Ollama)
* Automatically generates initial Google Test unit test cases
* Optionally iterates to refine and improve the test quality
* Integrates with GNU compiler to build and validate the tests

---

## 📁 Project Structure

```
UNIT_TEST_GENERATOR/
│
├── src/                 # Source code (cloned C++ project here)
│   └── orgChartApi/     # Target repo for which tests will be generated
│
├── tests/               # Output folder for generated test files
│   └── test_main.cpp
│
├── prompts/             # YAML-style prompt templates for LLM
│   └── gen_test.yaml
│
├── logs/                # Logs from test failures or builds
│   └── output.txt
│
├── run.py               # Python script to automate LLM-driven test generation
├── README.md            # Project documentation
```

---

## 🚀 How It Works

1. Clone a C++ project (like `orgChartApi`) into the `src/` directory.
2. Write a structured YAML prompt in `prompts/` with instructions for the LLM.
3. Run `run.py` to:

   * Read `.cc` and `.h` files
   * Format a prompt using YAML
   * Send it to a local LLM via Ollama
   * Save the response into `tests/test_main.cpp`
4. Compile the project with Google Test and run the generated tests.

---

## ⚙️ Setup Instructions

### ✅ Prerequisites

* Python 3.8+
* Ollama (download from [https://ollama.com/](https://ollama.com/))
* Google Test (installed system-wide or compiled locally)
* g++ or clang (with pthread support)

### 🔧 Install Python dependencies

```bash
pip install requests
```

### 🧙‍♂️ Run Ollama locally

```bash
ollama run codellama
```

Or use `mistral`, `llama3`, etc.

---

## 🧪 Example Usage

### Step 1: Clone the target repo

```bash
cd src
git clone https://github.com/keploy/orgChartApi.git
cd ..
```

### Step 2: Create a prompt

**`prompts/gen_test.yaml`**

```yaml
instructions:
  - Generate unit tests using Google Test
  - Focus on edge cases and logical paths
  - Include all relevant #includes
  - Do not duplicate tests
  - Use TEST macros correctly
```

### Step 3: Run the generator

```bash
python run.py
```

You’ll get test files inside `tests/`.

---

## 💡 Build & Run the Tests

### Sample Compilation Command (Windows example):

```powershell
g++ -std=c++17 -I"C:\Program Files\googletest\include" `
    src/orgChartApi/main.cc tests/test_main.cpp `
    -o runTests.exe -lgtest -lgtest_main -pthread
```

### Then run:

```bash
./runTests
```

---

## 📈 Future Enhancements

* Iterative test refinement based on build logs
* Coverage integration with `gcov` or `llvm-cov`
* Dockerized version for platform-independent setup
* GUI or VSCode extension for inline test generation

---

## 🧠 Credits

* Project inspired by real-world C++ AI-assisted dev tools
* Built on [Ollama](https://ollama.com), Google Test, and the [`orgChartApi`](https://github.com/keploy/orgChartApi) repo.

---

## 📜 License

This tool is for educational purposes only. Please ensure you comply with the licenses of any external repos you test on.
