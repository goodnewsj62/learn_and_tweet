import io

with io.BytesIO(b"normal boring bytes") as f, \
io.StringIO("second cool string bet you did'nt know of this") as x,\
io.BytesIO(b"cool bytes you get the point") as v:
    print(f.getvalue())
    print(x.getvalue())
    print(v.getvalue())

# RESULT:
# b'normal boring bytes'
# second cool string bet you did'nt know of this
# b'cool bytes you get the point'

try:
    print(f.getvalue())
except ValueError as e:
    import logging
    logging.exception(f" {e}:")

# LOG:
# ERROR:root: I/O operation on closed file.:
# Traceback (most recent call last):
#   File "/home/goodnews/Documents/twitter_posts/learn_and_tweet/with_many.py", line 11, in <module>
#     print(f.getvalue())
# ValueError: I/O operation on closed file.