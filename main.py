from google import genai

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client(api_key="AIzaSyBAzkjGJ_7nHjWD3tq1OkpdZvREAx-NEbY")

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="tell me the best crop to from august to november considring  nitrogen=110cg/kg, soil oragnic carbon = 107dg/kg, ph = 7.8, clay content=232g/kg, Vol. water content at -33 kPa"
)
print(response.text)