import discord
import requests
from bs4 import BeautifulSoup


def read_token():
    with open('token.txt', 'r') as f:
        lines = f.readlines()
        return lines[0].strip()


token = read_token()

client = discord.Client()


@client.event
async def on_server_join(member):
    server = member.server
    default_channel = server.default_channel
    message = f"""welcome {member.mention}"""
    await client.send_message(default_channel, message)


@client.event
async def on_message(message):
    id_guild = client.get_guild('750242281105391746')
    channels = ['general', 'testchannel']
    if str(message.channel) in channels:
        if message.content.find('!Hello') != -1:
            await message.channel.send(f"""{message.author} typed hello""")
        elif message.content == '!members':
            total_member = len(message.guild.members)
            await message.channel.send(total_member)
        elif message.content == '!leaderboard':
            mes = 'Pls specify which branch you are looking for. for eg: !leaderboard-eng,!leaderboard-arch,!leaderboard-med,!leaderboard-law,!leaderboard-MBA \n source:https://aglasem.com/top-engineering-colleges-in-india/'
            await message.channel.send(mes)
        elif message.content == '!branches':
            mes = 'All Branches :- Architecture,Engineering,Medical,law,MBA,'
            await message.channel.send(mes)
        elif message.content == '!leaderboard-eng':
            s = requests.get('https://aglasem.com/top-engineering-colleges-in-india/')
            soup = BeautifulSoup(s.content, 'html5lib')
            a = soup.find('table')
            y = []
            h = {}
            z = []
            for i in range(1, 200):
                b = a.find_all('tr')[i]
                rank = b.find_all('td')[0].getText()
                college = b.find_all('td')[1].getText()
                state = b.find_all('td')[3].getText()
                da = [college]
                db = [rank]
                dc = [state]
                y = y + db + da + dc
            print(y, end='')
            for n in range(0,60,3):
                z =  y[n]+' , '+y[n+1]+' , '+y[n+2]
                await message.channel.send(z)
        elif message.content == '!leaderboard-arch':
            s = requests.get('https://aglasem.com/top-architecture-colleges-in-india/')
            soup = BeautifulSoup(s.content, 'html5lib')
            a = soup.find('table')
            y = []
            h = {}
            for i in range(1, 20):
                b = a.find_all('tr')[i]
                rank = b.find_all('td')[0].getText()
                college = b.find_all('td')[1].getText()
                state = b.find_all('td')[3].getText()
                da = [college]
                db = [rank]
                dc = [state]
                y = y + db + da + dc
            print(y, end='')
            for n in range(0, 60, 3):
                z = y[n] + ' , ' + y[n + 1] + ' , ' + y[n + 2]
                await message.channel.send(z)
        elif message.content == '!leaderboard-med':
            s = requests.get('https://aglasem.com/top-medical-colleges-in-india/')
            soup = BeautifulSoup(s.content, 'html5lib')
            a = soup.find('table')
            y = []
            h = {}
            for i in range(1, 40):
                b = a.find_all('tr')[i]
                rank = b.find_all('td')[0].getText()
                college = b.find_all('td')[1].getText()
                state = b.find_all('td')[3].getText()
                da = [college]
                db = [rank]
                dc = [state]
                y = y + db + da + dc
            print(y, end='')
            for n in range(0, 60, 3):
                z = y[n] + ' , ' + y[n + 1] + ' , ' + y[n + 2]
                await message.channel.send(z)
        elif message.content == '!leaderboard-MBA':
            s = requests.get('https://aglasem.com/top-mba-colleges-in-india/')
            soup = BeautifulSoup(s.content, 'html5lib')
            a = soup.find('table')
            y = []
            h = {}
            for i in range(1, 75):
                b = a.find_all('tr')[i]
                rank = b.find_all('td')[0].getText()
                college = b.find_all('td')[1].getText()
                state = b.find_all('td')[3].getText()
                da = [college]
                db = [rank]
                dc = [state]
                y = y + db + da + dc
            print(y, end='')
            for n in range(0, 60, 3):
                z = y[n] + ' , ' + y[n + 1] + ' , ' + y[n + 2]
                await message.channel.send(z)
        elif message.content == '!leaderboard-law':
            s = requests.get('https://aglasem.com/top-law-colleges-in-india/')
            soup = BeautifulSoup(s.content, 'html5lib')
            a = soup.find('table')
            y = []
            h = {}
            for i in range(1, 20):
                b = a.find_all('tr')[i]
                rank = b.find_all('td')[0].getText()
                college = b.find_all('td')[1].getText()
                state = b.find_all('td')[3].getText()
                da = [college]
                db = [rank]
                dc = [state]
                y = y + db + da + dc
            print(y, end='')
            for n in range(0, 60, 3):
                z = y[n] + ' , ' + y[n + 1] + ' , ' + y[n + 2]
                await message.channel.send(z)
        elif message.content == '!decidemycareer':
            mes = 'You will be provided with some questions and and some options. You have to select the option which you feel is best suited for you.' \
                  'Each option has different points you have to sum up all the point and reply with !ans-<your added points> for eg: !ans-20. ''To start the quiz type !startquiz'
            await message.channel.send(mes)
        elif message.content == '!startquiz':
            mes1 = """1. You are held in a room and there is a camera, lock, computer, bookshelf, screwdriver and
            furniture. Would you……\n
            a) hack into computer and try to send a message to the outside world for help(1)
            b) pick the lock with the screw driver (3)
            c) wait for people to come and negotiate with them (5)
            d) panic and cry in the corner (6)
            e) remain calm and accept reality (4)
            f) build an awesome tool to kill the people who trapped you and then escape (2)"""
            mes2 = """ \n2. Which character would best describe you?
            a) helpful and caring (3)
            b) responsible and hardworking (1)
            c) law and order (5)
            d) sneaky (6)
            e) comedic and popular (4)
            f) frequent mood swings (2)\n"""
            mes3 = """\n3. How would you spend your vacation?
            a) make new projects on your computer or with your tools (1)
            b) watch movies and listen to songs (6)
            c) chat with your friends 24/7 (4)
            d) read a book or write a book (3)
            e) read research books and watch national geographic (2)
            f) draw, paint, culinary arts, do it yourself projects (5)\n"""
            inf = """type !nextquiz for the next page of quiz.\nYou will be provided with some questions and and some options. You have to select the option which you feel is best suited for you.\n
                  Each option has different points you have to sum up all the point and reply with !ans-<your added points> \nfor eg: !ans-20. To start the quiz type !startquiz"""

            mes = mes1 + mes2 + mes3 + inf
            await message.channel.send(mes)
        elif message.content == '!nextquiz':
            mes4 = """\n4. What is your favorite workspace?
            a) in a closed room away from people (6)
            b) a public area (4)
            c) in front of a computer (1)
            d) in an office (2)
            e) in a classroom or library (3)
            f) in a field surrounded by nature (5)\n"""

            mes5 = """\n5. You are late for a meeting but you are held in traffic. Would you......
            a) wait patiently and hope that your boss is caught in the traffic as well (4)
            b) get frustrated and shout at the people nearby (6)
            c) get out of the car and try to find the reason for the traffic (5)
            d) make a video call and attend the meeting in your car (1)
            e) make use of your time to get finished with some work (2)
            f) write an article on the lame traffic regulating systems (3)\n"""

            mes6 = """\n6. You notice a person with corona like symptoms. Would you……
            a) call a health inspector (4)
            b) advise the person to stay at home (1)
            c) run for your life (6)
            d) tell others to stay away from the person without letting the person know (3)
            e) mind your own business (5)
            f) wear 5 masks together so that the person would get a hint (2)\n"""

            mes7 = """\n7. What is your productive time of the day?
            a) midnight (12AM-4AM) (1)
            b) dawn (5AM-9AM) (2)
            c) afternnon (1PM-4PM) (5)
            d) evening (5PM-8PM) (4)
            e) mid-morning (9AM-1PM) (3)
            f) night (8PM-11PM) (6)\n"""
            inf = """type !nextquiz2 for the next page of quiz.\nYou will be provided with some questions and and some options. You have to select the option which you feel is best suited for you.\n
                  Each option has different points you have to sum up all the point and reply with !ans-<your added points> \nfor eg: !ans-20. To start the quiz type !startquiz"""

            mes = mes4 + mes5 + mes6 + mes7 + inf
            await message.channel.send(mes)
        elif message.content == '!nextquiz2':
            mes8 = """\n8. What is your dream goal?
            a) travel the world (6)
            b) make a difference in the society (2)
            c) learn everything that the world has to offer (3)
            d) invent/create something cool (1)
            e) help to improve the law (5)
            f) entertain others and become worldwide famous (4)\n"""
            mes9 = """\n9. What type of games would you prefer?
            a) coding and programming, construction, etc. games (1)
            b) karaoke, damsharades games (4)
            c) looking after a farm, home, etc. games (6)
            d) helping the sick, animals, etc. games (3)
            e) maths and logical games (2)
            f) war games (5)\n"""
            mes10 = """\n10.What qualities do you except from your job?
            a) interact with people(3)
            b) invent / create new things (1)
            c) creating world peace (6)
            d) bringing awareness (5)
            e) gain knowledge at every step (2)
            f) being known by everyone (4)\n"""
            inf = "type !<yoursum> for your suggested career path for eg: !20"
            mes = mes8 + mes9 + mes10 + inf
            await message.channel.send(mes)
        elif message.content == '!10':
            mes = """\nScience and technology is a diverse career field that generally involves scientific research and
                    the development of innovative technologies that benefit humanity\n.\n
                    Scientific professions often involved some degree of mathematics or computer science
                    knowledge\n.
                    \nThese professions all belong to this career field:\n
                    * \nArcheologist
                    * \nSoftware engineer
                    * \nLaboratory technician
                    * \nMicrobiologist
                    * \nPhysicist"""
            await message.channel.send(mes)
        elif message.content == '!11':
            mes = """\nScience and technology is a diverse career field that generally involves scientific research and
                    the development of innovative technologies that benefit humanity\n.
                    \nScientific professions often involved some degree of mathematics or computer science
                    knowledge\n.
                    These professions all belong to this career field:
                    * Archeologist
                    * Software engineer
                    * Laboratory technician
                    * Microbiologist
                    * Physicist"""
            await message.channel.send(mes)
        elif message.content == '!12':
            mes = """Science and technology is a diverse career field that generally involves scientific research and
                    the development of innovative technologies that benefit humanity.
                    Scientific professions often involved some degree of mathematics or computer science
                    knowledge.
                    These professions all belong to this career field:
                    * Archeologist
                    * Software engineer
                    * Laboratory technician
                    * Microbiologist
                    * Physicist"""
            await message.channel.send(mes)
        elif message.content == '!13':
            mes = """Science and technology is a diverse career field that generally involves scientific research and
                    the development of innovative technologies that benefit humanity.
                    Scientific professions often involved some degree of mathematics or computer science
                    knowledge.
                    These professions all belong to this career field:
                    * Archeologist
                    * Software engineer
                    * Laboratory technician
                    * Microbiologist
                    * Physicist"""
            await message.channel.send(mes)
        elif message.content == '!14':
            mes = """"2. Architecture and engineering (14-17)
                        People in the architecture and planning fields are responsible for designing new structures or
                        creating aesthetically pleasing, practical and structurally sound environments. Many positions
                        require an undergraduate or graduate degree. Jobs in this field include:
                        * Architect
                        * Civil engineer
                        * Landscape architect
                        * Sustainable designer
                        * Biomedical engineer"""
            await message.channel.send(mes)
        elif message.content == '!15':
            mes = """"2. Architecture and engineering (14-17)
                        People in the architecture and planning fields are responsible for designing new structures or
                        creating aesthetically pleasing, practical and structurally sound environments. Many positions
                        require an undergraduate or graduate degree. Jobs in this field include:
                        * Architect
                        * Civil engineer
                        * Landscape architect
                        * Sustainable designer
                        * Biomedical engineer"""
            await message.channel.send(mes)
        elif message.content == '!16':
            mes = """"2. Architecture and engineering (14-17)
                        People in the architecture and planning fields are responsible for designing new structures or
                        creating aesthetically pleasing, practical and structurally sound environments. Many positions
                        require an undergraduate or graduate degree. Jobs in this field include:
                        * Architect
                        * Civil engineer
                        * Landscape architect
                        * Sustainable designer
                        * Biomedical engineer"""
            await message.channel.send(mes)
        elif message.content == '!17':
            mes = """"2. Architecture and engineering (14-17)
                        People in the architecture and planning fields are responsible for designing new structures or
                        creating aesthetically pleasing, practical and structurally sound environments. Many positions
                        require an undergraduate or graduate degree. Jobs in this field include:
                        * Architect
                        * Civil engineer
                        * Landscape architect
                        * Sustainable designer
                        * Biomedical engineer"""
            await message.channel.send(mes)
        elif message.content == '!26':
            mes = """ Business, management and administration (26-29)
                        The business, management and administration career fields are best for business-minded
                        individuals with a penchant for communication. They work to execute various processes
                        necessary for the functioning of businesses. It usually involves working in an office environment.
                        Here are some of the positions in this field:
                        * Human resources manager
                        * Marketing assistant
                        * Accountants
                        * Secretary
                        * Entrepreneur/small business owner
                        * Real estate agent
                        * Business development manager"""
            await message.channel.send(mes)
        elif message.content == '!27':
            mes = """ Business, management and administration (26-29)
                        The business, management and administration career fields are best for business-minded
                        individuals with a penchant for communication. They work to execute various processes
                        necessary for the functioning of businesses. It usually involves working in an office environment.
                        Here are some of the positions in this field:
                        * Human resources manager
                        * Marketing assistant
                        * Accountants
                        * Secretary
                        * Entrepreneur/small business owner
                        * Real estate agent
                        * Business development manager"""
            await message.channel.send(mes)
        elif message.content == '!28':
            mes = """ Business, management and administration (26-29)
                        The business, management and administration career fields are best for business-minded
                        individuals with a penchant for communication. They work to execute various processes
                        necessary for the functioning of businesses. It usually involves working in an office environment.
                        Here are some of the positions in this field:
                        * Human resources manager
                        * Marketing assistant
                        * Accountants
                        * Secretary
                        * Entrepreneur/small business owner
                        * Real estate agent
                        * Business development manager"""
            await message.channel.send(mes)
        elif message.content == '!29':
            mes = """ Business, management and administration (26-29)
                        The business, management and administration career fields are best for business-minded
                        individuals with a penchant for communication. They work to execute various processes
                        necessary for the functioning of businesses. It usually involves working in an office environment.
                        Here are some of the positions in this field:
                        * Human resources manager
                        * Marketing assistant
                        * Accountants
                        * Secretary
                        * Entrepreneur/small business owner
                        * Real estate agent
                        * Business development manager"""
            await message.channel.send(mes)
        elif message.content == '!30':
            mes = """ 6. Health and medicine (30-33)
                        This career profession involves healthcare services that provide care for people. They are an
                        essential part of our society. This professional field often requires specialized training and
                        certification.
                        Here are some examples of professions in health and medicine:
                        * Anesthesiologist
                        * Dental assistant
                        * Nurse
                        * Veterinarian
                        * Physical therapist"""
            await message.channel.send(mes)
        elif message.content == '!31':
            mes = """ 6. Health and medicine (30-33)
                        This career profession involves healthcare services that provide care for people. They are an
                        essential part of our society. This professional field often requires specialized training and
                        certification.
                        Here are some examples of professions in health and medicine:
                        * Anesthesiologist
                        * Dental assistant
                        * Nurse
                        * Veterinarian
                        * Physical therapist"""
            await message.channel.send(mes)
        elif message.content == '!32':
            mes = """ 6. Health and medicine (30-33)
                        This career profession involves healthcare services that provide care for people. They are an
                        essential part of our society. This professional field often requires specialized training and
                        certification.
                        Here are some examples of professions in health and medicine:
                        * Anesthesiologist
                        * Dental assistant
                        * Nurse
                        * Veterinarian
                        * Physical therapist"""
            await message.channel.send(mes)
        elif message.content == '!30':
            mes = """ 6. Health and medicine (30-33)
                            This career profession involves healthcare services that provide care for people. They are an
                            essential part of our society. This professional field often requires specialized training and
                            certification.
                            Here are some examples of professions in health and medicine:
                            * Anesthesiologist
                            * Dental assistant
                            * Nurse
                            * Veterinarian
                            * Physical therapist"""
            await message.channel.send(mes)
        elif message.content == '!38':
            mes = """The education field is dedicated to the art of skillfully disseminating knowledge and information
                    to people. The most obvious job in this field are teachers, but it is not just limited to teaching.
                    There are also management, administrative and board member jobs, for example.
                    Here are some jobs you can find in this field:
                    * Special education teacher
                    * School principal
                    * Superintendent
                    * College professor
                    * School librarian
                    * Substitute teacher"""
            await message.channel.send(mes)
        elif message.content == '!39':
            mes = """The education field is dedicated to the art of skillfully disseminating knowledge and information
                    to people. The most obvious job in this field are teachers, but it is not just limited to teaching.
                    There are also management, administrative and board member jobs, for example.
                    Here are some jobs you can find in this field:
                    * Special education teacher
                    * School principal
                    * Superintendent
                    * College professor
                    * School librarian
                    * Substitute teacher"""
            await message.channel.send(mes)
        elif message.content == '!40':
            mes = """The education field is dedicated to the art of skillfully disseminating knowledge and information
                    to people. The most obvious job in this field are teachers, but it is not just limited to teaching.
                    There are also management, administrative and board member jobs, for example.
                    Here are some jobs you can find in this field:
                    * Special education teacher
                    * School principal
                    * Superintendent
                    * College professor
                    * School librarian
                    * Substitute teacher"""
            await message.channel.send(mes)
        elif message.content == '!41':
            mes = """The education field is dedicated to the art of skillfully disseminating knowledge and information
                    to people. The most obvious job in this field are teachers, but it is not just limited to teaching.
                    There are also management, administrative and board member jobs, for example.
                    Here are some jobs you can find in this field:
                    * Special education teacher
                    * School principal
                    * Superintendent
                    * College professor
                    * School librarian
                    * Substitute teacher"""
            await message.channel.send(mes)
        elif message.content == '!46':
            mes = """Arts, culture and entertainment (46-49)
                    This career field is dedicated to enriching people's lives through culture and the sharing of arts
                    and self-expression. There are formal educational programs for these fields, but these careers
                    also include self-taught people who have natural talent. Some jobs in this field include:
                    * Singer/songwriter
                    * Music producer
                    * Art curator
                    * Animator/video game designer
                    * Filmmaker
                    * Graphic designer
                    * Fashion designe"""
            await message.channel.send(mes)
        elif message.content == '!47':
            mes = """Arts, culture and entertainment (46-49)
                    This career field is dedicated to enriching people's lives through culture and the sharing of arts
                    and self-expression. There are formal educational programs for these fields, but these careers
                    also include self-taught people who have natural talent. Some jobs in this field include:
                    * Singer/songwriter
                    * Music producer
                    * Art curator
                    * Animator/video game designer
                    * Filmmaker
                    * Graphic designer
                    * Fashion designe"""
            await message.channel.send(mes)
        elif message.content == '!48':
            mes = """Arts, culture and entertainment (46-49)
                    This career field is dedicated to enriching people's lives through culture and the sharing of arts
                    and self-expression. There are formal educational programs for these fields, but these careers
                    also include self-taught people who have natural talent. Some jobs in this field include:
                    * Singer/songwriter
                    * Music producer
                    * Art curator
                    * Animator/video game designer
                    * Filmmaker
                    * Graphic designer
                    * Fashion designe"""
            await message.channel.send(mes)
        elif message.content == '!49':
            mes = """Arts, culture and entertainment (46-49)
                    This career field is dedicated to enriching people's lives through culture and the sharing of arts
                    and self-expression. There are formal educational programs for these fields, but these careers
                    also include self-taught people who have natural talent. Some jobs in this field include:
                    * Singer/songwriter
                    * Music producer
                    * Art curator
                    * Animator/video game designer
                    * Filmmaker
                    * Graphic designer
                    * Fashion designe"""
            await message.channel.send(mes)
        elif message.content == '!50':
            mes = """Law and public policy (50-53)
                    Within the law and public policy field, the variety of occupations include criminal justice, public
                    policy advocacy and political lobbying. This career field comprises all the employment sectors.
                    You can find a job in government, nonprofit, thinktanks and large for-profit companies.
                    Here are some jobs in this career field:
                    * Lobbyist
                    * Public administrator
                    * Paralegal
                    * Lawyer
                    * Labor relations specialist
                    * FBI
                    * forensics"""
            await message.channel.send(mes)
        elif message.content == '!51':
            mes = """Law and public policy (50-53)
                    Within the law and public policy field, the variety of occupations include criminal justice, public
                    policy advocacy and political lobbying. This career field comprises all the employment sectors.
                    You can find a job in government, nonprofit, thinktanks and large for-profit companies.
                    Here are some jobs in this career field:
                    * Lobbyist
                    * Public administrator
                    * Paralegal
                    * Lawyer
                    * Labor relations specialist
                    * FBI
                    * forensics"""
            await message.channel.send(mes)
        elif message.content == '!52':
            mes = """Law and public policy (50-53)
                    Within the law and public policy field, the variety of occupations include criminal justice, public
                    policy advocacy and political lobbying. This career field comprises all the employment sectors.
                    You can find a job in government, nonprofit, thinktanks and large for-profit companies.
                    Here are some jobs in this career field:
                    * Lobbyist
                    * Public administrator
                    * Paralegal
                    * Lawyer
                    * Labor relations specialist
                    * FBI
                    * forensics"""
            await message.channel.send(mes)
        elif message.content == '!53':
            mes = """Law and public policy (50-53)
                    Within the law and public policy field, the variety of occupations include criminal justice, public
                    policy advocacy and political lobbying. This career field comprises all the employment sectors.
                    You can find a job in government, nonprofit, thinktanks and large for-profit companies.
                    Here are some jobs in this career field:
                    * Lobbyist
                    * Public administrator
                    * Paralegal
                    * Lawyer
                    * Labor relations specialist
                    * FBI
                    * forensics"""
            await message.channel.send(mes)
        elif message.content == '!54':
            mes = """NDA (54-57)
                    Choosing a career path in NDA involves working in dire situations and constantly looking after
                    each other’s back. People require the ability to risk their own life for the well-being of their
                    country. This field is fitness-oriented and requires great general knowledge.
                    Jobs in this career field include:
                    * Army"""
            await message.channel.send(mes)
        elif message.content == '!55':
            mes = """NDA (54-57)
                    Choosing a career path in NDA involves working in dire situations and constantly looking after
                    each other’s back. People require the ability to risk their own life for the well-being of their
                    country. This field is fitness-oriented and requires great general knowledge.
                    Jobs in this career field include:
                    * Army"""
            await message.channel.send(mes)
        elif message.content == '!56':
            mes = """NDA (54-57)
                    Choosing a career path in NDA involves working in dire situations and constantly looking after
                    each other’s back. People require the ability to risk their own life for the well-being of their
                    country. This field is fitness-oriented and requires great general knowledge.
                    Jobs in this career field include:
                    * Army"""
            await message.channel.send(mes)
        elif message.content == '!57':
            mes = """NDA (54-57)
                    Choosing a career path in NDA involves working in dire situations and constantly looking after
                    each other’s back. People require the ability to risk their own life for the well-being of their
                    country. This field is fitness-oriented and requires great general knowledge.
                    Jobs in this career field include:
                    * Army"""
            await message.channel.send(mes)
        elif message.content == '!cutoff':
            r = requests.get('https://cutoffs.aglasem.com/page/1')
            s = BeautifulSoup(r.content, 'html5lib')
            jc = s.find(class_="jeg_posts jeg_load_more_flag")
            for i in range(0, len(jc) - 2):
                tot = """\nHaldia Institute of Pharmacy Cut Off – Check Here https://cutoffs.aglasem.com/170516\n
                        \nTechno International Batanagar Cut Off – Check Here https://cutoffs.aglasem.com/153508\n
                        \nIdeal Institute of Engineering Cut Off https://cutoffs.aglasem.com/978\n
                        \nBengal College of Engineering & Technology, Durgapur Cut Off – Check Herehttps://cutoffs.aglasem.com/170515\n
                        \nHeritage Institute of Technology Cut Off https://cutoffs.aglasem.com/956\n
                        \nHooghly Engineering and Technology College Cut Off https://cutoffs.aglasem.com/977\n
                        \nGhani Khan Choudhury Institute of Engineering & Technology Cut Off – Check Here https://cutoffs.aglasem.com/170511\n
                        \nHaldia Institute of Technology Cut Off https://cutoffs.aglasem.com/955\n
                        \nRamkrishna Mahato Government Engineering College Cut Off – Check Here https://cutoffs.aglasem.com/170503\n
                        \nGuru Nanak Institute of Technology Cut Off https://cutoffs.aglasem.com/954\n
                        \n source:https://cutoffs.aglasem.com\n
                        """
                print(tot)
            await message.channel.send(tot)
        elif message.content == '!syllabus':
            mes = """\nIIT JEE Main Mathematics Syllabus - https://www.successcds.net/examsyllabus/iit-jee-mathematics-syllabus/1031/\n
                    \nIIT JEE Main Chemistry Syllabus - https://www.successcds.net/examsyllabus/iit-jee-chemistry-syllabus/1029/\n
                    \nGATE Syllabus 2020 for Statistics – GATE Exam Syllabus - https://www.successcds.net/examsyllabus/gate-syllabus-for-statistics/103617/\n
                    \nGATE Syllabus 2020 for Biomedical Engineering – GATE Exam Syllabus - https://www.successcds.net/examsyllabus/gate-syllabus-for-biomedical-engineering/103620/\n
                    \nAll India Bar Examination (AIBE) Syllabus 2019 - https://www.successcds.net/examsyllabus/aibe-syllabus/103592/\n
                    \nB.Pharm Entrance Exam Syllabus - https://www.successcds.net/examsyllabus/bpharm-entrance-exam-syllabus/103580/\n
                    \nFTII Entrance Exam Syllabus - https://www.successcds.net/examsyllabus/ftii-entrance-exam-syllabus/103575/\n
                    \nAPTET Syllabus 2019 Andhra Pradesh Teacher Eligibility Test - https://www.successcds.net/examsyllabus/andhra-pradesh-tet-syllabus/103376/\n
                    \n type !syllabus2 for next page
                    \n source:https://www.successcds.net/examsyllabus/iit-jee-mathematics-syllabus\n"""
            await message.channel.send(mes)
        elif message.content == '!syllabus2':
            mes = """\nB.Ed. Entrance Exam Syllabus 2019 - https://www.successcds.net/examsyllabus/b-ed-entrance-exam-syllabus-2019/103226/\n
                        \nRevised syllabus and scheme for UPSC Mains Geology released - https://www.successcds.net/examsyllabus/revised-syllabus-and-scheme-for-upsc-mains-geology-released/103214/\n
                        \nAnna University MBA Syllabus - https://www.successcds.net/examsyllabus/anna-university-mba-syllabus/103190/\n
                        \nJIPMER MBBS 2019 Syllabus - https://www.successcds.net/examsyllabus/jipmer-mbbs-syllabus/102004/\n
                        \nWBJEEM Biological Science Syllabus - https://www.successcds.net/examsyllabus/wbjeem-biological-science-syllabus/101992/\n
                        \nWBJEEM Mathematics Syllabus - https://www.successcds.net/examsyllabus/wbjeem-mathematics-syllabus/101990/\n
                        \nWBJEEM Physics Syllabus - https://www.successcds.net/examsyllabus/wbjeem-physics-syllabus/101988/\n
                        \nWBJEEM Chemistry Syllabus - https://www.successcds.net/examsyllabus/wbjeem-chemistry-syllabus/101984/\n
                        \nRBI Officers Recruitment Examination – Exam Syllabus - https://www.successcds.net/examsyllabus/rbi-officers-recruitment-examination-exam-syllabus/101952/\n
                        \nCTET 2019 Exam syllabus - https://www.successcds.net/examsyllabus/syllabus-of-ctet-2011-for-class-vi-%E2%80%93-viii-teacher/101224/\n
                        \nGJU Hissar BBA Distance Education Syllabus and Exam Scheme - https://www.successcds.net/examsyllabus/gju-hissar-bba-distance-education-syllabus-exam-scheme/101361/\n
                        \nAIMS Test for Management Admissions (ATMA) Syllabus - https://www.successcds.net/examsyllabus/aims-test-for-management-admissions-atma-syllabus/101341/\n
                        \n type !syllabus3 for next page\n
                        \n source:https://www.successcds.net/examsyllabus/iit-jee-mathematics-syllabus\n"""
            await message.channel.send(mes)
        elif message.content == '!syllabus3':
            mes = """\nBBA Entrance Exam Syllabus | Syllabus for BBA Admission Test - https://www.successcds.net/examsyllabus/bba-entrance-exam-syllabus/101316/\n
                    \nMat Entrance Exam Syllabus 2019 | MAT Exam Test Syllabus 2019 - https://www.successcds.net/examsyllabus/mat-entrance-exam-syllabus-2013-mat-exam-test-syllabus-2013/101291/\n
                    \nIBPS CWE Exam Syllabus - https://www.successcds.net/examsyllabus/ibps-cwe-exam-syllabus/101274/\n
                    \nIBPS PO Exam Syllabus - https://www.successcds.net/examsyllabus/ibps-po-exam-syllabus/101255/\n
                    \nCSIR UGC NET Engineering Sciences Syllabus - https://www.successcds.net/examsyllabus/csir-ugc-net-engineering-sciences-syllabus/101232/\n
                    \nCentral Teacher Eligibility Test CTET  Syllabus for Class I-V Teacher Selection - https://www.successcds.net/examsyllabus/syllabus-of-ctet-2011-for-class-i-v-teacher/101217/\n
                    \nCentral Teacher Eligibility Test CTET  Syllabus for Class VI to VIII Teacher Selection - https://www.successcds.net/examsyllabus/syllabus-of-ctet-2011-for-class-vi-%E2%80%93-viii-teacher/101224/\n
                    \nJNU M.Tech Biotechnology Exam Syllabus - https://www.successcds.net/examsyllabus/syllabus-for-jnu-m-tech-biotechnology/101211/\n
                    \nJNU M.Sc Biotechnology Exam Syllabus - https://www.successcds.net/examsyllabus/syllabus-for-jnu-msc-biotechnology/101207/\n
                    \nKLE UGAIET  Syllabus - https://www.successcds.net/examsyllabus/kle-ugaiet-syllabus/101198/\n
                    \n type !syllabus4 for next page\n
                    \n source:https://www.successcds.net/examsyllabus/iit-jee-mathematics-syllabus\n"""
            await message.channel.send(mes)
        elif message.content == '!syllabus4':
            mes = """\nGPAT 2019 – Graduate Pharmacy Aptitude Test Syllabus - https://www.successcds.net/examsyllabus/syllabus-for-gpat-2010-examination/101080/\n
                    \nNEST  2019 Syllabus- https://www.successcds.net/examsyllabus/national-entrance-screening-test-syllabus/101052/\n
                     \nKIITEE M.Sc Biotechnology Exam Syllabus - https://www.successcds.net/examsyllabus/syllabus-for-kiitee-msc-biotechnology-exam/101188/\n
                    \nKIITEE MCA Entrance Exam Syllabus - https://www.successcds.net/examsyllabus/syllabus-for-kiitee-mca-programme/101184/\n
                    \nKIITEE B.Tech Entrance Exam Syllabus - https://www.successcds.net/examsyllabus/kiitee-b-tech-entrance-exam-syllabus/101170/\n
                    \nKerala KEAM  2019 Entrance Exam Syllabus- https://www.successcds.net/examsyllabus/keam-entrance-exam-syllabus/10944/\n
                    \nWest Bengal JEE 2019 Entrance Exam Syllabus- https://www.successcds.net/examsyllabus/west-bengal-jem-entrance-exam-syllabus/10649/\n
                    \nVITEEE  Entrance Exam Syllabus- https://www.successcds.net/examsyllabus/viteee-entrance-exam-syllabus/10633/\n
                    \nIIT Joint Entrance Exam (JEE) Syllabus  - https://www.successcds.net/examsyllabus/iit-joint-entrance-exam-jee-syllabus/1026/\n
                    \nCA CPT Exam Syllabus - https://www.successcds.net/CA-CPT/CA-CPT-Syllabus.php\n
                    \n source:https://www.successcds.net/examsyllabus/iit-jee-mathematics-syllabus\n"""
            await message.channel.send(mes)
        elif message.content == '!updates':
            r = requests.get('https://aglasem.com/category/entrance-exams/page/1')
            s = BeautifulSoup(r.content, 'html5lib')
            j = s.find(class_="jeg_posts jeg_load_more_flag")
            y = []
            for i in range(0, len(j) - 2):
                v = j.find_all('article')[i]
                title = v.find('div', class_="jeg_postblock_content").find('h3').find('a').getText()
                link = v.find('div', class_="jeg_postblock_content").find('h3').find('a')['href']
                desc = v.find('div', class_="jeg_post_excerpt").find('p').getText()
                da = [title]
                db = [link]
                dc = [desc]
                y = y + db + da + dc
            print(y, end='\n')
            for n in range(60):
                await message.channel.send(y[n])
        elif message.content == '!sources':
            mes = """https://aglasem.com/top-engineering-colleges-in-india/\nhttps://cutoffs.aglasem.com/\nhttps://www.successcds.net/examsyllabus/iit-jee-mathematics-syllabus/\nhttps://aglasem.com/category/entrance-exams/page/"""
            await message.channel.send(mes)
        elif message.content == '!contact':
            mes = """If there is a trouble with the bot or any queries\nYou can contact us through: \nneoblaze24@gmail.com\nsanchitjain200327@gmail.com\njacobtheresa01@gmail.com\n"""
            await message.channel.send(mes)
        elif message.content == '!commands':
            mes = """Available Commands:\n!leaderboard\n!decidemycareer\n!cutoff\n!updates\n!syllabus\n!contact\n!sources\n"""
            await message.channel.send(mes)
    else:
        print(f"""{message.author} typed {message.content}""")


client.run(token)
