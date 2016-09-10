import glob, os
from feedgen.feed import FeedGenerator

home = "/home/balint"
dirpath = home + '/autopodcaster/onkenyes'
print(dirpath)

os.chdir(dirpath)
files = glob.glob('*.mp3')
print(files)

fg = FeedGenerator()
fg.load_extension('podcast')

# TODO remove filler data
fg.id('http://example.com')
fg.title('Autopodcaster testfeed')
fg.author(name='John Doe', email='john@example.de')
fg.link(href='http://example.com', rel='alternate')
fg.logo('https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Flag_of_River_Gee_County.svg/640px-Flag_of_River_Gee_County.svg.png')
fg.subtitle('This is a test feed of autopodcaster!')
fg.link(href='http://example.com', rel='self')
fg.language('en')

# fg.podcast.itunes_category('Technology', 'Podcasting')

for f in files:
    fe = fg.add_entry()
    fe.id(f)
    fe.title(f)
    fe.description('Automatically generated with AutoPodcaster')
    # TODO add date/time source information
    size = os.path.getsize(f)  # size of file in bytes
    fe.enclosure('http://192.168.1.132/onkenyes/' + f, str(size), 'audio/mpeg')
    # TODO make this portable

fg.rss_file('./podcast.xml')
print('Finished.')
