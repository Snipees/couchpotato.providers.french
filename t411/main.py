from bs4 import BeautifulSoup
from couchpotato.core.helpers.encoding import tryUrlencode
from couchpotato.core.helpers.encoding import toSafeString
from couchpotato.core.helpers.variable import tryInt
from couchpotato.core.logger import CPLog
from couchpotato.environment import Env
from couchpotato.core.media._base.providers.torrent.base import TorrentProvider
from couchpotato.core.media.movie.providers.base import MovieProvider
import traceback
from urlparse import urlparse
import json
import re
import time

log = CPLog(__name__)


class t411(TorrentProvider, MovieProvider):

    urls = {
        'test' : 'https://t411.in',
        'login' : 'https://api.t411.in/auth',
        'login_check': 'https://api.t411.in/torrents/top/100',
        'detail' : 'https://www.t411.in/torrents/?id=%s',
        'search' : 'https://api.t411.in/torrents/search/%s?limit=200&cat=631',
        'download' : 'https://api.t411.in/torrents/download/%s',
    }

    cat_ids = [
        ([28], ['720p', '1080p']),
        ([2], ['cam', 'ts', 'tc', 'r5', 'scr', 'dvdrip', 'brrip']),
        ([3], ['dvdr']),
    ]

    http_time_between_calls = 1 #seconds
    cat_backup_id = None

    def _searchOnTitle(self, title, movie, quality, results):
        log.debug('Searching T411 for %s' % (title))
        url = self.urls['search'] % (title.replace(':', ''))
        try:
            output = self.getJsonData(url,cache_timeout = 30, headers = {"Authorization": self.token})
        except: pass
        for entry in output['torrents']:
            try:
                log.debug(entry)
                #log.debug("NAME: "+entry['name']+"  SIZE:  "+self.parseSize(str(tryInt(tryInt(entry['size'])/1024))+"kb"))
                results.append({
                    'id': entry['id'],
                    'name': entry['name'],
                    'url': self.urls['download'] % entry['id'],
                    'detail_url': self.urls['detail'] % entry['id'],
                    'size': self.parseSize(str(tryInt(tryInt(entry['size'])/1024))+"kb"),
                    'seeders': entry['seeders'],
                    'leechers': entry['leechers'],
                    })
            except:
                error = traceback.format_exc()

    def login(self):
        log.debug('Try to login on T411')
        # Check if we are still logged in every 60 days

        self.token = self.conf('token')

        now = time.time()
        if self.last_login_check and self.last_login_check < (now - 10):
            try:
                output = self.getJsonData(self.urls['login_check'],cache_timeout = 30, headers = "Authorization: %s" % self.token)
                if self.loginCheckSuccess(output):
                    self.last_login_check = now
                    return True
            except: pass
            self.last_login_check = None

        if self.last_login_check:
            return True

        try:
            output = self.getJsonData(self.urls['login'], files=False, data = self.getLoginParams())

            if self.loginSuccess(output):
                self.last_login_check = now
                self.conf('token',value = output['token'])
                return True

            error = 'unknown'
        except:
            error = traceback.format_exc()


    def download(self, url = '', nzb_id = ''):
        log.debug('Try to download %s from %s', (self.getName(), traceback.format_exc()))
        try:
            torrent = self.urlopen(url, files=False, headers = {"Authorization": self.conf('token')})
            return torrent
        except:
            log.error('Failed getting release from %s: %s', (self.getName(), traceback.format_exc()))

        return 'try_next'


    def getLoginParams(self):
        log.debug('Getting login params for T411')
        return {
            'username': self.conf('username'),
            'password': self.conf('password'),
        }

    def loginSuccess(self, output):
        log.debug('Checking login success for T411: %s' % ('True' if (output.has_key('error') != True) else 'False'))
        #return True
        return (output.has_key('error') != True)

    loginCheckSuccess = loginSuccess
    loginDownload = download
