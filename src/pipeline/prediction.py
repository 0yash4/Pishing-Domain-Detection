from dataclasses import dataclass

from src.exception import CustomException
from src.logger import logging
from src.url.url_credentials import url_credentials
from src.url.url_details import url_details


@dataclass
class classes_initailization:
    def __init__(self, url):
        # Initializing All the imported classes
        self.url_credentials = url_credentials(url)
        self.url_details = url_details(url)
        
class me_try:
    def __init__(self, url):
        self.classes_initailization = classes_initailization(url)
        self.length_url = self.classes_initailization.url_details.url_length()
        
    def length(self):
        qty_dot = self.classes_initailization.url_details.count_signs_in_url()["."]
        return qty_dot
    
class CustomData1:
    def __init__(self, url):
        self.classes_initailization = classes_initailization(url)
        self.qty_dot_url = self.classes_initailization.url_details.count_signs_in_url()["."]
        self.qty_hyphen_url = self.classes_initailization.url_details.count_signs_in_url()["-"]
        self.qty_underline_url = self.classes_initailization.url_details.count_signs_in_url()["_"]
        self.qty_slash_url = self.classes_initailization.url_details.count_signs_in_url()["/"]
        self.qty_questionmark_url = self.classes_initailization.url_details.count_signs_in_url()["?"]
        self.qty_equal_url = self.classes_initailization.url_details.count_signs_in_url()["="]
        self.qty_at_url = self.classes_initailization.url_details.count_signs_in_url()["@"]
        self.qty_and_url = self.classes_initailization.url_details.count_signs_in_url()["&"]
        self.qty_exclamation_url = self.classes_initailization.url_details.count_signs_in_url()["!"]
        self.qty_space_url = self.classes_initailization.url_details.count_signs_in_url()[" "]

class CustomData2:
    def __init__(self, url):
        self.classes_initailization = classes_initailization(url)
        self.qty_tilde_url = self.classes_initailization.url_details.count_signs_in_url()["∼"]
        self.qty_comma_url = self.classes_initailization.url_details.count_signs_in_url()[","]
        self.qty_plus_url = self.classes_initailization.url_details.count_signs_in_url()["+"]
        self.qty_asterisk_url = self.classes_initailization.url_details.count_signs_in_url()["*"]
        self.qty_hashtag_url = self.classes_initailization.url_details.count_signs_in_url()["#"]
        self.qty_dollar_url = self.classes_initailization.url_details.count_signs_in_url()["$"]
        self.qty_percent_url = self.classes_initailization.url_details.count_signs_in_url()["%"]
        self.qty_tld_url = self.classes_initailization.url_details.qty_tld_url()
        self.length_url = self.classes_initailization.url_details.url_length()
        self.qty_dot_domain = self.classes_initailization.url_details.count_signs_in_url_domain()["."]

class CustomData3:
    def __init__(self, url):
        self.classes_initailization = classes_initailization(url)
        self.qty_hyphen_domain = self.classes_initailization.url_details.count_signs_in_url_domain()["-"]
        self.qty_underline_domain = self.classes_initailization.url_details.count_signs_in_url_domain()["_"]
        self.qty_slash_domain = self.classes_initailization.url_details.count_signs_in_url_domain()["/"]
        self.qty_questionmark_domain = self.classes_initailization.url_details.count_signs_in_url_domain()["?"]
        self.qty_equal_domain = self.classes_initailization.url_details.count_signs_in_url_domain()["="]
        self.qty_at_domain = self.classes_initailization.url_details.count_signs_in_url_domain()["@"]
        self.qty_and_domain = self.classes_initailization.url_details.count_signs_in_url_domain()["&"]
        self.qty_exclamation_domain = self.classes_initailization.url_details.count_signs_in_url_domain()["!"]
        self.qty_space_domain = self.classes_initailization.url_details.count_signs_in_url_domain()[" "]
        self.qty_tilde_domain = self.classes_initailization.url_details.count_signs_in_url_domain()["∼"]

class CustomData4:
    def __init__(self, url):
        self.classes_initailization = classes_initailization(url)
        self.qty_comma_domain = self.classes_initailization.url_details.count_signs_in_url_domain()[","]
        self.qty_plus_domain = self.classes_initailization.url_details.count_signs_in_url_domain()["+"]
        self.qty_asterisk_domain = self.classes_initailization.url_details.count_signs_in_url_domain()["*"]
        self.qty_hashtag_domain = self.classes_initailization.url_details.count_signs_in_url_domain()["#"]
        self.qty_dollar_domain = self.classes_initailization.url_details.count_signs_in_url_domain()["$"]
        self.qty_percent_domain = self.classes_initailization.url_details.count_signs_in_url_domain()["%"]
        self.qty_vowels_domain = self.classes_initailization.url_details.qty_vowels_domain()
        self.domain_length = self.classes_initailization.url_details.domain_length()
        self.domain_in_ip = self.classes_initailization.url_credentials.domain_in_ip()
        self.server_client_domain = self.classes_initailization.url_credentials.server_client_domain()

class CustomData5:
    def __init__(self, url):
        self.classes_initailization = classes_initailization(url)
        self.qty_dot_directory = self.classes_initailization.url_details.count_signs_in_url_directory()["."]
        self.qty_hyphen_directory = self.classes_initailization.url_details.count_signs_in_url_directory()["-"]
        self.qty_underline_directory = self.classes_initailization.url_details.count_signs_in_url_directory()["_"]
        self.qty_slash_directory = self.classes_initailization.url_details.count_signs_in_url_directory()["/"]
        self.qty_questionmark_directory = self.classes_initailization.url_details.count_signs_in_url_directory()["?"]
        self.qty_equal_directory = self.classes_initailization.url_details.count_signs_in_url_directory()["="]
        self.qty_at_directory = self.classes_initailization.url_details.count_signs_in_url_directory()["@"]
        self.qty_and_directory = self.classes_initailization.url_details.count_signs_in_url_directory()["&"]
        self.qty_exclamation_directory = self.classes_initailization.url_details.count_signs_in_url_directory()["!"]
        self.qty_space_directory = self.classes_initailization.url_details.count_signs_in_url_directory()[" "]

class CustomData6:
    def __init__(self, url):
        self.classes_initailization = classes_initailization(url)
        self.qty_tilde_directory = self.classes_initailization.url_details.count_signs_in_url_directory()["∼"]
        self.qty_comma_directory = self.classes_initailization.url_details.count_signs_in_url_directory()[","]
        self.qty_plus_directory = self.classes_initailization.url_details.count_signs_in_url_directory()["+"]
        self.qty_asterisk_directory = self.classes_initailization.url_details.count_signs_in_url_directory()["*"]
        self.qty_hashtag_directory = self.classes_initailization.url_details.count_signs_in_url_directory()["#"]
        self.qty_dollar_directory = self.classes_initailization.url_details.count_signs_in_url_directory()["$"]
        self.qty_percent_directory = self.classes_initailization.url_details.count_signs_in_url_directory()["%"]
        self.directory_length = self.classes_initailization.url_details.directory_length()
        self.qty_dot_file = self.classes_initailization.url_details.count_signs_in_url_path_file()["."]
        self.qty_hyphen_file = self.classes_initailization.url_details.count_signs_in_url_path_file()["-"]
        
class CustomData7:
    def __init__(self, url):
        self.classes_initailization = classes_initailization(url)
        self.qty_underline_file = self.classes_initailization.url_details.count_signs_in_url_path_file()["_"]
        self.qty_slash_file = self.classes_initailization.url_details.count_signs_in_url_path_file()["/"]
        self.qty_questionmark_file = self.classes_initailization.url_details.count_signs_in_url_path_file()["?"]
        self.qty_equal_file = self.classes_initailization.url_details.count_signs_in_url_path_file()["="]
        self.qty_at_file = self.classes_initailization.url_details.count_signs_in_url_path_file()["@"]
        self.qty_and_file = self.classes_initailization.url_details.count_signs_in_url_path_file()["&"]
        self.qty_exclamation_file = self.classes_initailization.url_details.count_signs_in_url_path_file()["!"]
        self.qty_space_file = self.classes_initailization.url_details.count_signs_in_url_path_file()[" "]
        self.qty_tilde_file = self.classes_initailization.url_details.count_signs_in_url_path_file()["∼"]
        self.qty_comma_file = self.classes_initailization.url_details.count_signs_in_url_path_file()[","]

class CustomData8:
    def __init__(self, url):
        self.classes_initailization = classes_initailization(url)
        self.qty_plus_file = self.classes_initailization.url_details.count_signs_in_url_path_file()["+"]
        self.qty_asterisk_file = self.classes_initailization.url_details.count_signs_in_url_path_file()["*"]
        self.qty_hashtag_file = self.classes_initailization.url_details.count_signs_in_url_path_file()["#"]
        self.qty_dollar_file = self.classes_initailization.url_details.count_signs_in_url_path_file()["$"]
        self.qty_percent_file = self.classes_initailization.url_details.count_signs_in_url_path_file()["%"]
        self.file_length = self.classes_initailization.url_details.file_path_length()
        self.qty_dot_params = self.classes_initailization.url_details.count_signs_in_url_parameters()["."]
        self.qty_hyphen_params = self.classes_initailization.url_details.count_signs_in_url_parameters()["-"]
        self.qty_underline_params = self.classes_initailization.url_details.count_signs_in_url_parameters()["_"]
        self.qty_slash_params = self.classes_initailization.url_details.count_signs_in_url_parameters()["/"]

class CustomData9:
    def __init__(self, url):
        self.classes_initailization = classes_initailization(url)
        self.qty_questionmark_params = self.classes_initailization.url_details.count_signs_in_url_parameters()["?"]
        self.qty_equal_params = self.classes_initailization.url_details.count_signs_in_url_parameters()["="]
        self.qty_at_params = self.classes_initailization.url_details.count_signs_in_url_parameters()["@"]
        self.qty_and_params = self.classes_initailization.url_details.count_signs_in_url_parameters()["&"]
        self.qty_exclamation_params = self.classes_initailization.url_details.count_signs_in_url_parameters()["!"]
        self.qty_space_params = self.classes_initailization.url_details.count_signs_in_url_parameters()[" "]
        self.qty_tilde_params = self.classes_initailization.url_details.count_signs_in_url_parameters()["∼"]
        self.qty_comma_params = self.classes_initailization.url_details.count_signs_in_url_parameters()[","]
        self.qty_plus_params = self.classes_initailization.url_details.count_signs_in_url_parameters()["+"]
        self.qty_asterisk_params = self.classes_initailization.url_details.count_signs_in_url_parameters()["*"]

class CustomData10:
    def __init__(self, url):
        self.classes_initailization = classes_initailization(url)
        self.qty_hashtag_params = self.classes_initailization.url_details.count_signs_in_url_parameters()["#"]
        self.qty_dollar_params = self.classes_initailization.url_details.count_signs_in_url_parameters()["$"]
        self.qty_percent_params = self.classes_initailization.url_details.count_signs_in_url_parameters()["%"]
        self.params_length = self.classes_initailization.url_details.params_length()
        self.tld_present_params = self.classes_initailization.url_details.tld_present_params()
        self.qty_params = self.classes_initailization.url_details.qty_params()
        self.email_in_url = self.classes_initailization.url_credentials.email_in_url()
        self.time_response = self.classes_initailization.url_credentials.time_response()
        self.domain_spf = self.classes_initailization.url_credentials.domain_spf()
        self.asn_ip = self.classes_initailization.url_credentials.asn_ip()

class CustomData11:
    def __init__(self, url):
        self.classes_initailization = classes_initailization(url)
        self.time_domain_activation, self.time_domain_expiration = self.classes_initailization.url_credentials.time_domain_activation_expiration()
        self.qty_ip_resolved = self.classes_initailization.url_credentials.qty_ip_resolved()
        self.qty_nameservers = self.classes_initailization.url_credentials.qty_nameservers()
        self.qty_mx_servers = self.classes_initailization.url_credentials.qty_mx_servers()
        self.ttl_hostname = self.classes_initailization.url_credentials.ttl_hostname()
        self.tls_ssl_certificate = self.classes_initailization.url_credentials.tls_ssl_certificate()
        self.qty_redirects = self.classes_initailization.url_credentials.qty_redirects()
        self.url_google_index = self.classes_initailization.url_credentials.url_google_index()
        self.domain_google_index = self.classes_initailization.url_credentials.domain_google_index()
        self.url_shortened = self.classes_initailization.url_credentials.url_shortened()

    


if __name__ == "__main__":
    url1 = "https://example.com/search?qu..ery=python&category=tutorials&sort=popularity"
    init = me_try(url1)
    print(init.length())