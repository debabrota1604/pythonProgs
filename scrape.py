import requests
from bs4 import BeautifulSoup

def get_directory_listing(url):
    try:
        # Perform an HTTP GET request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(response.content, 'html.parser')

            # Find all <a> tags (links) in the HTML content
            links = soup.find_all('a')

            # Extract the href attribute from each link
            file_list = [link.get('href') for link in links]

            # Filter out None values and parent directory links
            file_list = [file for file in file_list if file and not file.startswith('../')]

            # Print the file list
            print("\nFile List:")
            for file in file_list:
                print(file)

        else:
            print(f"Error: Unable to access the URL. Status code: {response.status_code}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Get the URL input from the user
    url = input("Enter the URL of the directory: ")

    # Ensure the URL ends with a '/'
    if not url.endswith('/'):
        url += '/'

    # Call the function to get the directory listing
    get_directory_listing(url)

