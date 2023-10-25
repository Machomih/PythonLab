def build_xml_element(tag, content, **key_value_elements):
    string = "<" + tag
    for i in key_value_elements:
        string = string + " " + i + " = " + "\"" + key_value_elements[i] + "\""
    string = string + ">" + content + "</" + tag + ">"
    return string


print(build_xml_element("a", "Hello there", href="https://python.org", _class="my-link", id="someid"))
