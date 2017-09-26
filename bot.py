# This Python file uses the following encoding: utf-8 /// code này để python hiểu viết unicode
import os, sys
from fbchat import Client
from fbchat.models import *
from config import *
import time

class AutoReplyBot(Client):
	def onMessage(self, author_id, message, thread_id, thread_type, **kwargs):
		self.markAsDelivered(author_id, thread_id)   /// code này sẽ khiến cho tin nhắn là đã nhận
		self.markAsRead(author_id)    				/// code này là đã xem tin nhắn

		if author_id != self.uid and thread_type == ThreadType.USER:
			messages = client.fetchThreadMessages(thread_id, limit=30)     / bot sẽ đọc 30 tin nhắn rồi sẽ xác thực và trả lời tin nhắn tự động

			for i in range(0, len(messages)):
				if(messages[i].author == self.uid):
					lastmessage = messages[i]
					break
			if 'lastmessage' in locals():
				away = (int(time.time() - (int(lastmessage.timestamp))/1000)/60)
				if(away >= 10):				/// đọc 30 tin nhắn và sau 10p sẽ tự trả lời tự động
					self.sendMessage("Đây là tin nhắn trả lời tự động của BOT, hiện tại tui đang offline, bạn vui lòng để lại lời nhắn, nếu tui seen mà ko reply lại bạn thì do BOT tự seen chứ tui ko có seen đâu :(, tui sẽ reply trong thời gian sớm nhất <3.", thread_id=thread_id, thread_type=thread_type)				/// code này là nội dung tin nhắn
					self.sendRemoteImage('https://i.imgur.com/GjUMhvs.png', thread_id=thread_id, thread_type=thread_type)			/// code này là tui dò source code trên github, tải 1 ảnh từ link đính kèm và gủi đi
			else:
					self.sendMessage("Đây là tin nhắn trả lời tự động của BOT, hiện tại tui đang offline, bạn vui lòng để lại lời nhắn, nếu tui seen mà ko reply lại bạn thì do BOT tự seen chứ tui ko có seen đâu :(, tui sẽ reply trong thời gian sớm nhất <3.", thread_id=thread_id, thread_type=thread_type)
					self.sendRemoteImage('https://i.imgur.com/GjUMhvs.png', thread_id=thread_id, thread_type=thread_type)
client = AutoReplyBot(username, password)
client.listen()