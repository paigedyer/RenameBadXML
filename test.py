import sys
from lxml import etree
import re


def open_file(input_file, output_file):
    try:
        with open(input_file, 'r') as f:
            # Read the content of the input file
            input_content = f.read()

            # Remove invalid characters using a regular expression
            sanitized_content = re.sub(r'[\x00-\x08\x0B\x0C\x0E-\x1F\x7F-\x9F]', '', input_content)

        # Parse the sanitized content as XML
        parser = etree.XMLParser(remove_blank_text=True)
        tree = etree.fromstring(sanitized_content, parser)

        for element_to_delete in tree.xpath(".//CustPrePressNotes"):
            element_to_delete.getparent().remove(element_to_delete)

        element_to_extract = tree.find(".//AVPJobRef")
        if element_to_extract is not None:
            output_file_name = element_to_extract.text + ".xml"
        else:
            output_file_name = "output.xml"

        # Write the modified XML to the output file
        with open(output_file_name, 'wb') as f:
            f.write(etree.tostring(tree, pretty_print=True))

    except FileNotFoundError:
        print(f"Input file not found: {input_file}")
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    if len(sys.argv) != 3:
        print("Usage: python your_script.py input.xml output.xml")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        open_file(input_file, output_file)


if __name__ == "__main__":
    main()
