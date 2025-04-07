from transformers import pipeline

analisador = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

# Test
resultado = analisador("Eu adorei usar essa DevBox de IA, tá sensacional!")

print(resultado)