
# Document → Slides 

The purpose of this program is to use an LLM to split a document into multiple sections where each section represents a discrete idea, and each of these sections could essentially be turned into a single slide in a presentation. This Python program takes a markdown document and splits it into a target number of slides/sections specified by the user input. It uses Google Gemini API by calling the gemini-1.5-flash model to divide the content into logical sections. 

 



## Why this solution?

I specifically chose Python for this project because I felt it was the ideal choice for different reasons:

- Ease of use: Python's syntax is easy to follow along with quick development and testing initial ideas in a short amount of time.  
- Extensive libraries: Since this project involved making API calls to an LLM, Python has many libraries for working with APIs, handling files, and managing errors, which were all used in my program. 

Here's why I chose Google's Gemini over the OpenAI and Claude models:

- Natural Language Understanding: Gemini excels at generating text in a way that aligns with this project's goals to create distinct sections for each slide since it's optimized for content generation with special attention to structure and flow. 
- Response Formatting: Gemini's responses tend to be more concise and structured, which makes it ideal to fit the content neatly into a presentation slide. 
- Performance and Efficiency: Gemini provides strong performance with fast processing times, which is ideal for the test cases with longer documents. 

How the Code Works:

- Document Input: The program reads the markdown content from the .md file provided by the user and this should be located in the /test_cases directory. 
- Input Validation: The user is then prompted to input the number of slides (between 1 and 50) and the program first checks if this is valid input.
- If valid, the markdown file is then passed to the Gemini API, which uses its LLM capabilities to split the document into the specified number of logical sections. 
- Return Sections: Once this API response is processed, these split document sections are printed as plain text on the terminal where each section corresponds to a distinct idea for a presentation slide. 
## Features

- Markdown Input: A document, as a string in markdown format
- Customizable Number of Slides: The number of slides (sections) can be set between 1 and 50 specified by the user. 
- API Integration: Uses the Gemini API to process the markdown document into discrete sections. 
- Error Handling: Includes error handling for invalid inputs, missing files, and API errors.
- Logging: Logs key actions and errors to help with debugging and tracking API usage.


## Installation

Clone the repository:

```bash
  git clone https://github.com/zunera-ashar/Document-to-Slides/tree/main

```

Navigate into the project directory:

```bash
  cd Document-to-Slides
```

Install dependencies from `requirements.txt`:

```bash
  pip install -r requirements.txt
```

Set up your `.env` file:
- Create a `.env` file in the root of the repo.
- Add your Gemini API key to it 
```bash
  GEMINI_API_KEY=your_api_key_here
```




## Usage

1. Create a test_cases directory in the root of the repo. 

2. Place all your markdown documents (ex: sample_text_file.md) inside this /test_cases repo. 

3. Run the program from the command line, passing the markdown file and target number of slides as arguments:

```bash
  python main.py test_cases/sample_text_file.md 10
```

Change the name of the file to swap it with another test case. For example:

```bash
  python main.py test_cases/example_text_file_2.md 5
  python main.py test_cases/example_text_file_3.md 20
```

4. Then this program will split the markdown into sections and should display the results along with the logging in the terminal.



## API Limitations

Currently, this project only supports the gemini-1.5-flash model. Ensure that your API key has access to this specific model.


- Rate Limiting: Since the Gemini API has usage limits, you may encounter rate-limiting errors if you exceed the free tier quota, which will be logged if this error is encountered. 


