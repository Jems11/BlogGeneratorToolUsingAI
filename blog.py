import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

print("start generating content..")

def GenerateBlogTopiocs(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        # prompt="Generate blog topic ideas on : how to make a application for e-commerce store\n \n 1.",
        prompt= "Generate blog topics on : {} \n \n 1. ".format(prompt),
        temperature=0.7,
        max_tokens=120,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response['choices'][0]['text']

def GenerateBlogSections(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        # prompt="Generate blog topic ideas on : how to make a application for e-commerce store\n \n 1.",
        prompt= "Expand blog title into high level blog sections : {} \n \n 1. ".format(prompt),
        temperature=0.7,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response['choices'][0]['text']

def GenerateBlogContent(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        # prompt="Generate blog topic ideas on : how to make a application for e-commerce store\n \n 1.",
        prompt= "Expand blog section into a detailed professional, witty and cleaver explanation: : {} \n \n".format(prompt),
        temperature=0.7,
        max_tokens=300,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response['choices'][0]['text']