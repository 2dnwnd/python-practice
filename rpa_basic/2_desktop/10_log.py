# import logging

# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s [%(levelname)s] %(message)s')

# logging.debug('아 이거 누가 짠거야')
# logging.info('자동화 수행 준비')
# logging.warning('이 스크립트는 조금 오래됨')
# logging.error('에러 발생')
# logging.critical('치명적 문제 발생')

# 터미널과 파일에 함께 로그 남기기
import logging
from datetime import datetime
# 시간 로그레벨 메세지
logFormatter =logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
logger = logging.getLogger()
# 로그 레벨 설정
logger.setLevel(logging.DEBUG)

# 스트림
streamHandler = logging.StreamHandler()
streamHandler.setFormatter(logFormatter)
logger.addHandler(streamHandler)

# 파일
filename = datetime.now().strftime('mylogfile_%Y%m%d%H%M%S.log')
fileHandler = logging.FileHandler(filename, encoding='utf-8')
fileHandler.setFormatter(logFormatter)
logger.addHandler(fileHandler)

logger.debug('로그를 남겨보는 테스트를 진행합니다.')