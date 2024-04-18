from urllib.parse import parse_qs, urlparse


class url_details:
    def __init__(self, url):
       self.url = url
       self.parsed_url = urlparse(url)
       self.url_domain = self.parsed_url.netloc
       self.url_path_file = self.parsed_url.path.split("/")[-1]
       self.url_parameters = self.parsed_url.query 
       self.url_directory = self.parsed_url.path.split("/")[1]
       #to avoid Path/File and Directory are same.
       if self.url_path_file == self.url_directory:
           self.url_directory = None
        
    def count_signs_in_url(self):
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
    
    def count_signs_in_url_domain(self):
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
    
    def count_signs_in_url_directory(self):
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
    
    def count_signs_in_url_path_file(self):
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
    
    def count_signs_in_url_parameters(self):
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
    
    def test(self):
        return(
        self.url_domain,
        self.url_path_file,
        self.url_directory,
        self.url_parameters
        )

    
if __name__ == "__main__":
    url1 = "https://www.example.com/ya.sdj.-df/page1231-dwq!?query=example&lang=en"
    url = url_details(url1)
    print(url.test())
    print(url.count_signs_in_url_parameters())
    print(url.count_signs_in_url_path_file())
    print(url.count_signs_in_url_directory())
    print(url.count_signs_in_url_domain())
    print(url.count_signs_in_url())