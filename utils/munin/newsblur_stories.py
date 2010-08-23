#!/usr/bin/env python 

from utils.munin.base import MuninGraph
from apps.rss_feeds.models import MStory
from apps.reader.models import MUserStory

graph_config = {
    'graph_category' : 'NewsBlur',
    'graph_title' : 'NewsBlur Stories',
    'graph_vlabel' : 'Stories',
    'stories.label': 'stories',
    'tags.label': 'tags',
    'authors.label': 'authors',
    'read_stories.label': 'read_stories',
}

metrics = {
    'stories': MStory.objects().count(),
    'read_stories': MUserStory.objects().count(),
}

if __name__ == '__main__':
    MuninGraph(graph_config, metrics).run()
