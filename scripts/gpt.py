import openai
import sys

openai.api_key = 'YOUR_API_KEY'  # OpenAI API anahtarınızı buraya girin

def ask_gpt(question):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": question}
        ]
    )
    return response.choices[0].message.content

def main():
    if len(sys.argv) > 1:
        question = " ".join(sys.argv[1:])
        answer = ask_gpt(question)
        print("Cevap:", answer)
    else:
        print("Soru belirtmediniz.")

if __name__ == "__main__":
    main()
