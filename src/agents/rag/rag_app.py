import os
from flask import Flask, request, jsonify
from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM
from rag_system import RetrievalSystem  # Assuming a custom module for RAG retrieval

# Initialize the Flask app
app = Flask(__name__)

# Load the pre-trained model and tokenizer for generation (e.g., a T5 model)
model_name = "t5-small"  # Example model, you can replace with your preferred model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

# Initialize the retrieval system (you need to implement your own RAG retrieval system)
retrieval_system = RetrievalSystem()

@app.route('/generate', methods=['POST'])
def generate_response():
    try:
        # Get input query from request
        data = request.get_json()
        query = data.get("query")

        if not query:
            return jsonify({"error": "No query provided"}), 400

        # Retrieve relevant documents based on the query
        retrieved_docs = retrieval_system.retrieve(query)

        # Combine the retrieved documents with the query for generation
        input_text = query + " " + " ".join(retrieved_docs)

        # Encode the input and generate a response
        inputs = tokenizer(input_text, return_tensors="pt", truncation=True, padding=True)
        outputs = model.generate(**inputs)
        response_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

        # Return the generated response
        return jsonify({"response": response_text})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "ok"}), 200

if __name__ == '__main__':
    # Run the app on port 8000
    app.run(host='0.0.0.0', port=8000)
