import logging

logging.basicConfig(level="DEBUG")

logger = logging.getLogger(__name__) # name of this module could me __main__ or log
# basically you could do logging.getLogger('any_name')
#think of a logger as a name bucket or dump where certain logs are directed to

logger.debug("script is running") #prints level:name of logger: message
logger.info("wow this would be fun")
logger.warning("this is a warning you are running script")

try:
    x = 1/0
except ZeroDivisionError as e:
    # you can get the traceback of an exception easily with the below
    logger.exception(f"zero division error here: {e}") # this is same as logger.error("message",exc_info=True)

# RESULT:
# >>>python log.py 
# DEBUG:__main__:script is running
# INFO:__main__:wow this would be fun
# WARNING:__main__:this is a warning you are running script
# ERROR:__main__:zero division error here: division by zero
# Traceback (most recent call last):
#   File "/home/goodnews/Documents/twitter_posts/learn_and_tweet/log.py", line 13, in <module>
#     x = 1/0
# ZeroDivisionError: division by zero