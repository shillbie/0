# -*- coding: utf-8 -*-
# Tolong jangan ubah mid creator || Hargai saya
import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time, random, sys, ast, re, os, io, json, subprocess, threading, string, codecs, requests, ctypes, urllib, urllib2, urllib3, wikipedia, tempfile
from bs4 import BeautifulSoup
from urllib import urlopen
import requests
from io import StringIO
from threading import Thread
#from gtts import gTTS
from googletrans import Translator

cl = LINETCR.LINE()
cl.login(token="Eo9FIOMpDW2ajNLXJzvb.w6+8YbOkbOMyiHAGbC+hcW.+cg2i+bnzkLG0nq0zFsYGwxSdoK3K/Pfyq0DZNj4BDk=")
cl.loginResult()

ki = LINETCR.LINE() # Assist
ki.login(token="Eo45jLYHE6nHXz3NT3Ad.qcJOSgzQEpbuah+2LTD5Bq.dFnOMmTxdMFrTG47zWH9ABYIUdPw1RKgtLGNU4PuGUk=")
ki.loginResult()

print "===[Login Success]==="
mulai = time.time()
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage ="""
          💥Ｓモㄥ下   乃口匕💥
🌀▂▃▅▇█▓▒░۩M͓̽E͓̽N͓̽U͓̽۩░▒▓█▇▅▃▂🌀      
🔘⚔ Creator ⚔
🔘⚔ Gcreator ⚔
🔘⚔ List group: ⚔
🔘⚔ Leave group: ⚔
🔘⚔ Cancel ⚔
🔘⚔ Url:on/off ⚔
🔘⚔ Autojoin:on/off ⚔
🔘⚔ Autocancel:on/off ⚔
🔘⚔ Qr:on/off ⚔
🔘⚔ Autokick:on/off ⚔
🔘⚔ Contact:on/off ⚔
🔘⚔ Gift1-3 ⚔
🔘⚔ Tag all/Mention all⚔
🔘⚔ Bintit /Tan⚔      
🔘⚔ Boom  @ ⚔
🔘⚔ Add all ⚔
🔘⚔ Recover ⚔
🔘⚔ Remove all chat ⚔
🔘⚔ Gn: [ name ] ⚔
🔘⚔ Kick: [ mid ] ⚔
🔘⚔ Invite: [ mid ] ⚔
🔘⚔ Welcome ⚔
🔘⚔ Bc: [ text ] ⚔
🔘⚔ Cancelall ⚔ 
🔘⚔ Gurl ⚔
🔘⚔ Self Like ⚔
🔘⚔ Speedbot ⚔
🔘⚔ Ban ⚔
🔘⚔ Unban ⚔
🔘⚔ Ban  @ ⚔
🔘⚔ Unban  @ ⚔
🔘⚔ Banlist ⚔
🔘⚔ Kill ban ⚔
🔘⚔ Mid  @ ⚔
🔘⚔ Kernel ⚔
🔘⚔ random: [ jumlah ] ⚔
🔘⚔ Gcreator:inv ⚔
🔘⚔ Gcreator ⚔
🔘⚔ Cipok ⚔
🔘⚔ Kickall ⚔
🔘⚔ Reboot ⚔
🔘⚔ Runtime ⚔
🔘⚔ Blacklist  @  ⚔
🔘⚔ Myname: ⚔
🔘⚔ Mybio: ⚔
🔘⚔ Copy  @ ⚔
🔘⚔ Backup me ⚔ 
🔘⚔ Ifconfig ⚔
🔘⚔ Kernel  ⚔
🔘⚔ Cpu ⚔
🔘⚔ System ⚔
🔘⚔ Say ⚔
🔘⚔ Say-en ⚔English
🔘⚔ Say-af  ⚔Africans
🔘⚔ Say-ko ⚔Korean
🔘⚔ Say-id  ⚔Indonesian
🔘⚔ Say-de ⚔Germany
🔘⚔ Say-ja  ⚔Japan
🔘⚔ Say-pl  ⚔Polish
🔘⚔ Music  ⚔
🔘⚔ Lyric⚔
🔘⚔ Steal name @ ⚔
🔘⚔ Steal bio @ ⚔
🔘⚔ Steal status @ ⚔
🔘⚔ Steal contact @ ⚔
🔘⚔ Steal cover @ ⚔
🔘⚔ Steal pict @ ⚔
🔘⚔ Steal mid @ ⚔
🔘⚔ Steal group pict ⚔
🔘⚔ Midpict: ⚔
🔘⚔ Info @ ⚔
🔘⚔ Youtube ⚔
🔘⚔ Vidio ⚔
🔘⚔ Wiki ⚔
🔘⚔ Instagram ⚔
🔘⚔ Translate-idn ⚔
🔘⚔ Translate-eng ⚔
🔘⚔ Translate-japan ⚔
🔘⚔ Translate-thai⚔
🔘⚔ Spam [on/off] [jumlah] [text]⚔
🔘⚔ Image: (link) ⚔
🔘⚔ Searchimage ⚔
🔘 ⚔Spam gift⚔
🔘 ⚔Spam sticker⚔
🔘 ⚔Random sticker⚔
🔘 ⚔Random gift⚔
🔘 ⚔Random number⚔
🔘 ⚔Spam toket⚔
🔘 ⚔Spam anu⚔
🔘 ⚔Virus⚔
🔘 ⚔Bisakah ⚔
🔘 ⚔Dosa @⚔
🔘 ⚔Pahala @⚔
🔘 ⚔Dimana ⚔
🔘 ⚔Apakah ⚔
🔘 ⚔Assist clone @⚔ 
🔘 ⚔Assist backup ⚔
🔘 ⚔Assist spam @⚔
🔘 ⚔Assist name: ⚔
🔘 ⚔Assist bio: ⚔
🔘 ⚔Assist speed⚔
🔘 ⚔Assist join⚔
🔘 ⚔Assist out⚔
🔘 ⚔Abist⚔      
▂▃▅▇█▓▒░۩S̺͆T̺͆A̺͆R̺͆B̺͆O̺͆T̺͆۩░▒▓█▇▅▃▂
═╬════════►∆∆
                            E̸͟͞d̸͟͞i̸͟͞t̸͟͞e̸͟͞d̸͟͞.
By.   »»» http://line.me/ti/p/VxtJPseezK «««
═╬════════►
"""

KAC=[ki] 
mid = cl.getProfile().mid
Amid = ki.getProfile().mid
Creator="u5baffcc81a0a0689982216a005cfc70b"
admin=["u5baffcc81a0a0689982216a005cfc70b","uc8e1e36f976e5f4e15e64d9d1cbe1878","ub34b6b9a9ce7d7fca99460477fd3fcf3","udd917e76596789ae636e53342f37f78c","u15be3f8d6ff7f0e53e4cc8bb30c4fa18","u940947814c50be1fed29c901beed59e1","u5a8137fd38839d7ae320ad9e005ecda1","ub80075ee3659acb3cfb51dfb3903451b","u4028e8b0666a78f054007ff696d7796d","u787fd768992b484e603ff5441f9eb699","u385a4a012015cc7964778a165514ac9a","u2744c4550c7e293e97adca243805fb4b","ufd259e96c3022e3743b9898a54e0136a","ua5aaf0948ab5631f2013bb50186d5f06","u6fb1bd6b5af0f27bbdb88ecb6a1468c0","u76315ca794eddf984026849e315c7aa6","u4fd06871f6f34b093a3972b8b5de8f3d","ueb83fb1e6439cc1c58332fedd065379c",Amid]

contact = cl.getProfile()
backup = cl.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

#contact = ki.getProfile()
#backup = ki.getProfile()
#backup.displayName = contact.displayName
#backup.statusMessage = contact.statusMessage
#backup.pictureStatus = contact.pictureStatus

wait = {
    "LeaveRoom":True,
    "AutoJoin":True,
    "Members":0,
    "AutoCancel":False,
    "AutoKick":False,       
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "Qr":True,
    "Timeline":True,
    "Contact":True,
    "lang":"JP",
    "BlGroup":{}    
}    


def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1
def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    return '%02d J̺͆a̺͆m̺͆ %02d M̺͆e̺͆n̺͆i̺͆t̺͆ %02d D̺͆e̺͆t̺͆i̺͆k̺͆' % (hours, mins, secs)
    
#^deff searchimage

def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     #If the Current Version of Python is 3.0 or above
        import urllib,request    #urllib library for Extracting web pages
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        #If the Current Version of Python is 2.x
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"
#Finding 'Next Image' from the given raw page
def _images_get_next_item(s):
    start_line = s.find('rg_di')
    if start_line == -1:    #If no links are found then give an error!
        end_quote = 0
        link = "no_links"
        return link, end_quote
    else:
        start_line = s.find('"class="rg_meta"')
        start_content = s.find('"ou"',start_line+90)
        end_content = s.find(',"ow"',start_content-90)
        content_raw = str(s[start_content+6:end_content-1])
        return content_raw, end_content

#Getting all links with the help of '_images_get_next_image'
def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      #Append all the links in the list named 'Links'
            time.sleep(0.1)        #Timer could be used to slow down the request for image downloads
            page = page[end_content:]
    return items
def yt(query):
    with requests.session() as s:
         isi = []
         if query == "":
             query = "S1B tanysyz"   
         s.headers['user-agent'] = 'Mozilla/5.0'
         url    = 'http://www.youtube.com/results'
         params = {'search_query': query}
         r    = s.get(url, params=params)
         soup = BeautifulSoup(r.content, 'html5lib')
         for a in soup.select('.yt-lockup-title > a[title]'):
            if '&list=' not in a['href']:
                if 'watch?v' in a['href']:
                    b = a['href'].replace('watch?v=', '')
                    isi += ['youtu.be' + b]
         return isi
         
def mention(to, nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print "[Command] Tag All"
    try:
       cl.sendMessage(msg)
    except Exception as error:
       print error
       
def bot(op):
    try:
#--------------------END_OF_OPERATION--------------------
        if op.type == 0:
            return
#-------------------NOTIFIED_READ_MESSAGE----------------
        if op.type == 55:
	    try:
	      group_id = op.param1
	      user_id=op.param2
	      subprocess.Popen('echo "'+ user_id+'|'+str(op.createdTime)+'" >> dataSeen/%s.txt' % group_id, shell=True, stdout=subprocess.PIPE, )
	    except Exception as e:
	      print e
#------------------NOTIFIED_INVITE_INTO_ROOM-------------
        if op.type == 22:
            cl.leaveRoom(op.param1)
#--------------------INVITE_INTO_ROOM--------------------
        if op.type == 21:
            cl.leaveRoom(op.param1)

#--------------NOTIFIED_INVITE_INTO_GROUP----------------

	    if mid in op.param3:
                if wait["AutoJoin"] == True:
                    cl.acceptGroupInvitation(op.param1)
                else:
		    cl.rejectGroupInvitation(op.param1)
	    else:
                if wait["AutoCancel"] == True:
		    if op.param3 in admin:
			pass
		    else:
                        cl.cancelGroupInvitation(op.param1, [op.param3])
		else:
		    if op.param3 in wait["blacklist"]:
			cl.cancelGroupInvitation(op.param1, [op.param3])
			cl.sendText(op.param1, "Itu kicker jgn di invite!")
		    else:
			pass
#------------------NOTIFIED_KICKOUT_FROM_GROUP-----------------
         #-------------------------------
        if op.type == 19:
            if mid in op.param3:
                wait["blacklist"][op.param2] = True
		if op.type == 17:
			if mid in op.param3:
				if wait["blacklist"] == True:
					cl.kickoutFromGroup(op.param1,[op.param2])
					ki.kickoutFromGroup(op.param1,[op.param2])
					kk.kickoutFromGroup(op.param1,[op.param2])
					ks.kickoutFromGroup(op.param1,[op.param2])
		if op.type == 32:
			if mid in op.param3:
				wait["blacklist"][op.param2] == True
		if op.type == 32:
			if mid in op.param3:
				if wait["blacklist"] == True:
					cl.kickoutFromGroup(op.param1,[op.param2])
					ki.kickoutFromGroup(op.param1,[op.param2])
					kk.kickoutFromGroup(op.param1,[op.param2])
					ks.kickoutFromGroup(op.param1,[op.param2])
		if op.type == 25:
			if mid in op.param3:
				wait["blacklist"][op.param2] == True
		if op.type == 25:
			if mid in op.param3:
				if wait["blacklist"] == True:
					cl.kickoutFromGroup(op.param1,[op.param2])
					ki.kickoutFromGroup(op.param1,[op.param2])
					kk.kickoutFromGroup(op.param1,[op.param2])
					ks.kickoutFromGroup(op.param1,[op.param2])
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.param3 == "4":
            if op.param1 in protecturl:
				group = cl.getGroup(op.param1)
				if group.preventJoinByTicket == False:
					group.preventJoinByTicket = True
					cl.updateGroup(group)
					cl.sendText(op.param1,"URL can not be changed")
					ki.kickoutFromGroup(op.param1,[op.param2])
					kk.kickoutFromGroup(op.param1,[op.param2])
					ks.kickoutFromGroup(op.param1,[op.param2])
					wait["blacklist"][op.param2] = True
					f=codecs.open('st2__b.json','w','utf-8')
					json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
				else:
					pass                
        if op.type == 19:
		if wait["AutoKick"] == True:
                    if op.param2 in admin:
                        pass
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
			cl.inviteIntoGroup(op.param1,[op.param3])
                    except:
                        try:
			    cl.kickoutFromGroup(op.param1,[op.param2])
			    cl.inviteIntoGroup(op.param1,[op.param3])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in admin:
			        pass
			    else:
                                wait["blacklist"][op.param2] = True
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in admin:
			    pass
		        else:
                            wait["blacklist"][op.param2] = True



#--------------------------NOTIFIED_UPDATE_GROUP---------------------
        if op.type == 11:
            if wait["Qr"] == True:
		if op.param2 in admin:
		    pass
		else:
                    cl.sendText(msg.to, "Jangan mainan QR ntr ada kicker")
            else:
                pass
#--------------------------SEND_MESSAGE---------------------------
        if op.type == 25:
            msg = op.message
#----------------------------------------------------------------------------
            if msg.contentType == 13:
                if wait["wblacklist"] == True:
		    if msg.contentMetadata["mid"] not in admin:
                        if msg.contentMetadata["mid"] in wait["blacklist"]:
                            cl.sendText(msg.to,"already")
                            wait["wblacklist"] = False
                        else:
                            wait["blacklist"][msg.contentMetadata["mid"]] = True
                            wait["wblacklist"] = False
                            cl.sendText(msg.to,"aded")
		    else:
			cl.sendText(msg.to,"Admin Detected~")
			

                elif wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        wait["dblacklist"] = False

                    else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"It is not in the black list")
#--------------------------------------------------------
                elif wait["Contact"] == True:
                     msg.contentType = 0
                     cl.sendText(msg.to,msg.contentMetadata["mid"])
                     if 'displayName' in msg.contentMetadata:
                         contact = cl.getContact(msg.contentMetadata["mid"])
                         try:
                             cu = cl.channel.getCover(msg.contentMetadata["mid"])
                         except:
                             cu = ""
                         cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                     else:
                         contact = cl.getContact(msg.contentMetadata["mid"])
                         try:
                             cu = cl.channel.getCover(msg.contentMetadata["mid"])
                         except:
                             cu = ""
                         cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))


#--------------------------------------------------------
            elif msg.text == "Ginfo":
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "close"
                        else:
                            u = "open"
                        cl.sendText(msg.to,"[Group name]\n" + str(ginfo.name) + "\n\n[Gid]\n" + msg.to + "\n\n[Group creator]\n" + gCreator + "\n\n[Profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n\nMembers:" + str(len(ginfo.members)) + "members\nPending:" + sinvitee + "people\nURL:" + u + "it is inside")
                    else:
                        cl.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")

#--------------------------------------------------------
            elif msg.text is None:
                return
#--------------------------------------------------------
#//commandnya
            elif msg.text.lower() == 'runtime':
                eltime = time.time() - mulai
                van = "「ᴮᴼᵀ ˢᵁᴰᴬᴴ ᴮᴱᴿᴶᴬᴸᴬᴺ ˢᴱᴸᴬᴹᴬ」"+waktu(eltime)
                cl.sendText(msg.to,van)                
            elif msg.text is None:
                return
            elif msg.text in ["Virus"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': "u5baffcc81a0a0689982216a005cfc70b',"}
                cl.sendMessage(msg)
		cl.sendText(msg.to,"mamvos...!!!")
            elif msg.text in ["Creator"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': "u5baffcc81a0a0689982216a005cfc70b"}
                cl.sendMessage(msg)
		cl.sendText(msg.to,"Itu Yang Bikin BOT")
#--------------------------------------------------------
	    elif msg.text in ["Group creator","Gcreator","gcreator"]:
		ginfo = cl.getGroup(msg.to)
		gCreator = ginfo.creator.mid
                msg.contentType = 13
                msg.contentMetadata = {'mid': gCreator}
                cl.sendMessage(msg)
		cl.sendText(msg.to,"Itu Yang Buat Grup Ini")
#--------------------------------------------------------
            elif msg.contentType == 16:
                if wait["Timeline"] == True:
                    msg.contentType = 0
                    msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
#--------------------------------------------------------
      #----------------
            elif "Steal contact" in msg.text:
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]                
                mmid = cl.getContact(key1)
                msg.contentType = 13
                msg.contentMetadata = {"mid": key1}
                cl.sendMessage(msg)
            elif msg.text in ["Menu"]:
                cl.sendText(msg.to,helpMessage)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Creator}
                cl.sendMessage(msg)
                
#--------------------------------------------------------
#----------------------
            elif "Besar cinta" in msg.text:
                tanya = msg.text.replace("Besar cinta","")
                jawab = ("0%","10%","20%","30%","40%","50%","60%","70%","80%","90%","100%")
                jawaban = random.choice(jawab)
                cl.sendText(msg.to,"Besar Cinta " + tanya + " adalah " + jawaban)
#-----------------------------------------------
#----------------------
            elif "Dimana " in msg.text:
                tanya = msg.text.replace("Dimana ","")
                jawab = ("Kuburan :v","Di pantai ","Pinggir sungai"," Singapore ","Perancis ( perapatan Ciamis hehe )")
                jawaban = random.choice(jawab)
                cl.sendText(msg.to," Pertanyaan :  Dimana " + tanya + "\n==================\n" + "Jawaban : " + jawaban)
#-----------------------------------------------
#----------------------
            elif "Bisakah " in msg.text:
                tanya = msg.text.replace("Bisakah ","")
                jawab = ("Ya","Bisa jadi","Mungkin","Coba tanya lagi :v","Tidak")
                jawaban = random.choice(jawab)
                cl.sendText(msg.to," Pertanyaan :  Bisakah " + tanya + "\n==================\n" + "Jawaban : " + jawaban)
#-----------------------------------------------
#----------------------
            elif "Apakah " in msg.text:
                tanya = msg.text.replace("Apakah ","")
                jawab = ("Ya","Bisa jadi","Mungkin","Coba tanya lagi :v","Tidak")
                jawaban = random.choice(jawab)
                cl.sendText(msg.to," Pertanyaan : Apakah " + tanya + "\n==================\n" + "Jawaban : " + jawaban)
#-----------------------------------------------
#----------------------
            elif "Dosa " in msg.text:
                tanya = msg.text.replace("Dosa ","")
                jawab = ("10%","20%","30%","40%","50%","60%","70%","80%","90%","100%","Tak terhingga")
                jawab2 = ("Waduh tobat yah","Banyak banyak tobat yah","Maksiat mulu sih lu")
                jawaban = random.choice(jawab)
                basa = random.choice(jawab2)
                cl.sendText(msg.to,"Dosanya " + tanya + " adalah " + jawaban + " " + basa)
#-----------------------------------------------
            elif msg.text in ["List group"]:
                gid = ki.getGroupIdsJoined()
                h = ""
		jml = 0
                for i in gid:
		    gn = ki.getGroup(i).name
                    h += "[{o̺͆}]【%s】\n" % (gn)
		    jml += 1
                ki.sendText(msg.to,"======[List Group]======\n"+ h +"Total group: "+str(jml))
#--------------------------------------------------------
	    elif "Leave group: " in msg.text:
		ng = msg.text.replace("Leave group: ","")
		gid = cl.getGroupIdsJoined()
		gid = ki.getGroupIdsJoined()
                for i in gid:
                    h = cl.getGroup(i).name
                    h = ki.getGroup(i).name                    
		    if h == ng:
			cl.sendText(i,"Bye "+h+"~")
		        cl.leaveGroup(i)
			cl.sendText(msg.to,"Success left ["+ h +"] group")
		    else:
			pass
#--------------------------------------------------------
#============================================================
            elif "Steal mid" in msg.text:
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                cl.sendText(msg.to,"Mc: " + key1)
#==========================================
            elif "Youtube " in msg.text.lower():
                if msg.from_ in admin:
                   query = msg.text.split(" ")
                   try:
                       if len(query) == 3:
                           isi = yt(query[2])
                           hasil = isi[int(query[1])-1]
                           cl.sendText(msg.to, hasil)
                       else:
                           isi = yt(query[1])
                           cl.sendText(msg.to, isi[0])
                   except Exception as e:
                       cl.sendText(msg.to, str(e))
            elif 'Vidio ' in msg.text:
	      if msg.from_ in admin:
                try:
                    textToSearch = (msg.text).replace('Vidio ', "").strip()
                    query = urllib.quote(textToSearch)
                    url = "https://www.youtube.com/results?search_query=" + query
                    response = urllib2.urlopen(url)
                    html = response.read()
                    soup = BeautifulSoup(html, "html.parser")
                    results = soup.find(attrs={'class':'yt-uix-tile-link'})
                    ght=('https://www.youtube.com' + results['href'])
		    cl.sendVideoWithURL(msg.to,ght)
                except:
                    cl.sendText(msg.to,"Could not find it")
#------------
#==================================================
            elif 'lyric ' in msg.text.lower():
              if msg.from_ in admin:
                try:
                    songname = msg.text.lower().replace('lyric ','')
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'Lyric Lagu ('
                        hasil += song[0]
                        hasil += ')\n\n'
                        hasil += song[5]
                        cl.sendText(msg.to, hasil)
                except Exception as wak:
                        cl.sendText(msg.to, str(wak))
                                 #----------------Fungsi Join Group Start-----------------------#
            elif msg.text in ["Kuy","Assist join","Join all"]:
              if msg.from_ in admin:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ks.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ka.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        kb.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ko.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ke.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ku.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ku2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ku3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ku4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ku5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                        print "Semua Sudah Lengkap"
                        G.preventJoinByTicket(G)
                        random.choice(KAC).updateGroup(G)
            elif 'wiki ' in msg.text.lower():
              if msg.from_ in admin:
                  try:
                      wiki = msg.text.lower().replace("wiki ","")
                      wikipedia.set_lang("id")
                      pesan="Title ("
                      pesan+=wikipedia.page(wiki).title
                      pesan+=")\n\n"
                      pesan+=wikipedia.summary(wiki, sentences=1)
                      pesan+="\n"
                      pesan+=wikipedia.page(wiki).url
                      cl.sendText(msg.to, pesan)
                  except:
                          try:
                              pesan="Over Text Limit! Please Click link\n"
                              pesan+=wikipedia.page(wiki).url
                              cl.sendText(msg.to, pesan)
                          except Exception as e:
                              cl.sendText(msg.to, str(e))
            elif "Info @" in msg.text:
              if msg.from_ in admin:
                nama = msg.text.replace("Info @","")
                target = nama.rstrip(' ')
                tob = cl.getGroup(msg.to)
                for g in tob.members:
                    if target == g.displayName:
                        gjh= cl.getContact(g.mid)
                        try:
                            cover = cl.channel.getCover(g.mid)
                        except:
                            cover = ""
                        cl.sendText(msg.to,"[Display Name]:\n" + gjh.displayName + "\n[Mid]:\n" + gjh.mid + "\n[BIO]:\n" + gjh.statusMessage + "\n[pict profile]:\nhttp://dl.profile.line-cdn.net/" + gjh.pictureStatus + "\n[Cover]:\n" + str(cover))
                    else:
                        pass
                                    #-------------------------------------------------
            elif "Say-ja " in msg.text:
                say = msg.text.replace("Say-ja ","")
                lang = 'ja'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
                                    #---------------------
            elif 'instagram ' in msg.text.lower():
              if msg.from_ in admin:
                try:
                    instagram = msg.text.lower().replace("instagram ","")
                    html = requests.get('https://www.instagram.com/' + instagram + '/?')
                    soup = BeautifulSoup(html.text, 'html5lib')
                    data = soup.find_all('meta', attrs={'property':'og:description'})
                    text = data[0].get('content').split()
                    data1 = soup.find_all('meta', attrs={'property':'og:image'})
                    text1 = data1[0].get('content').split()
                    user = "Name: " + text[-2] + "\n"
                    user1 = "Username: " + text[-1] + "\n"
                    followers = "Followers: " + text[0] + "\n"
                    following = "Following: " + text[2] + "\n"
                    post = "Post: " + text[4] + "\n"
                    link = "Link: " + "https://www.instagram.com/" + instagram
                    detail = "======INSTAGRAM INFO USER======\n"
                    details = "\n======INSTAGRAM INFO USER======"
                    cl.sendText(msg.to, detail + user + user1 + followers + following + post + link + details)
                    cl.sendImageWithURL(msg.to, text1[0])
                except Exception as njer:
                	cl.sendText(msg.to, str(njer))
                
                #----------------------
            elif "Pap cecan" in msg.text:
                tanya = msg.text.replace("Pap cecan","")
                jawab = ("https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcQAa0KQ8XfoVfKRh82Ys63AX3VcuPml1JJFLk7iTEtMpmd7OzbN-yk_MGK6","https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRPMwr1Igswf8wgrTURHbGAt9jn54SvimA6Ps6W6lCtItkrh4I-kA","https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRg5SRVDjILsjUyBeLkBnbV96kX22_1mplLyjfCKws6nv8E_VtMDyV07e56bw","https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTOXZ4yFF8R8vPVmEl21Txhvzh4YpUJkJ2uuO3KQLUzYIEVsuT9")
                jawaban = random.choice(jawab)
                cl.sendImageWithURL(msg.to,jawaban)
#-----------------------------------------------
#----------------------
            elif "Pap toket" in msg.text:
                tanya = msg.text.replace("Pap toket","")
                jawab = ("https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcTilO50kExe4q_t-l8Kfn98sxyrHcbWPWCu2GP2SNgg8XWGMaZc8h5zaxAeVA","https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQKgSYYgB33GP3LAvVSYxKjDlbPokmtzSWjbWJogz8lbZMNSyvqJTE3qWpwBg","https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTgwKO_CAdZpSlXVVfA29qglGQR00WHkeqq4JakyYDuzIW2tKhvGg","https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcSC3ZMq4PnCX5dj7Fc_N6HOG6R_XrmOM7r6uBtpEcBfbO4hMEXQirK_lU_ePw","https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRgynJUxS4uYgaIiV_R6e4FY62QfhYRUEgYZg6psfJzWH_ci4dFng")
                jawaban = random.choice(jawab)
                cl.sendImageWithURL(msg.to,jawaban)
#-----------------------------------------------#----------------------
            elif "Pap anu" in msg.text:
                tanya = msg.text.replace("Pap anu","")
                jawab = ("https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcQFFKdXErF56KzAa4oWnWQT34jmGKJ66lj1g0hnN4zwYh9GgW0dHWZfRnuM","https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcQTn4_JMD1ZAg-XIk6JZ1Crhz9gtXEIS8AcjTA3SYmazAutt7ekHw","https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcTIVuITo7KicaU6UwPhol1Rvkq4aQwznly8Xl2SiTlAa_1FrSHuwhwV5XoElA")
                jawaban = random.choice(jawab)
                cl.sendImageWithURL(msg.to,jawaban)
#-----------------------------------------------
                 #=======================================================
            elif "Translate-eng " in msg.text:
              if msg.from_ in admin:
                txt = msg.text.replace("Translate-eng ","")
                try:
                    gs = goslate.Goslate()
                    trs = gs.translate(txt,'en')
                    cl.sendText(msg.to,trs)
                    print '[Command] Translate EN'
                except Exception as error:
                    cl.sendText(msg.to,(error))
            elif "Translate-jp" in msg.text:
              if msg.from_ in admin:
                txt = msg.text.replace("Translate-jp ","")
                try:
                    gs = goslate.Goslate()
                    trs = gs.translate(txt,'jp')
                    cl.sendText(msg.to,trs)
                    print '[Command] Translate jp'
                except Exception as error:
                    cl.sendText(msg.to,(error))
            elif "Translate-th " in msg.text:
              if msg.from_ in admin:
                txt = msg.text.replace("Translate-th ","")
                try:
                    gs = goslate.Goslate()
                    trs = gs.translate(txt,'th')
                    cl.sendText(msg.to,trs)
                    print '[Command] Translate th'
                except Exception as error:
                    cl.sendText(msg.to,(error))
            elif "Translate-idn " in msg.text:
              if msg.from_ in admin:
                txt = msg.text.replace("Translate-id ","")
                try:
                    gs = goslate.Goslate()
                    trs = gs.translate(txt,'id')
                    cl.sendText(msg.to,trs)
                    print '[Command] Translate ID'
                except Exception as error: 
                    cl.sendText(msg.to,(error))          

#------------------------------------------------
            elif "Say-en " in msg.text:
                say = msg.text.replace("Say-en ","")
                lang = 'en'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
#-----------------------------------------------
#------------------------------------------------
            elif "Say-pl " in msg.text:
                say = msg.text.replace("Say-pl ","")
                lang = 'pl'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
#-----------------------------------------------
#------------------------------------------------
            elif "Say-af " in msg.text:
                say = msg.text.replace("Say-af ","")
                lang = 'af'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
#-----------------------------------------------
#------------------------------------------------
            elif "Say-ko " in msg.text:
                say = msg.text.replace("Say-ko ","")
                lang = 'ko'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
#-----------------------------------------------
#------------------------------------------------
            elif "Say-id " in msg.text:
                say = msg.text.replace("Say-id ","")
                lang = 'id'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
#-----------------------------------------------
#------------------------------------------------
            elif "Say-de " in msg.text:
                say = msg.text.replace("Say-de ","")
                lang = 'de'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
#-----------------------------------------------
#--------------------------------------------------------
            elif msg.text in ["cancel","Cancel"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        cl.sendText(msg.to,"No one is inviting")
                else:
                    Cl.sendText(msg.to,"Can not be used outside the group")
#--------------------------------------------------------
#-----------
            elif "Steal group pict" in msg.text:
              if msg.from_ in admin:
					group = cl.getGroup(msg.to)
					path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                                        cl.sendImageWithURL(msg.to,path)
            elif msg.text in ["Ourl","Url:on"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    cl.sendText(msg.to,"Url Active")
                else:
                    cl.sendText(msg.to,"Can not be used outside the group")
#-------------------------------------------------------
#==================================================================
            elif "Steal bio" in msg.text:
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                try:
                    cl.sendText(msg.to,contact.statusMessage)
                except:
                    cl.sendText(msg.to,contact.statusMessage)
            elif msg.text in ["Curl","Url:off"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    cl.sendText(msg.to,"Url inActive")

                else:
                    cl.sendText(msg.to,"Can not be used outside the group")
#--------------------------------------------------------
               #-------------
            elif "Mybio:" in msg.text:
                string = msg.text.replace("Mybio:","")
                if len(string.decode('utf-8')) <= 60000000000:
                    profile = cl.getProfile()
                    profile.statusMessage = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"􀜁􀇔􏿿Update Bio👉" + string + "👈")
#--------------------------------------------------------
           #---------------------------------------------------------
            elif "Myname:" in msg.text:
                string = msg.text.replace("Myname:","")
                if len(string.decode('utf-8')) <= 600000000000:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"The name " + string + " I did NI change ◑")          
#-----------------------------------------------
#--------------------------------------------------------
               #-------------
            elif "Assist bio:" in msg.text:
                string = msg.text.replace("Assist bio:","")
                if len(string.decode('utf-8')) <= 60000000000:
                    profile = ki.getProfile()
                    profile.statusMessage = string
                    ki.updateProfile(profile)
                    ki.sendText(msg.to,"􀜁􀇔􏿿Update Bio👉" + string + "👈")
#--------------------------------------------------------
           #---------------------------------------------------------
            elif "Assist name:" in msg.text:
                string = msg.text.replace("Assist name:","")
                if len(string.decode('utf-8')) <= 600000000000:
                    profile = ki.getProfile()
                    profile.displayName = string
                    ki.updateProfile(profile)
                    ki.sendText(msg.to,"The name " + string + " I did NI change ◑")          
#-----------------------------------------------
            elif msg.text in ["Join on","Autojoin:on"]:
                wait["AutoJoin"] = True
                cl.sendText(msg.to,"AutoJoin Active")

            elif msg.text in ["Join off","Autojoin:off"]:
                wait["AutoJoin"] = False
                cl.sendText(msg.to,"AutoJoin inActive")

#--------------------------------------------------------
#-----------------------------------------------
                #----------
                #========================================
            elif "Steal cover @" in msg.text:
              if msg.from_ in admin:            
                print "[Command]dp executing"
                _name = msg.text.replace("Steal cover @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            cu = cl.channel.getCover(target)
                            path = str(cu)
                            cl.sendImageWithURL(msg.to, path)
                        except:
                            pass
                print "[Command]dp executed"
            elif "Midpict:" in msg.text:
              if msg.from_ in admin:
                umid = msg.text.replace("Midpict:","")
                contact = cl.getContact(umid)
                try:
                    image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                except:
                    image = "https://www.1and1.co.uk/digitalguide/fileadmin/DigitalGuide/Teaser/not-found-t.jpg"
                try:
                    cl.sendImageWithURL(msg.to,image)
                except Exception as error:
                    cl.sendText(msg.to,(error))
                    pass
            elif "Steal pict " in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    msg.contentType = 0
                    steal0 = msg.text.replace("Steal pict ","")
                    steal1 = steal0.lstrip()
                    steal2 = steal1.replace("@","")
                    steal3 = steal2.rstrip()
                    _name = steal3
                    group = cl.getGroup(msg.to)
                    targets = []
                    for g in group.members:
                        if _name == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"not found")
                    else:
                        for target in targets:
                            try:
                                contact = cl.getContact(target)
                                try:
                                    image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                except:
                                    image = "https://www.1and1.co.uk/digitalguide/fileadmin/DigitalGuide/Teaser/not-found-t.jpg"
                                try:
                                    cl.sendImageWithURL(msg.to,image)
                                except Exception as error:
                                    cl.sendText(msg.to,(error))
                                    pass
                            except:
                                cl.sendText(msg.to,"Error!")
                                break
                else:
                    cl.sendText(msg.to,"Tidak bisa dilakukan di luar grup")
            elif "Say " in msg.text:
                say = msg.text.replace("Say ","")
                lang = 'id'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
                                        #----------*
            elif msg.text.lower() == 'ifconfig':
                    botKernel = subprocess.Popen(["ifconfig"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO NetStat===")
            elif msg.text.lower() == 'system':
                    botKernel = subprocess.Popen(["df","-h"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO SYSTEM===")
            elif msg.text.lower() == 'kernel':
                    botKernel = subprocess.Popen(["uname","-srvmpio"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO KERNEL===")
            elif msg.text.lower() == 'cpu':
                    botKernel = subprocess.Popen(["cat","/proc/cpuinfo"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO CPU===")
	    elif msg.text in ["Autocancel:on"]:
                wait["AutoCancel"] = True
                cl.sendText(msg.to,"The group of people and below decided to automatically refuse invitation")
		print wait["AutoCancel"][msg.to]

	    elif msg.text in ["Autocancel:off"]:
                wait["AutoCancel"] = False
                cl.sendText(msg.to,"Invitation refused turned off")
		print wait["AutoCancel"][msg.to]
#--------------------------------------------------------
                #-------------
            elif "Music " in msg.text:
                try:
                    songname = msg.text.lower().replace("Music ","")
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'This is Your Music\n'
                        hasil += 'Judul : ' + song[0]
                        hasil += '\nDurasi : ' + song[1]
                        hasil += '\nLink Download : ' + song[4]
                        cl.sendText(msg.to, hasil)
                        cl.sendText(msg.to, "Please Wait for audio...")
                        cl.sendAudioWithURL(msg.to, song[4])
                except Exception as njer:
                        cl.sendText(msg.to, str(njer))
		except Exception as njer:
		        cl.sendText(msg.to, str(njer))
		#==================================================================
            elif "Steal bio" in msg.text:
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                try:
                    cl.sendText(msg.to,contact.statusMessage)
                except:
                    cl.sendText(msg.to,contact.statusMessage)
	    elif "Qr:on" in msg.text:
	        wait["Qr"] = True
	    	cl.sendText(msg.to,"QR Protect Active")

	    elif "Qr:off" in msg.text:
	    	wait["Qr"] = False
	    	cl.sendText(msg.to,"Qr Protect inActive")
#--------------------------------------------------------
	    elif "Autokick:on" in msg.text:
		wait["AutoKick"] = True
		cl.sendText(msg.to,"AutoKick Active")

	    elif "Autokick:off" in msg.text:
		wait["AutoKick"] = False
		cl.sendText(msg.to,"AutoKick inActive")
#--------------------------------------------------------
            elif msg.text in ["K on","Contact:on"]:
                wait["Contact"] = True
                cl.sendText(msg.to,"Contact Active")

            elif msg.text in ["K off","Contact:off"]:
                wait["Contact"] = False
                cl.sendText(msg.to,"Contact inActive")
#--------------------------------------------------------
            elif msg.text in ["Status"]:
                md = ""
		if wait["AutoJoin"] == True: md+="◑ Auto join : on\n"
                else: md +="◑ Auto join : off\n"
		if wait["Contact"] == True: md+="◑ Info Contact : on\n"
		else: md+="◑ Info Contact : off\n"
                if wait["AutoCancel"] == True:md+="◑ Auto cancel : on\n"
                else: md+= "◑ Auto cancel : off\n"
		if wait["Qr"] == True: md+="◑ Qr Protect : on\n"
		else:md+="◑ Qr Protect : off\n"
		if wait["AutoKick"] == True: md+="◑ Autokick : on\n"
		else:md+="◑ Autokick : off"
                cl.sendText(msg.to,"=====[Status selfbot]=====\n"+md)
#--------------------------------------------------------
            elif msg.text in ["Gift","gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                cl.sendMessage(msg)


            elif msg.text in ["Gift1"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '696d7046-843b-4ed0-8aac-3113ed6c0733',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '6'}
                msg.text = None
                cl.sendMessage(msg)

            elif msg.text in ["Gift2"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '8fe8cdab-96f3-4f84-95f1-6d731f0e273e',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '7'}
                msg.text = None
                cl.sendMessage(msg)

            elif msg.text in ["Spam gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'ae3d9165-fab2-4e70-859b-c14a9d4137c4',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '8'}
                msg.text = None
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)

    #-------------Fungsi Tag All Start---------------#
            elif msg.text in ["Tag all","Cipok"]:
            	 if msg.from_ in admin:
                  group = cl.getGroup(msg.to)
                  nama = [contact.mid for contact in group.members]

                  cb = ""
                  cb2 = ""
                  strt = int(0)
                  akh = int(0)
                  for md in nama:
                      akh = akh + int(6)

                      cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""

                      strt = strt + int(7)
                      akh = akh + 1
                      cb2 += "@nrik \n"

                  cb = (cb[:int(len(cb)-1)])
                  msg.contentType = 0
                  msg.text = cb2
                  msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}

                  try:
                      cl.sendMessage(msg)
                  except Exception as error:
                      print error
    #-------------Fungsi Tag All Finish---------------#
##Buat kick by tag lebih dari 1

#--------------------------CEK SIDER------------------------------

            elif "Bintit" in msg.text:
                subprocess.Popen("echo '' > dataSeen/"+msg.to+".txt", shell=True, stdout=subprocess.PIPE)
                cl.sendText(msg.to, "sabar")
                cl.sendText(msg.to, "lg di proses")                
                print "@setview"

            elif "••••" in msg.text:
	        lurkGroup = ""
	        dataResult, timeSeen, contacts, userList, timelist, recheckData = [], [], [], [], [], []
                with open('dataSeen/'+msg.to+'.txt','r') as rr:
                    contactArr = rr.readlines()
                    for v in xrange(len(contactArr) -1,0,-1):
                        num = re.sub(r'\n', "", contactArr[v])
                        contacts.append(num)
                        pass
                    contacts = list(set(contacts))
                    for z in range(len(contacts)):
                        arg = contacts[z].split('|')
                        userList.append(arg[0])
                        timelist.append(arg[1])
                    uL = list(set(userList))
                    for ll in range(len(uL)):
                        try:
                            getIndexUser = userList.index(uL[ll])
                            timeSeen.append(time.strftime("%H:%M:%S", time.localtime(int(timelist[getIndexUser]) / 1000)))
                            recheckData.append(userList[getIndexUser])
                        except IndexError:
                            conName.append('nones')
                            pass
                    contactId = cl.getContacts(recheckData)
                    for v in range(len(recheckData)):
                        dataResult.append(contactId[v].displayName + ' ('+timeSeen[v]+')')
                        pass
                    if len(dataResult) > 0:
                        tukang = "List Viewer\n*"
                        grp = '\n* '.join(str(f) for f in dataResult)
                        total = '\n\nTotal %i viewers (%s)' % (len(dataResult), datetime.now().strftime('%H:%M:%S') )
                        cl.sendText(msg.to, "%s %s %s" % (tukang, grp, total))
                    else:
                        cl.sendText(msg.to, "Belum ada viewers")
                    print "@viewseen"
#--------------------------------------------------------

#KICK_BY_TAG
	    elif "Boom " in msg.text:
		if 'MENTION' in msg.contentMetadata.keys()!= None:
		    names = re.findall(r'@(\w+)', msg.text)
		    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
		    mentionees = mention['MENTIONEES']
		    print mentionees
		    for mention in mentionees:
			cl.kickoutFromGroup(msg.to,[mention['M']])

#--------------------------------------------------------
	    elif "Add all" in msg.text:
		thisgroup = cl.getGroups([msg.to])
		Mids = [contact.mid for contact in thisgroup[0].members]
		mi_d = Mids[:33]
		cl.findAndAddContactsByMids(mi_d)
		cl.sendText(msg.to,"Success Add all")
#--------------------------------------------------------
	    elif "Recover" in msg.text:
		thisgroup = cl.getGroups([msg.to])
		Mids = [contact.mid for contact in thisgroup[0].members]
		mi_d = Mids[:33]
		cl.createGroup("Recover", mi_d)
		cl.sendText(msg.to,"Success recover")
#--------------------------------------------------------
	    elif msg.text in ["Remove all chat"]:
		cl.removeAllMessages(op.param2)
		cl.sendText(msg.to,"Removed all chat")
#--------------------------------------------------------
            elif ("Gn: " in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Gn: ","")
                    cl.updateGroup(X)
                else:
                    cl.sendText(msg.to,"It can't be used besides the group.")
#--------------------------------------------------------
            elif "Kick: " in msg.text:
                midd = msg.text.replace("Kick: ","")
		if midd not in admin:
		    cl.kickoutFromGroup(msg.to,[midd])
		else:
		    cl.sendText(msg.to,"Admin Detected")
#--------------------------------------------------------
            elif "Invite: " in msg.text:
                midd = msg.text.replace("Invite: ","")
                cl.findAndAddContactsByMid(midd)
                ki.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to,[midd])
                ki.inviteIntoGroup(msg.to,[midd])
#--------------------------------------------------------
            elif msg.text in ["#welcome","Welcome","welcome","Welkam","welkam"]:
                gs = cl.getGroup(msg.to)
                cl.sendText(msg.to,"Selamat datang di "+ gs.name)
#-----------------------------------------------
            elif "Mid @" in msg.text:
            	if msg.from_ in admin:
                  _name = msg.text.replace("Mid @","")
                  _nametarget = _name.rstrip(' ')
                  gs = cl.getGroup(msg.to)
                  for g in gs.members:
                      if _nametarget == g.displayName:
                          cl.sendText(msg.to, g.mid)
                      else:
                          pass
#-----------------------------------------------
#--------------------------------------------------------
	    elif "Bc: " in msg.text:
		bc = msg.text.replace("Bc: ","")
		gid = cl.getGroupIdsJoined()
		for i in gid:
		    cl.sendText(i,"=======[BROADCAST]=======\n\n"+bc+"\n")
		cl.sendText(msg.to,"Success BC BosQ")
#--------------------------------------------------------
            elif msg.text in ["Cancelall"]:
                gid = cl.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                cl.sendText(msg.to,"All invitations have been refused")
#--------------------------------------------------------
            elif msg.text in ["Gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        cl.updateGroup(x)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
#--------------------------------------------------------
	    elif msg.text in ["Self Like","Self like"]:
		try:
		    print "activity"
		    url = cl.activity(limit=1)
		    print url
		    cl.like(url['result']['posts'][0]['userInfo']['mid'], url['result']['posts'][0]['postInfo']['postId'], likeType=1001)
		    cl.comment(url['result']['posts'][0]['userInfo']['mid'], url['result']['posts'][0]['postInfo']['postId'], "Auto like by: http://line.me/ti/p/~rhnprmd")
		    cl.sendText(msg.to, "Success~")
		except Exception as E:
		    try:
			cl.sendText(msg.to,str(E))
		    except:
			pass

#--------------------------------------------------------
#=================================================
            elif "Spam " in msg.text:
                if msg.from_ in admin:
                   txt = msg.text.split(" ")
                   jmlh = int(txt[2])
                   teks = msg.text.replace("Spam "+str(txt[1])+" "+str(jmlh)+ " ","")
                   tulisan = jmlh * (teks+"\n")
                   #Keke cantik <3
                   if txt[1] == "on":
                        if jmlh <= 10000:
                             for x in range(jmlh):
                                   cl.sendText(msg.to, teks)
                        else:
                               cl.sendText(msg.to, "Out of range! ")
                   elif txt[1] == "off":
                         if jmlh <= 10000:
                               cl.sendText(msg.to, tulisan)
                         else:
                               cl.sendText(msg.to, "Out of range! ")
            elif msg.text in ["Sp","Speed","speed"]:
                start = time.time()
		print("Speed")
		cl.sendText(msg.to, "「Please wait..」")
		elapsed_time = time.time() - start
                cl.sendText(msg.to, "[{o̺͆}]「Speed : 0.04 - 0.07」\n[{o̺͆}]「Speed is : %sseconds 」" % (elapsed_time))

#--------------------------------------------------------
            elif msg.text in ["Ban"]:
                wait["wblacklist"] = True
                cl.sendText(msg.to,"send contact")

            elif msg.text in ["Unban"]:
                wait["dblacklist"] = True
                cl.sendText(msg.to,"send contact")
#--------------------------------------------------------
	    elif "Assist backup" in msg.text:
		try:
		    ki.updateDisplayPicture(backup.pictureStatus)
		    ki.updateProfile(backup)
		    ki.sendText(msg.to, "Success backup profile")
		except Exception as e:
		    ki.sendText(msg.to, str(e))
#--------------------------------------------------------
#--------------------------------------------------------
	    elif "Semula" in msg.text:
		try:
		    cl.updateDisplayPicture(backup.pictureStatus)
		    cl.updateProfile(backup)
		    cl.sendText(msg.to, "seperti semula clear bos")
		except Exception as e:
		    cl.sendText(msg.to, str(e))
#--------------------------------------------------------
#-----------------------------------------------             
            elif msg.text in ["Gcreator:inv"]:              
            	if msg.toType == 2:
                 ginfo = cl.getGroup(msg.to)
                 gCreator = ginfo.creator.mid
                 try:
                    cl.findAndAddContactsByMid(gCreator)
                    cl.inviteIntoGroup(msg.to,[gCreator])
                    print "success inv gCreator"
                 except:
                    pass
            elif msg.text in ["Undang"]:
              if msg.from_ in admin:
                 wait["winvite"] = True
                 cl.sendText(msg.to,"send contact")
            elif msg.text in ["Tarik"]:
              if msg.from_ in admin:
                 wait["winvite2"] = True
                 ki.sendText(msg.to,"send contact")
            elif msg.text in ["Jepit"]:
              if msg.from_ in admin:
                 wait["winvite2"] = True
                 ki.sendText(msg.to,"send contact")
#-----------------------------------------------
#-----------------------------------------------
            elif msg.text in ["Gcreator"]:
              if msg.toType == 2:
                    msg.contentType = 13
                    ginfo = cl.getGroup(msg.to)
                    gCreator = ginfo.creator.mid
                    try:
                        msg.contentMetadata = {'mid': gCreator}
                        gCreator1 = ginfo.creator.displayName
                        
                    except:
                        gCreator = "Error"
                    cl.sendText(msg.to, "Group Creator : " + gCreator1)
                    cl.sendMessage(msg)
                    #-----------------------
	    elif "Copy " in msg.text:
                copy0 = msg.text.replace("Copy ","")
                copy1 = copy0.lstrip()
                copy2 = copy1.replace("@","")
                copy3 = copy2.rstrip()
                _name = copy3
		group = cl.getGroup(msg.to)
		for contact in group.members:
		    cname = cl.getContact(contact.mid).displayName
		    if cname == _name:
			cl.CloneContactProfile(contact.mid)
			cl.sendText(msg.to, "Success~")
		    else:
			pass
		
		                    #-----------------------
	    elif "Assist clone " in msg.text:
                copy0 = msg.text.replace("Assist clone ","")
                copy1 = copy0.lstrip()
                copy2 = copy1.replace("@","")
                copy3 = copy2.rstrip()
                _name = copy3
		group = ki.getGroup(msg.to)
		for contact in group.members:
		    cname = ki.getContact(contact.mid).displayName
		    if cname == _name:
			ki.CloneContactProfile(contact.mid)
			ki.sendText(msg.to, "Success~")
		    else:
			pass
		
#--------------------------------------------------------
    #-------------Fungsi Leave Group Start---------------#
            elif msg.text in ["Out"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                        kk.leaveGroup(msg.to)
                        kc.leaveGroup(msg.to)
                        ks.leaveGroup(msg.to)
                        ka.leaveGroup(msg.to)
                        kb.leaveGroup(msg.to)
                        ko.leaveGroup(msg.to)
                        ke.leaveGroup(msg.to)
                        ku.leaveGroup(msg.to)
                        ku2.leaveGroup(msg.to)
                        ku3.leaveGroup(msg.to)
                        ku4.leaveGroup(msg.to)
                        ku5.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "Image: " in msg.text:
					bctxt = msg.text.replace("Image: ","")
					cl.sendImageWithURL(msg.to,(bctxt))
            elif 'searchimage' in msg.text.lower():
                  try:
                      shi = msg.text.lower().replace("searchimage ","")
                      kha = random.choice(items)
                      url = 'https://www.google.com/search?hl=en&biw=1366&bih=659&tbm=isch&sa=1&ei=vSD9WYimHMWHvQTg_53IDw&q=' + shi
                      raw_html = (download_page(url))
                      items = items + (_images_get_all_items(raw_html))
                      items = []
                  except:
                      try:
                          start = timeit.timeit()
                          cl.sendImageWithURL(msg.to,random.choice(items))
                          cl.sendText(msg.to,"Total Image Links ="+str(len(items)))
                      except Exception as e:
                          cl.sendText(msg.to,str(e))
            elif "Ban @" in msg.text:
                if msg.toType == 2:
                    print "@Ban by mention"
                    _name = msg.text.replace("Ban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
			    if target not in admin:
                                try:
                                    wait["blacklist"][target] = True
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    cl.sendText(msg.to,"Succes BosQ")
                                except:
                                    cl.sendText(msg.to,"Error")
			    else:
				cl.sendText(msg.to,"Admin Detected~")
#--------------------------------------------------------
            elif "random:" in msg.text:
				if msg.from_ in admin:
					if msg.toType == 2:
						strnum = msg.text.replace("random:","")
						source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
						try:
							num = int(strnum)
							group = cl.getGroup(msg.to)
							for var in range(0,num):
								name = "".join([random.choice(source_str) for x in xrange(10)])
								time.sleep(0.01)
								group.name = name
								cl.updateGroup(group)
						except:
							cl.sendText(msg.to,"Error")
							
            elif msg.text in ["Banlist"]:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"nothing")
                else:
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,"===[Blacklist User]===\n"+mc)

#--------------------------------------------------------
            elif "Unban @" in msg.text:
                if msg.toType == 2:
                    print "@Unban by mention"
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Succes BosQ")
                            except:
                                cl.sendText(msg.to,"Succes BosQ")
#--------------------------------------------------------
            elif msg.text in ["Kill ban"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        cl.sendText(msg.to,"There was no blacklist user")
                        return
                    for jj in matched_list:
                        cl.kickoutFromGroup(msg.to,[jj])
                    cl.sendText(msg.to,"Blacklist emang pantas tuk di usir")
#--------------------------------------------------------
            elif "Kickall" in msg.text:
                if msg.toType == 2:
                    print "Kick all member"
                    _name = msg.text.replace("Kickall","")
                    gs = cl.getGroup(msg.to)
                    cl.sendText(msg.to,"Dadaaah~")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found.")
                    else:
                        for target in targets:
			     if target not in admin:
                                try:
                                    cl.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except Exception as e:
                                    cl.sendText(msg.to,str(e))
#--------------------------------------------------------
            elif "aBist" in msg.text:
                if msg.toType == 2:
                    print "Kick all member"
                    _name = msg.text.replace("aBist","")
                    gs = ki.getGroup(msg.to)
                    ki.sendText(msg.to,"lanjut")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Not found.")
                    else:
                        for target in targets:
			     if target not in admin:
                                try:
                                    ki.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except Exception as e:
                                    ki.sendText(msg.to,str(e))                                    
            elif "@"+cl.getProfile().displayName in msg.text:
                try:
                    tanya = msg.text.replace("@"+cl.getProfile().displayName,"")
                    jawab = ("ada apa bro "+cl.getProfile().displayName+"nya lg sibuk, Kalo penting PM aja...!")                                    
                    cl.sendText(msg.to,"jawaban")
                except:
                    pass                    
#--------------------------------------------------------
#Restart_Program
	    elif msg.text in ["Reboot"]:
		       cl.sendText(msg.to, "Bot has been restarted")
		       restart_program()
		       print "@Restart"
#--------------------------------------------------------
#-----------------------------------------------             
        if op.type == 19:
            try:
                if op.param3 in mid:
                    if op.param2 in Amid:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                    else:
                        G = ki.getGroup(op.param1)                        
                        
                        ki.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        wait["blacklist"][op.param2] = False

                elif op.param3 in op.param3:
                    if op.param1 in protection:
                        OWN = "u28bee33a596b0fafb73d601397321c22","u406133ad4d3fbe50a2f4d51ea081d050","ua51ba06b0dd18c0bfe2cc6caa3458202","u34a9af3a18784280147fc413a68a77fd"
                    if op.param2 in OWN:
                        kicker1 = [cl,ki,kk,ks,kc,ka,km,kn,ko]
                        G = random.choice(kicker1).getGroup(op.param1)
                        G.preventJoinByTicket = False
                        random.choice(kicker1).updateGroup(G)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        random.choice(kicker1).updateGroup(G)
                    else:
                        G = random.choice(kicker1).getGroup(op.param1)

                        random.choice(kicker1).kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        random.choice(kicker1).updateGroup(G)
                        Ticket = random.choice(kicker1).reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        random.choice(kicker1).updateGroup(G)

                        wait["blacklist"][op.param2] = True
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        
                elif op.param3 in Amid:
                    if op.param2 in mid:
                        G = cl.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                    else:
                        G = cl.getGroup(op.param1)

                        
                        cl.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                        wait["blacklist"][op.param2] = False
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)            
            except:
                pass
                #---------------------------
        if op.type == 19:
            try:
                if op.param3 in Amid:
                    if op.param2 in mid:
                        G = cl.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                    else:
                        G = cl.getGroup(op.param1)

                        
                        cl.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)


                elif op.param3 in mid:
                    if op.param2 in Amid:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                    else:
                        G = ki.getGroup(op.param1)

                        
                        ki.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        wait["blacklist"][op.param2] = False
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)            
            except:
                pass
                #-----------------
        if op.type == 59:
            print op


    except Exception as error:
        print error


#thread2 = threading.Thread(target=nameUpdate)
#thread2.daemon = True
#thread2.start()

while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)

