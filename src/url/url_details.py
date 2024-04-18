import sys
from urllib.parse import parse_qs, urlparse

from src.exception import CustomException
from src.logger import logging
from src.url.url_substrings import URLSubStrings


class url_details:
    def __init__(self, url):
       self.url_substrings = URLSubStrings(url)  #Importing and creating the object of Url Substrings 
       self.url = self.url_substrings.url        #Assigning the URL from URL substring Constructor to the current class
       self.url_domain = self.url_substrings.url_domain()     #Getting the URL domain from the URL SubStrings class
       self.url_path_file = self.url_substrings.url_path_file()
       self.url_parameters = self.url_substrings.url_parameters()
       self.url_directory = self.url_substrings.url_domain()
       #to avoid Path/File and Directory are same.
       if self.url_path_file == self.url_directory:
           self.url_directory = None
        
    def count_signs_in_url(self):
        try:
            # Define the signs
            signs = [".", "-", "_", "/", "?", "=", "@", "&", "!", " ", "∼", ",", "+", "*", "#", "$", "%"]
            # Initialize a dictionary to store the count of each sign
            sign_counts = {sign: 0 for sign in signs}
            # Split the URL into words
            words = self.url.split()
            
            # Iterate over each word
            for word in words:
                # Iterate over each character in the word
                for char in word:
                    # If the character is a sign, increment its count
                    if char in signs:
                        sign_counts[char] += 1
                        
            # Return the the dictionary of sign counts
            return sign_counts  
            logging.info("Counted the number of signs in URL")
            
        except Exception as e:
            raise CustomException(e, sys)
        
    def count_signs_in_url_domain(self):
        try:
            # Define the signs
            signs = [".", "-", "_", "/", "?", "=", "@", "&", "!", " ", "∼", ",", "+", "*", "#", "$", "%"]

            # Initialize a dictionary to store the count of each sign
            sign_counts = {sign: 0 for sign in signs}
            
            words = self.url_domain

            # Iterate over each word
            for word in words:
                # Iterate over each character in the word
                for char in word:
                    # If the character is a sign, increment its count
                    if char in signs:
                        sign_counts[char] += 1

            # Return the sign counts
            return sign_counts  
            logging.info("Counted the number of signs in URL Domain")
            
        except Exception as e:
            raise CustomException(e, sys)
        
    def count_signs_in_url_directory(self):
        try:
            # Define the signs
            signs = [".", "-", "_", "/", "?", "=", "@", "&", "!", " ", "∼", ",", "+", "*", "#", "$", "%"]

            # Initialize a dictionary to store the count of each sign
            sign_counts = {sign: 0 for sign in signs}
            ''' 
            Sometimes Path/File and directory are same in few links 
            If Directory == Path/File then Directory will be set to none 
            and returns 0 to every sign available   

            '''
            
            if self.url_directory == None:
                return sign_counts
            else:

                words = self.url_directory

                # Iterate over each word
                for word in words:
                    # Iterate over each character in the word
                    for char in word:
                        # If the character is a sign, increment its count
                        if char in signs:
                            sign_counts[char] += 1

                # Return the sign counts
                return sign_counts  
            logging.info("Counted the number of signs in URL Directory")
            
        except Exception as e:
            raise CustomException(e, sys)
        
    def count_signs_in_url_path_file(self):
        try:
            # Define the signs
            signs = [".", "-", "_", "/", "?", "=", "@", "&", "!", " ", "∼", ",", "+", "*", "#", "$", "%"]

            # Initialize a dictionary to store the count of each sign
            sign_counts = {sign: 0 for sign in signs}
            
            words = self.url_path_file

            # Iterate over each word
            for word in words:
                # Iterate over each character in the word
                for char in word:
                    # If the character is a sign, increment its count
                    if char in signs:
                        sign_counts[char] += 1

            # Return the sign counts
            return sign_counts  
            logging.info("Counted the number of signs in URL Path/File")
            
        except Exception as e:
            raise CustomException(e, sys)
        
    def count_signs_in_url_parameters(self):
        try:
            # Define the signs
            signs = [".", "-", "_", "/", "?", "=", "@", "&", "!", " ", "∼", ",", "+", "*", "#", "$", "%"]

            # Initialize a dictionary to store the count of each sign
            sign_counts = {sign: 0 for sign in signs}
            
            words = self.url_parameters

            # Iterate over each word
            for word in words:
                # Iterate over each character in the word
                for char in word:
                    # If the character is a sign, increment its count
                    if char in signs:
                        sign_counts[char] += 1

            # Return the sign counts
            return sign_counts  
            logging.info("Counted the number of signs in URL Parameters")
            
        except Exception as e:
            raise CustomException(e, sys)
        
        
        
    
if __name__ == "__main__":
    url1 = "https://www.example.com/ya.sdj.-df/page1231-dwq!?query=example&lang=en"
    url = url_details(url1)
    print(url.count_signs_in_url_parameters())
    print(url.count_signs_in_url_path_file())
    print(url.count_signs_in_url_directory())
    print(url.count_signs_in_url_domain())
    print(url.count_signs_in_url())