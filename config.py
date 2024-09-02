# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "23089557")

API_HASH = os.environ.get("API_HASH", "4a98e047ba5b456892b5043107c0a61f")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7274144090:AAG8agPibVG_VCP70I7Cg8RXmbzTmXx7_TI") 

FORCE_SUB = os.environ.get("FORCE_SUB", "cineepiratesss") 

             # Don't Remove Credit @VJ_Botz
             # Subscribe YouTube Channel For Amazing Bot @Tech_VJ
             # Ask Doubt on telegram @KingVJ01

DB_NAME = os.environ.get("DB_NAME", "rename_pro")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://charanrajkendyala1177:Pubg1838@cluster0.k5rmybi.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://w0.peakpx.com/wallpaper/853/969/HD-wallpaper-samantha-actress-films-samantha-ruth-prabhu-telugu-movie-samantha-akkineni-telugu-actress-samanthaakkineni-bollywood-actress.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '5480645152').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
