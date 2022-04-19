from imap_tools import MailBox
from account import *

# mailbox = MailBox('imap.gmail.com', 993)
# mailbox.login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder='INBOX')

with MailBox('imap.gmail.com', 993).login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder='INBOX') as mailbox:
    # for msg in mailbox.fetch(): # 전체메일 다 가져오기
    #     print('[{}] {}'.format(msg.from_, msg.subject))

    # for msg in mailbox.fetch('(UNSEEN)'): # 읽지않은 메일 가져오기
    #     print('[{}] {}'.format(msg.from_, msg.subject))

    # for msg in mailbox.fetch('(FROM dnwnd1019@gmail.com)'): # 특정인이 보낸 메일 가져오기
    #     print('[{}] {}'.format(msg.from_, msg.subject))

    # for msg in mailbox.fetch('(TEXT "테스트")'): # 특정 글자를 포함하는 메일 가져오기
    #     print('[{}] {}'.format(msg.from_, msg.subject))
    
    # for msg in mailbox.fetch('(SUBJECT "test")'): # 특정 글자를 포함하는 메일 가져오기 (제목만)
    #     print('[{}] {}'.format(msg.from_, msg.subject))

    # for msg in mailbox.fetch(): # 특정 글자(한글)를 포함하는 메일 
    #     if '테스트' in msg.subject:
    #         print('[{}] {}'.format(msg.from_, msg.subject))
    
    # for msg in mailbox.fetch('(SENTSINCE 07-Nov-2021)'): # 특정 날짜이후에 온 메일
    #     print('[{}] {}'.format(msg.from_, msg.subject))

    for msg in mailbox.fetch('(SENTSINCE 07-Nov-2021 UNSEEN)'): # 2가지 이상의 조건
        print('[{}] {}'.format(msg.from_, msg.subject))
