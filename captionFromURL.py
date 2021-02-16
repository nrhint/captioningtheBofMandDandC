import re

from util.verse_util import get_verse_from_file
from util.video_util import get_time_from_video
from util.subtitle_util import generate_srt

book = 'D&C'
urlList = open('resources/book/' + book + '.csv', 'r').read()
urlList = urlList.split('\n') #The urlList file is a set of new line spaced links with the first one being a comment
urlList.pop(0) #The first line is a comment that says the purpuse of the file

for detail in urlList:
    details = detail.split(',')
    prefix = details[0]
    url = details[1]
    url = re.sub(' ', '', url)
    verses = get_verse_from_file(book, prefix)
    get_time_from_video(verses, url)
    srt = generate_srt(verses)
    open('output/book/%s/%s.srt'%(book, prefix), 'w').write(srt)
    print('SRT file for %s written at %s'%(prefix, 'output/book/%s/%s.srt'%(book, prefix)))