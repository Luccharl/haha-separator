import re

message_template = Element("message-template").select(".msg", from_content=True)
message_container = Element("message-container")
message = Element("message")

def haha_separator(strng):
        haha = re.split(r'(HA|ha|Ha|hA|HE|he|He|hE)', strng)
        result =''.join(haha[x] if haha[x] != '' else ' ' for x in range(len(haha)))
        return result

def convert(*ags, **kws):
    if not message.element.value:
        return None

    message_html = message_template
    message_html_content = message_html.select("p")
    message_html_content.element.innerText = haha_separator(message.element.value)
    message_container.element.appendChild(message_html.element)

    message.clear()

def convert_event(e):
    if e.key == "Enter":
        convert()

message.element.onkeypress = convert_event
