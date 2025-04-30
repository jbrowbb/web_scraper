# test_transformers.py
try:
    from transformers import pipeline
    print("transformerslibrary imported successfully!")

    # try a simple pipeline
    sentiment_pipeline = pipeline("sentiment-analysis")
    result = sentiment_pipeline("I love using transformers!")
    print(f"Sentiment analysis result: {result}")

except ImportError as e:
    print(f"Error importing transformers: {e}")
    print("Make sure you hae installed transformers library in your active environment.")

except Exception as e:
    print(f"An unexpecting error occurred: {e}")