# test_phi2.py
from transformers import AutoModelForCausalLM, AutoTokenizer

phi2_model_name = "microsoft/phi-2"

try:
    phi2_tokenizer = AutoTokenizer.from_pretrained(phi2_model_name, trust_remote_code=True)
    phi2_model = AutoModelForCausalLM.from_pretrained(phi2_model_name, trust_remote_code=True)
    print(f"Phi-2 model and tokenizer loaded successfully from: {phi2_model_name}")

    # You can even try a quick generation
    input_text = "Write a short poem about a cat."
    input_ids = phi2_tokenizer.encode(input_text, return_tensors="pt")
    output = phi2_model.generate(input_ids, max_length=50, num_return_sequences=1)
    poem = phi2_tokenizer.decode(output[0], skip_special_tokens=True)
    print(f"Generated poem:\n{poem}")

except Exception as e:
    print(f"Error loading Phi-2: {e}")
    print("Make sure you have internet access for the initial download and sufficient disk space.")