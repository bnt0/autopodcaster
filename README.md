# autopodcaster

Set of scripts (currently Bash and Python 3) to automatically generate podcasts RSS feeds from online radio streams and Youtube channels (or playlists).

## Dependencies

* [feedgenerator](https://github.com/lkiesow/python-feedgen) library
* A cron implementation (e.g. [cronie](https://fedorahosted.org/cronie/))

For Youtube videos:
* [youtube-dl](https://github.com/rg3/youtube-dl/)
* avconv or FFmpeg (for converting to mp3)

For radio streams:
* [streamripper](http://streamripper.sourceforge.net/)
