from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import requests
import re

# Function to start the bot
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Welcome to the Marketing Assistant Bot! 🎉\n"
        "Let’s begin with understanding your business.\n"
        "What industry is your business in?"
    )

# Function to handle user responses and guide the flow
async def handle_response(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_response = update.message.text.strip()
    user_data = context.user_data

    if 'industry' not in user_data:
        user_data['industry'] = user_response
        await update.message.reply_text('Got it! What is your primary business objective?')
    elif 'objective' not in user_data:
        user_data['objective'] = user_response
        await update.message.reply_text('Do you have a website? (Please answer yes or no)')
    elif 'website' not in user_data:
        user_data['website'] = user_response.lower() == 'yes'
        await update.message.reply_text('Do you use any social media platforms? (yes/no)')
    elif 'social_media' not in user_data:
        user_data['social_media'] = user_response.lower() == 'yes'
        await update.message.reply_text('Are you currently running PPC campaigns? (yes/no)')
    elif 'ppc' not in user_data:
        user_data['ppc'] = user_response.lower() == 'yes'
        await update.message.reply_text('Who is your target audience? (e.g., young adults, professionals, etc.)')
    elif 'target_audience' not in user_data:
        user_data['target_audience'] = user_response
        await update.message.reply_text('What geographical location would you like to target?')
    elif 'location' not in user_data:
        user_data['location'] = user_response
        keywords = generate_keywords(user_data)
        await update.message.reply_text(f'Generated Keywords: {keywords}\nLet me know if you need help with anything else.')

# Function to generate keywords based on user input
def generate_keywords(data):
    industry = data.get('industry', 'general')
    target_audience = data.get('target_audience', 'general audience')
    dataset = [
        "marketing", "SEO", "content creation", "social media", "branding", "campaign management",
        "lead generation", "conversion optimization", "customer engagement"
    ]
    relevant_keywords = [
        keyword for keyword in dataset 
        if industry.lower() in keyword.lower() or target_audience.lower() in keyword.lower()
    ]
    return ', '.join(relevant_keywords) if relevant_keywords else "No relevant keywords found."

# Function to fetch trends from a specific website
async def fetch_trends(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    url = "https://databox.com/ppc-industry-benchmarks"  # Example website
    try:
        response = requests.get(url)
        response.raise_for_status()
        trends = parse_trends(response.text)
        await update.message.reply_text(f'Latest Trends: {trends}')
    except requests.exceptions.RequestException as e:
        await update.message.reply_text(f'Error fetching trends: {e}')

# Function to parse trends from the website
def parse_trends(html_content):
    trends = re.findall(r'<strong>(.*?)</strong>', html_content)
    return ', '.join(trends[:5]) if trends else "No trends found."

# Function to handle advanced queries like FAQs
async def faq(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    question = update.message.text.lower().strip()
    response = get_faq_answer(question)
    await update.message.reply_text(response)

# Function to retrieve FAQ answers
def get_faq_answer(question):
    faq_responses = {
        "ad performance": "Optimize targeting, refine ad copy, and use A/B testing to improve ad performance.",
        "website traffic": "Increase traffic through SEO, engaging content, and effective PPC campaigns.",
        "cpc for construction business": "The average CPC for a construction business is approximately $2.5, but it may vary based on location and competition."
    }
    return faq_responses.get(question, "I’m not sure about that. Please consult a marketing expert.")

# Main function to initialize and run the bot
def main():
    token = "7141930622:AAG_BT9JQZKnU0T-jzWfNY-SYaMV3DjvJII"  # Replace with your bot's API token
    application = ApplicationBuilder().token(token).build()

    # Handlers
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('trends', fetch_trends))
    application.add_handler(CommandHandler('faq', faq))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_response))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, faq))

    application.run_polling()

if __name__ == '__main__':
    main()
