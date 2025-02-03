import google.generativeai as genai
import os
import argparse
import logging
from dotenv import load_dotenv

# set up logging for debugging purposes
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),  # logs to the console
        logging.FileHandler("app.log")  # writes logs to a file
    ]
)
logger = logging.getLogger()

# load API key from .env
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def split_document_to_slides(markdown_text, num_slides):
    try:
        prompt = f"Split this document into {num_slides} logical sections with each representing a discrete idea suitable for a presentation slide. Make sure the sections flow well cohesively and the ideas are distinct.\n\nMarkdown text:\n{markdown_text}"
        logger.debug(f"Generated prompt for {num_slides} slides")

        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)

        if response.text:
            sections = response.text.strip().split('\n\n')
            logger.info(f"Split into {len(sections)} sections successfully.")
            return sections
        else:
            logger.warning("No response text returned from the API.")
            return ["Error: No response from API."]

    except Exception as e:
        logger.error(f"API Error: {str(e)}")
        return [f"API Error: {str(e)}"]

def main():
    parser = argparse.ArgumentParser(description="Split markdown file into presentation slides")
    parser.add_argument("markdown_file", help="Path to the markdown file to be processed")
    parser.add_argument("num_slides", type=int, help="Number of slides (1-50)")

    args = parser.parse_args()

    # error handling and logging
    try:
        if args.num_slides < 1 or args.num_slides > 50:
            raise ValueError("Invalid input: Number of slides must be between 1 and 50.")

        logger.info(f"Processing file: {args.markdown_file} with {args.num_slides} slides.")

        if not os.path.exists(args.markdown_file):
            raise FileNotFoundError(f"Error: The file '{args.markdown_file}' does not exist.")

        logger.debug(f"Reading file: {args.markdown_file}")

        with open(args.markdown_file, "r", encoding="utf-8") as file:
            markdown_text = file.read().strip()

        if not markdown_text:
            raise ValueError("Error: The markdown file is empty.")

        logger.debug("Markdown file read successfully.")

        sections = split_document_to_slides(markdown_text, args.num_slides)
        logger.info("Sections split successfully.")
        for section in sections:
            print(section)

    except ValueError as ve:
        logger.error(f"Input Error: {ve}")
        print(f"Input Error: {ve}")

    except FileNotFoundError as fe:
        logger.error(f"File Error: {fe}")
        print(fe)

    except Exception as e:
        logger.error(f"Unexpected Error: {e}")
        print(f"Unexpected Error: {e}")


if __name__ == "__main__":
    logger.info("Starting the script...")
    main()
    logger.info("Script finished.")
