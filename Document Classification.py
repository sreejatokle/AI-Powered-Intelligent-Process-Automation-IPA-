from transformers import pipeline

# Initialize the HuggingFace text classification pipeline
classifier = pipeline('zero-shot-classification')

# Sample extracted text (from OCR or other sources)
text = "Customer has requested a refund for the product."

# Define candidate labels for classification
labels = ['Refund', 'Support', 'Inquiry']

# Classify the text
result = classifier(text, candidate_labels=labels)

print("Classification Result: ", result)
