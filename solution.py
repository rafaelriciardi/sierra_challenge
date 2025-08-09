import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

openai = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)

# Sierra Studio // AI Engineering Interview
# 1. What problems do you see with this code?
#   - The temperature is set to a high value, which can make the model less deterministic and predictable.
#   - There is a lack of test cases. We only have one test for the True class and none for the False one.
#   - The prompt is not wrong, but it could be improved to enhance accuracy and the expected outputs.
#   - The code is not fail safe. It will break if anything goes wrong, such as API unavailability or bad responses from the model.
#   - Thinking as system integration, the return of the model as string forces a transformation every time its values need to be accessed
# 2. What ideas do you have to make it better?
#   - Adjust the temperature to a lower value, making the model more deterministic and predictable, which is very important for this task.
#   - Create unit tests, with real examples, containing spams and not spams content.
#   - Create a function to strucurate the output as an object.
#   - Restructure the prompt with clearer and more strict instructions, making it less prone to hallucination.
#   - Add the few-shot technique to the prompt, providing a few examples and their expected outputs.
#   - Add a fallback option to another LLM service, enhancing the availability of the solution itself.
#   - Use a retry mechanism to ensure the output is as expected.
#   - Implement exception handling to act when the input is not as expected and when other kinds of errors hit the application, preventing it from breaking.
# 
# Don't use AI to answer this question :)

def check_spam(email: str) -> str | None:
    prompt = f"""\
Determine if the email is spam.

Return a valid JSON object with the format:
{{
    is_spam: is the email spam? // bool
    reason: think step by step, why is it spam or not spam? // str
}}

Email: {email}"""

    completion = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}], 
        temperature=1.0, 
        max_tokens=100,
    )
    return completion.choices[0].message.content

email = "hi how r u bro i have million dollar deal just sign here"
res = check_spam (email)
if res:
    print(json.dumps(json.loads(res),indent=2))
    