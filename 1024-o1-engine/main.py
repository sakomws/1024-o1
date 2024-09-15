import warnings
import urllib3

# Suppress all warnings from urllib3
urllib3.disable_warnings()

# If you want to suppress all warnings (use with caution)
warnings.filterwarnings("ignore")

import json
import requests
import time
import sys
import random
import threading

# Define your Chameleon API key here
CHAMELEON_API_KEY = "YOUR_CHAMELEON_API_KEY_HERE"
# Define the intent system with descriptions
intent_system = {
    "Customer": {
        "description": "This customer, identified as cus_01J7SBKDHBNYJVP0PGSCHR7K4B, registered with the email sako@1024-o1.ai on September 14, 2024. The customer currently has two pending orders, both placed on the same day as the account creation. The customer has not provided a first or last name, nor any billing or shipping phone details. Both orders have the status 'pending' and are awaiting payment and fulfillment. The customer is associated with the sales channel sc_01J7SBC76GFW21A6TTFXHB6PA3 and uses USD as the primary currency. The metadata and shipping addresses are currently empty.",
        "tags": [
            "New Customer",
            "Pending Payment",
            "Multiple Orders",
            "No Billing Address",
            "No Shipping Address",
            "First-Time Buyer"
        ]
    },
    "Order": {
        "description": "This order, identified as order_01J7SBT8CA5CJJ4BTJ4QTZ7Z2C, was placed by Shahriyar Mammadov on September 14, 2024. The order includes Medusa Sweatpants (size M) priced at $33.50, with a total of $41.50 including a flat rate shipping charge of $8.00 via FakeEx Standard. The order is currently pending with an awaiting payment status and has not been fulfilled yet. The shipping address is in Sunnyvale, California, and the billing address is the same. The order was placed under the sales channel sc_01J7SBC76GFW21A6TTFXHB6PA3. There are no discounts, refunds, or gift cards applied to this order. Taxes on both the items and shipping are 0%.",
        "tags": [
            "Awaiting Fulfillment",
            "Flat Rate Shipping",
            "No Discounts",
            "California Shipping",
            "No Taxes",
            "First-Time Buyer"
        ]
    },
    "Product": {
        "description": "This product, titled 1024-shirt, is part of the Merch collection. It is described as 'Warm and Cozy' and features a lightweight cotton material. The product is listed under the handle '1024-o1' and is available in multiple sizes, with the variant 'S' currently in stock. The product is priced at $100.00 and uses the Default Shipping Profile. The product status is published and is available for purchase through the Default Sales Channel. The weight, length, width, and height of the item are all 10 units, making it compact and easy to ship. No discounts have been applied to this product, and backorders are not allowed.",
        "tags": [
            "Merch",
            "Cotton",
            "Published",
            "Default Shipping Profile",
            "Warm and Cozy",
            "No Backorder",
            "Small Size Available"
        ]
    }
}

def format_intent_system() -> str:
    """Format the intent system for Chameleon."""
    formatted = "Intent System:\n\n"
    for category, data in intent_system.items():
        formatted += f"Category: {category}\n"
        formatted += f"Description: {data['description']}\n"
        formatted += "Tags:\n"
        for tag in data['tags']:
            formatted += f"- {tag}\n"
        formatted += "\n"
    return formatted

def query_chameleon(customer_info: dict, order_info: dict, product_info: dict) -> str:
    """Send a query to Chameleon API and return the brief product description to add in website. No mention of customer Dear Customer or best regards to the customer. """
    url = "https://api.anthropic.com/v1/messages"
    
    headers = {
        "Content-Type": "application/json",
        "X-API-Key": CHAMELEON_API_KEY,
        "anthropic-version": "2023-06-01"
    }

    # Format the input to include customer, order, and product information
    input_data = {
        "customer": customer_info,
        "order": order_info,
        "product": product_info
    }

    prompt = f"""
    {format_intent_system()}

    Input Data:
    {json.dumps(input_data, indent=2)}

    Based on the above intent system and all input data provided, provide a brief personalized to the customer product description with 2 sentences. Do not mention 'Dear Customer' or 'Best regards.
    """

    data = {
        "model": "claude-3-sonnet-20240229",
        "max_tokens": 3000,
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        content = response.json()['content'][0]['text']
        return content
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while querying Chameleon: {e}")
        return None

def animated_thinking():
    """Display an animated 'Chameleon is thinking' message with colored lines."""
    print("\033[?25l", end="")  # Hide cursor
    colors = ['\033[92m', '\033[93m', '\033[94m', '\033[95m', '\033[96m']  # Green, Yellow, Blue, Magenta, Cyan
    message = "Chameleon is thinking..."
    
    def animation():
        while True:
            for color in colors:
                sys.stdout.write(f"{color}{message}\033[0m\n")
                sys.stdout.flush()
                time.sleep(0.5)
            
            time.sleep(1)  # Pause before restarting
            sys.stdout.write("\033[2J")  # Clear the entire screen
            sys.stdout.write("\033[H")   # Move cursor to home position

    # Start the animation in a separate thread
    thread = threading.Thread(target=animation)
    thread.daemon = True
    thread.start()

    return thread

def output_product_description():
    # Example input data for customer, order, and product
    customer_info = intent_system['Customer']
    order_info = intent_system['Order']
    product_info = intent_system['Product']

    # Start the animation
    thinking_animation = animated_thinking()

    # Query Chameleon
    chameleon_response = query_chameleon(customer_info, order_info, product_info)

    # Stop the animation
    thinking_animation.join(timeout=0.5)
    print("\033[?25h", end="")  # Show cursor
    sys.stdout.write("\033[2J")  # Clear the entire screen
    sys.stdout.write("\033[H")   # Move cursor to home position
    print("\n")  # Move to the next line after animation

    if chameleon_response:
        print("\nChameleon's Personalized Product Description:")
        print(chameleon_response)
        return chameleon_response
    else:
        print("Failed to get a response from Chameleon.")

output=output_product_description()

# Set your backend URL and API token
product_id='prod_01J7SKPVZ6C5WT8FGY6FVH46P8'
backend_url = 'http://localhost:9000/admin/products/{product_id}'
api_token = 'api_token'
cookie='cookie'

# Define the headers
headers = {
    'Cookie': '{cookie}',
    'Content-Type': 'application/json'
}

# Define the data payload
data = {
    "description": output
}

# Send the POST request
response = requests.post(backend_url, headers=headers, json=data)

# Check the response
if response.status_code == 200:
    print('Success:', response.json())
else:
    print('Failed:', response.status_code, response.text)