Random Fractal Generator
This script generates and displays a random visual animation, pattern, or fractal using the Python Imaging Library (PIL).

How it works
The script first creates a blank canvas using the Image.new() function and sets the canvas size to (500, 500) and background color to white.
Next, it defines a function called "generate_visual()" which randomly chooses one of three options: animation, pattern, or fractal.
Depending on the chosen option, the function generates random coordinates, color, and draws the visual using the ImageDraw.Draw() function.
The script then calls the generate_visual() function 10 times to generate 10 random visuals.
Finally, it gets the current date and time, formats it as a string, and saves the canvas as an image file with a filename that includes the date and time.
Requirements
Python 3
PIL (Python Imaging Library)
Usage
To run the script, simply run the following command in your terminal:

Copy code
python random_visual_generator.py
The script will generate and display the random visuals and save them as an image file in the current directory.



