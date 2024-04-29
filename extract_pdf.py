import re
import os
import PyPDF2

# For this function, I will be using PyPDF2 to read the pdf file and then once the pdf file is read,
# then I will use regex expressions to parse through the pdf to obtain the different values in the pdf.
# This function will output the sum of all of the numbers in the pdf from line 1 to line 10 and will
# also throw an exception message if at any point in the method there is a bad number. But it will
# calculate the sum of the other acceptable numbers if an exception is thrown
def extract_sum(pdf):
    # Open the pdf file
    with open(pdf, 'rb') as file: # We will just be reading the pdf file so we use 'rb'
        # Make the pdf reader object using PyPDF2
        reader = PyPDF2.PdfReader(file)

        # Initialize the variables that this function will be using to store the sum
        # and for each individual line
        sum = 0
        lines = ''
        
        # Make a variable for the string output
        output = ''

        # Go through the pdf file and find the numbers in the file from line 1 to line 10 excluding line 9
        # Find the text of the file
        text = reader.pages[0].extract_text()

        # Define a regex pattern to match the template of each pdf file which will follow Line x. number
        # This regex will find anything that starts with:
        # at least 3 spaces plus maybe a - sign and the number following which could be a decimal
        # This is done because of how the pdfreader reads the file
        pattern = r'\s{3,}\W?\d+.?\d*'

        # Find all the matches in the pdf text to the pattern I defined above
        matches = re.findall(pattern, text)

        # Take the digit from each of the matches and then convert it to a float
        # If the number isn't valid, then throw an exception and move on to the other numbers
        for match in matches:
            try:
                # Convert each match to a float then add each of the matches to the sum
                sum += float(match)
                
                # Add each match to the lines variable and print it after this loop
                lines += match
            # Catch the exception if you cannot convert the match to a float
            except Exception as e:
                output += "Error: " + e

        # If the sum is zero, say to the user if they accidentally didn't put any values into the file
        # otherwise print each individual line and the sum
        if(sum > 0):
            # Add the output of each individual line
            output += 'Here is each individual value in the file:\n' + lines
            # Add the sum
            output += '\nHere is the sum of file ' + pdf + ': ' + str(sum)
        else:
            # Notify the user that the sum was zero and to check if there are values in the file
            output += 'File ' + pdf + ' has a sum of zero. Please double check if ' + pdf + ' has any values in it'
            
    # Return the output
    return output
    
# This second function will go through the folder and find all of the files to read and call extract_sum
# to find the sums of each file in the folder.
def extract_from_folder(folder):
    # Set a variable to the output of this function
    output = ''
    
    # Loop through the folder to find all the files
    for file in os.listdir(folder):
        # Check to see if the file is a pdf file
        if file.endswith('.pdf'):
            # Call extract_sum on the pdf file
            output += extract_sum(file) + '\n\n'
    
    #return the output
    return output

# Add a tester function to test the two functions above
def tester(output):
    # Check to see if the output has the expected sums for each of the files
    # This first if statement is for form 0
    if output.find('468.0') == -1:
        print("Extraction output is incorrect for form 0!")
    else:
        print("Extraction output is correct for form 0!")
        
    # This second if statement is for form 1
    if output.find('449.0') == -1:
        print("Extraction output is incorrect for form 1!")
    else:
        print("Extraction output is correct for form 1!")
        
    # This third if statement is for form 2
    if output.find('435.0') == -1:
        print("Extraction output is incorrect for form 2!")
    else:
        print("Extraction output is correct for form 2!")

# Make a main function to print the functions above
def main():
    print(extract_from_folder('c:/Users/timmy/Dropbox/My PC (Timmy)/Downloads/k1x assignment')) #TODO: you will need to change this according to the path where your files are located
    
    # Call the tester function
    tester(extract_from_folder('c:/Users/timmy/Dropbox/My PC (Timmy)/Downloads/k1x assignment'))
    

if __name__ == "__main__":
    main()