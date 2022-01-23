import time
import asyncio
from telethon import TelegramClient, events, sync

api_id = 5693816
api_hash = 'f6d70ef073bb0edf82633a5729155d5d'

client = TelegramClient('anon', api_id, api_hash)

@client.on(events.NewMessage)
async def my_event_handler(event):
    if '!bl' in event.raw_text:
     await event.edit("no")

    elif '!hi' in event.raw_text:
        await event.edit("Salom guruhimizga hush kelibsiz")

    elif '*salom' in event.raw_text:
        await event.edit("Assalomu Alaykum hammaga")

    elif '*hayirli kech' in event.raw_text:
        await event.edit("Salom hammaga hayirli kech")

    elif '*smile' in event.raw_text:
        await event.edit("😂😂😂")

    elif '!+' in event.raw_text:
        await event.edit("+++")

    elif '!pytg' in event.raw_text:
        await event.edit("pip install pyTelegramBotApi")

    elif '*rusalomqalesiz' in event.raw_text:
        await event.edit("Привет как ты?")

    elif '*rusalomhammaga' in event.raw_text:
        await event.edit("Привет всем")

    elif '*ruqalesiz' in event.raw_text:
        await event.edit("как ты?")

    elif 'ble' in event.raw_text:
        time.sleep(1)
        await event.edit("*")
        time.sleep(1)
        await event.edit("**")
        time.sleep(1)
        await event.edit("***")

    elif 'i ble' in event.raw_text:
        time.sleep(1)
        await event.edit("i ***")

    elif '*myyear' in event.raw_text:
        await event.edit("05")

    elif '*hack' in event.raw_text:
        await event.edit("01010101010010101010010001101010")
        await event.edit("001010100100001010101010101010101")
        await event.edit("01010101010010101010010001101010")
        await event.edit("001010100100001010101010101010101")
        await event.edit("01010101010010101010010001101010")
        await event.edit("00101010100010101011110100001010")
        await event.edit("10101010101010101010101010101100")
        await event.edit("h a k i n g . . . . . . .  . . .")
        await event.edit("01010101010101010101010101010101")
        await event.edit("p a s s w o r d . . . .  ")
        await event.edit("p a s s w o r d 1| . . . ")
        await event.edit("p a s s w o r d 1 2| . . ")
        await event.edit("p a s s w o r d 1 2 3| . ")
        await event.edit("p a s s w o r d 1 2 3 4| ")
        await event.edit("p a s s w o r d Analiysing... ")
        await event.edit("p a s s w o r d Analiysing.. ")
        await event.edit("p a s s w o r d Analiysing. ")
        await event.edit("p a s s w o r d Analiysing.. ")
        await event.edit("p a s s w o r d Analiysing... ")
        await event.edit("p a s s w o r d Scanning...")
        await event.edit("p a s s w o r d Scanning..")
        await event.edit("p a s s w o r d Scanning.")
        await event.edit("p a s s w o r d Scanning..")
        await event.edit("p a s s w o r d Scanning...")
        await event.edit("p a s s w o r d Scanning..")
        await event.edit("p a s s w o r d Scanning...")
        await event.edit("00001 h000101111111111111110010101")
        await event.edit("010101 h 1010101111010000101010101")
        await event.edit("001010101 h a 01010100001000100101010")
        await event.edit("100010001010 h a c 10101010101010101010")
        await event.edit("100010001010 h a c k 10101010101010101010")
        await event.edit("100010001010 h a c k i 10101010101010101010")
        await event.edit("100010001010 h a c k i n 10101010101010101010")
        await event.edit("100010001010 h a c k i n g 10101010101010101010")

    elif '*get' in event.raw_text:
        await event.edit("getting spys id. 1%")
        await event.edit("getting spys id. 2%")
        await event.edit("getting spys id. 3%")
        await event.edit("getting spys id. 4%")
        await event.edit("getting spys id. 5%")
        await event.edit("getting spys id. 10%")
        await event.edit("getting spys id. 15%")
        await event.edit("getting spys id. 19%")
        await event.edit("getting spys id. 20%")
        await event.edit("getting spys id. 21%")
        await event.edit("getting spys id. 22%")
        await event.edit("getting spys id. 23%")
        await event.edit("getting spys id. 26%")
        await event.edit("getting spys id. 29%")
        await event.edit("getting spys id. 36%")
        await event.edit("getting spys id. 40%")
        await event.edit("getting spys id. 45%")
        await event.edit("getting spys id. 48%")
        await event.edit("getting spys id. 49%")
        await event.edit("getting spys id. 50%")
        await event.edit("getting spys id. 69%")
        await event.edit("getting spys id. 75%")
        await event.edit("getting spys id. 89%")
        await event.edit("getting spys id. 98%")
        await event.edit("getting spys id. 99%")
        await event.edit("getting spys id. 100%")
        await event.edit("error try again")

    elif '*goodnight' in event.raw_text:
        await event.edit("**Tuningiz Hayirli o'tsin**")

    elif '*id' in event.raw_text:
     try:
        # await event.edit("saom|")
        # await event.edit("sao|m")
        # await event.edit("sa|om")
        # await event.edit("sal|om")
        # await event.edit("salo|m")
        # await event.edit("salom|")
        # await event.edit("salom |")
        # await event.edit("salom")
        await event.edit("sending...")
        await event.edit("sending..")
        await event.edit("sending.")
        await event.edit("sending..")
        await event.edit("sending...")
        await event.edit("sending..")
        await event.edit("sending.")
        await event.edit("sending..")
        await event.edit("sending...")

        await client.send_file(-1001547887477, "cybersecurity.jpg", caption = "CyberSecurity")
     except:
        await event.reply("kodingizda xatolik mavjud")
        # await client.send_file(-1001547887477, "cybersecurity.jpg")

    # elif event.raw_text in event.raw_text:
    #      await event.edit("*| ")
    #      await event.edit("*>| " )
    #      await event.edit("*>_| " + event.raw_text )
    #      await event.edit("*>_ | " + event.raw_text )
    #      await event.edit("*>_ " + event.raw_text )
    #      # await event.respond(">")


    elif '*news' in event.raw_text:
        await event.edit("Scanning.")
        await event.edit("Scanning..")
        await event.edit("Scanning...")
        await event.edit("Scanning....")
        await event.edit("Scanning...")
        await event.edit("Scanning..")
        await event.edit("Scanning.")
        await event.edit("Scanning....")
        await event.edit("Scanning...")
        await event.edit("Scanning..")
        await event.edit("Scanning.")
        await event.edit("Scanning....")
        await event.edit("Scanning...")
        await event.edit("Scanning..")
        await event.edit("Scanning.")
        await event.edit("E|")
        await event.edit("Er|")
        await event.edit("Err|")
        await event.edit("Erro|")
        await event.edit("Error|")
        await event.edit("Error!|")
        await event.edit("Error! >_ |")
        await event.edit("Error!")
        await event.client.get_entity(event.from_id)

    elif '*10' in event.raw_text:
        await event.edit("[ =>                ] 1%")
        await event.edit("[ ===>              ] 3%")
        await event.edit("[ =====>            ] 5%")
        await event.edit("[ ==========>       ] 10%")
        # await event.edit("[ =>            ]")
        # await event.edit("[ =>            ]")

    elif '*nosorry' in event.raw_text:
        await event.edit(">_ no s_")
        await event.edit(">_ no so_")
        await event.edit(">_ no sor_")
        await event.edit(">_ no sorr_")
        await event.edit(">_ no sorry_")
        await event.edit(">_ ")
        await event.edit(">_|")
        await event.edit(">|")
        await event.edit("|")
        await event.edit("i writed sorry bro")

    elif '*id' in event.raw_text:
        await event.client.get_entity(event.from_id)

    elif '*myname' in event.raw_text:
        await event.edit(">_ ib_")
        await event.edit(">_ ibr_")
        await event.edit(">_ ibro_")
        await event.edit(">_ ibroh_")
        await event.edit(">_ ibrohi_")
        await event.edit(">_ ibrohim_")
        await event.edit("ibrohim")
    elif event.raw_text in event.raw_text:
        await event.edit(">")
        await event.edit(">>")
        await event.edit(">>>")
        await event.edit(">>")
        await event.edit(">")
#         await event.edit(">>")
#         await event.edit(">>>")
#         await event.edit(">>")
#         await event.edit(">>>")
#         await event.edit(">")
        await event.edit(">_ ")
        await event.edit(">")
        await event.edit("_")
        time.sleep(1)
        await event.edit(event.raw_text)

    # elif event.raw_text in event.raw_text:
    #     await event.edit("Data, time.. : "+time.asctime()+"]\n\nMy message: " + event.raw_text )




client.start()
client.run_until_disconnected()

