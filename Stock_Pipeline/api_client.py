import time
import requests
import random 
from config import APIConfig
from stock_repository import upsert_stock

def fetch_meals(letter):
    url = f"{APIConfig.BASE_URL}/search.php?f={letter}"

    response = requests.get(url)
    data = response.json()

    meals = data.get('meals')
        
    if meals is None:
        return []
        
    result = []
    for meal in meals:
        name = meal.get('strMeal','Unknown Meal')
        category = meal.get('strCategory', 'Uncategorized')
        result.append({'name': name, 'category': category})
        
    print(f"Fetched {len(meals)} meals:")
    return result
    
def run_api_ingestion_pipeline():
    print("=" * 50)
    print("RUNNING PIPELINE")
    print("=" * 50)
    
    letters = ['a', 'b', 'c', 'd', 'e', 
               'f', 'g', 'h', 'i', 'j', 
               'k', 'l', 'm', 'n', 'o', 'p', 
               'q', 'r', 's', 't', 
               'u', 'v', 'w', 'x', 'y', 'z']
    
    total_inserted = 0
    total_failed = 0
    
    for letter in letters:
        print(f"Fetching meals starting with '{letter.upper()}'...")
        
        meals = fetch_meals(letter)
        
        if not meals:
            print(f"No meals found for '{letter}'. Skipping.")
            continue
        
        for meal in meals:
            quantity = random.randint(10, 50)  
            
            success = upsert_stock(meal['name'], meal['category'], quantity)
            
            if success:
                total_inserted += 1
                print(f"Inserted: {meal['name']} ({meal['category']}) | Qty: {quantity}")
            else:
                total_failed += 1
                print(f"Failed to insert: {meal['name']}")
        print("\n")
        
        time.sleep(APIConfig.REQUEST_DELAY)
    
    print("=" * 50)
    print(f"Successfully inserted: {total_inserted} items")
    print(f" Failed: {total_failed} items")
    print("=" * 50)

    return total_inserted > 0