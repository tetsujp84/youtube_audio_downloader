# !/usr/bin/env python
# coding: utf-8

import get_id_from_playlist as pl
import donwload_audio

#https://www.youtube.com/watch?v=XXXXXXXX&list=YYYYYYYY
PLAY_LIST_ID = "プレイリストID(YYYYYYYY)"
#プレイリスト内のVideoIDリスト取得
video_id_list = pl.get_video_ids(PLAY_LIST_ID)
#VideoIDリストからダウンロード→音声抽出
donwload_audio.save_audio(video_id_list)