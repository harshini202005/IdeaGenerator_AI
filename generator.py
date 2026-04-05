import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def ai_query(prompt, max_tokens=200, temperature=0.8):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature,
        max_tokens=max_tokens
    )
    return response.choices[0].message.content


def generate_output(mode, domain, theme):

    if mode == "Startup":
        prompt = f"""
        Generate:
        A startup name
        3 features
        Target users
        Tagline

        Domain: {domain}
        Theme: {theme}
        """

    elif mode == "Story":
        prompt = f"""
        Generate:
        Story title
        Main characters
        Short plot

        Theme: {theme}
        """

    elif mode == "Game":
        prompt = f"""
        Generate:
        Game name
        Characters
        Gameplay idea

        Theme: {theme}
        """

    else:  
        prompt = f"""
        Generate:
        Product name
        Features
        Target audience
        Marketing tagline

        Domain: {domain}
        Theme: {theme}
        """

    result = ai_query(prompt)

    return [line.strip(" -•") for line in result.split("\n") if line.strip()]