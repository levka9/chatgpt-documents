from openai import OpenAI
from datetime import datetime
from file_text import FileText
import json

def get_current_datetime_text():
    now = datetime.now()
    return now.strftime("%Y-%m-%d_%I-%M")

with open("secrets.json", "r", encoding="utf-8") as file:
    json_file_content = json.load(file)

api_key_value = json_file_content["openai"]["api_key"]

# Replace with your actual API key
client = OpenAI(api_key = api_key_value)
file_path = "doc-source/" + "שיטות בהפעלת לחץ פלי.pdf"

fileText = FileText(file_path)
file_content = fileText.get_text_from_pdf()

# Ask a question based on the file
# Send prompt with file content and ask a question
response = client.chat.completions.create(
    model="gpt-4.1",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user", "content": f"Here is a file:\n\n{file_content}\n\n"
            + "Prepare introduction about me and why I wanna present that to the business people and graduated people spesial in the programmer field."
            + "Prepare that in 3 variations and in Hebrew language and make in bold important parts."    
            + "add details about my expirience, how many times I complained to the police, quantity of damages"
            # + "Prepare summary for 2.5 pages in A4 format in Hebrew language"
            # + "Prepare this dialog with two persons for radio about criminal topic in Hebrew language."
            # + "Please prepare 100 sentences."
        }
    ]
)

# Print the response
#print(response.choices[0].message.content)
datetime_now = get_current_datetime_text()
file_name = "responses\\" + datetime_now + "_response.txt"

with open(file_name, "w", encoding="utf-8") as file:
    file.write(response.choices[0].message.content)

print(f"response saved to {file_name}")