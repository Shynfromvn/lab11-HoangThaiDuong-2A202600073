# Day-11-Guardrails-HITL-Responsible-AI

Day 11 - Guardrails, HITL & Responsible AI: How to make agent applications safe?

## Objectives

- Understand why guardrails are mandatory for AI products
- Implement input guardrails (injection detection, topic filter)
- Implement output guardrails (content filter, LLM-as-Judge)
- Use NeMo Guardrails (NVIDIA) with Colang
- Design HITL workflow with confidence-based routing
- Perform basic red teaming

## Project Structure

```text
Day-11-Guardrails-HITL-Responsible-AI/
|-- notebooks/
|   |-- lab11_guardrails_hitl.ipynb
|   `-- lab11_guardrails_hitl_solution.ipynb
|-- src/
|   |-- main.py
|   |-- core/
|   |   |-- config.py
|   |   `-- utils.py
|   |-- agents/
|   |   `-- agent.py
|   |-- attacks/
|   |   `-- attacks.py
|   |-- guardrails/
|   |   |-- input_guardrails.py
|   |   |-- output_guardrails.py
|   |   `-- nemo_guardrails.py
|   |-- testing/
|   |   `-- testing.py
|   `-- hitl/
|       `-- hitl.py
|-- .env.example
|-- requirements.txt
`-- README.md
```

## Setup

### Environment

1. Copy `.env.example` to `.env`
2. Paste your `OPENAI_API_KEY` into `.env`
3. Optionally change `OPENAI_MODEL` if you want a different OpenAI model

### Local Notebook

```bash
pip install -r requirements.txt
jupyter notebook notebooks/lab11_guardrails_hitl.ipynb
```

### Local Python Modules

```bash
cd src/
pip install -r ../requirements.txt

python main.py
python main.py --part 1
python main.py --part 2
python main.py --part 3
python main.py --part 4
```

## Tools Used

- Google ADK - Agent Development Kit (plugins, runners)
- NeMo Guardrails - NVIDIA framework with Colang
- OpenAI models via LiteLLM - LLM backend for ADK and NeMo

## 13 TODOs

| # | Description | Framework |
|---|-------------|-----------|
| 1 | Write 5 adversarial prompts | - |
| 2 | Generate attack test cases with AI | OpenAI |
| 3 | Injection detection (regex) | Python |
| 4 | Topic filter | Python |
| 5 | Input Guardrail Plugin | Google ADK |
| 6 | Content filter (PII, secrets) | Python |
| 7 | LLM-as-Judge safety check | OpenAI |
| 8 | Output Guardrail Plugin | Google ADK |
| 9 | NeMo Guardrails Colang config | NeMo |
| 10 | Rerun 5 attacks with guardrails | Google ADK |
| 11 | Automated security testing pipeline | Python |
| 12 | Confidence Router (HITL) | Python |
| 13 | Design 3 HITL decision points | Design |

## References

- https://owasp.org/www-project-top-10-for-large-language-model-applications/
- https://github.com/NVIDIA/NeMo-Guardrails
- https://google.github.io/adk-docs/
- https://platform.openai.com/docs/overview
