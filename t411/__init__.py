from .main import t411
from couchpotato.core.logger import CPLog

log = CPLog(__name__)

def autoload():
    log.debug('load success')
    return t411()

config = [{
    'name': 't411',
    'groups': [
        {
            'tab': 'searcher',
            'list': 'torrent_providers',
            'name': 'T411',
            'description': 'See <a href="https://t411.in">T411</a>',
            'icon': 'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAIAAACQkWg2AAAAA3NCSVQICAjb4U/gAAACdklEQVQokW2RX0hTcRTHz+/+cbvz3m1srbv8M6Ws6SbK1hRTkUoKIui5jIJ8sz9vQQTRQxDRexCkIGgmSC+B1YNWNCIrRQ3Z2PyTf5pb2/S2ud2/2723hyIt/b4cDud7+H4OB2CXrpOW+wYLYPju0R66DTABEAWYB7i6lwHtbEYAKi5crPE36Wa6QGKQyYylk1cePPwX4FqPquSSiZVHAN+Gh/JihpezUpGXinmxkBN5Lvjm5U4/1hzwS5JsJIkzkWnmZDtSZF2WQZZ0SSoIgiSJXq+37VjLNhLL7h/ofUzg0Dceutl1ejHOoa0fScUQW1rouXQWw3ANULXbt8cNJ7pudPrcd/pmLp8PBNpa344HDYTqYc2Ls58G+59sI/0uTgBTKj78OQIdTb6W5gKg+PpKaPprUoLB/mBHY/v/CacARru7ucaG6NCrj5vp2rpDWvmBDa83PzDwdJVOl5Zo8S+JQhoD7E/CGMBEKLyYTNWjLKNl6KkP5OsXbE1leGqdNFoBd3K034jbcJzYfqfPTpUZjOHkmkmS+SpzinXYlxdGM+4I5ezkoyHSUcIjHXHY3wWPqM9SOg2ataFMlvQ6YWs5FIvaKxxgmzEfrWYOazanXuAxAGBwGALoNcWePxtx8cKR4wGuBFZo05TI2gXViE3SaiyVn3bQRgU0DABuVdHn7na6iuSMAOk2X6WnrqLcMVlqTVQ5lHw2VaQURtNN+7YoD7L4cQCQKGo9GJsUEGC6bNPfzc1xpZAjWuH7+3u+xHy+BuFLLkYsx7la0yrCAeqdZg0h1kDQFkpVlSyvrG1krM5mNbtK/9wM0wddjF6UNywElpWVX6HUDxDMdBkmAAAAAElFTkSuQmCC',
            'wizard': True,
            'options': [
                {
                    'name': 'enabled',
                    'type': 'enabler',
                    'default': False,
                },
                {
                    'name': 'username',
                    'default': '',
                },
                {
                    'name': 'password',
                    'default': '',
                    'type': 'password',
                },
                {
                    'name': 'ignore_year',
                    'label': 'ignore year',
                    'default': 0,
                    'type': 'bool',
                    'description': 'Will ignore the year in the search results',
                },
                {
                    'name': 'seed_ratio',
                    'label': 'Seed ratio',
                    'type': 'float',
                    'default': 1,
                    'description': 'Will not be (re)moved until this seed ratio is met.',
                },
                {
                    'name': 'seed_time',
                    'label': 'Seed time',
                    'type': 'int',
                    'default': 40,
                    'description': 'Will not be (re)moved until this seed time (in hours) is met.',
                },
                {
                    'name': 'extra_score',
                    'advanced': True,
                    'label': 'Extra Score',
                    'type': 'int',
                    'default': 20,
                    'description': 'Starting score for each release found via this provider.',
                }
            ],
        },
    ],
}]
