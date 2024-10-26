'''
    News App using NewsAPI and requests module
'''
import requests

# Function to get news using NewsAPI
def get_news(url, api_key):
    ''' Function to get news from the url '''
    headers = {
        'Authorization': f'Bearer {api_key}'
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            data = response.json()
            if data.get('articles'):
                for idx, article in enumerate(data['articles'], start=1):
                    print(f"\nNews {idx}:")
                    print(f"Title: {article['title']}")
                    print(f"Description: {article['description']}")
                    print(f"Source: {article['source']['name']}")
                    print(f"Published At: {article['publishedAt']}")
                    print(f"URL: {article['url']}")
            else:
                print("No articles found.")
        else:
            print(f"Error: Unable to fetch news. Status Code: {response.status_code}")
    except requests.exceptions.Timeout:
        print("Error: The request timed out.")
    except requests.exceptions.RequestException as e:
        print(f"Error: An error occurred: {e}")

def search_news(api_key):
    ''' Choice 1 '''
    keyword = input("Enter a keyword/topic to search news articles: ").strip()
    if keyword:
        url = f'https://newsapi.org/v2/everything?q={keyword}&sortBy=popularity&apiKey={api_key}'
        get_news(url, api_key)
    else:
        print("Keyword cannot be empty.")

def top_headlines_country(api_key):
    ''' Choice 2 '''
    country = input("Enter country code (e.g., us, in, gb): ").strip()
    if country:
        url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={api_key}'
        get_news(url, api_key)
    else:
        print("Country code cannot be empty.")

def top_headlines_source(api_key):
    ''' Choice 3 '''
    source = input("Enter the news source (e.g., bbc-news, cnn, techcrunch): ").strip()
    if source:
        url = f'https://newsapi.org/v2/top-headlines?sources={source}&apiKey={api_key}'
        get_news(url, api_key)
    else:
        print("Source cannot be empty.")

# Main Program
def main():
    ''' Main Function '''
    api_key = 'eb4432547bc54ed0aa2f3643c2298ebd'  # Hardcoded API key
    options = {
        '1': search_news,
        '2': top_headlines_country,
        '3': top_headlines_source,
        }
    while True:
        print("\nWelcome to the News API Program!")
        print("1. Search for news articles by keyword or topic.")
        print("2. Get top news headlines in a specific country.")
        print("3. Get top headlines from a specific news source.")
        print("4. To Exit.")
        choice = input("Enter your choice (1-4): ").strip()
        if choice in options:
            options[choice](api_key)  # Call the corresponding function
        elif choice == '4':
            print("Thanks for coming.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

# Run the program
if __name__ == "__main__":
    main()
