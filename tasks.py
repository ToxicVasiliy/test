# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests

def count_words_at_url(url):
    resp = requests.get(url)
    return len(resp.text.split())