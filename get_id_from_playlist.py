from apiclient.discovery import build

DEVELOPER_KEY = "DEVELOPER_KEYを指定"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
videos = []


def youtube_playlist_id(playlist_id, pagetoken):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

    search_response = youtube.playlistItems().list(
        playlistId=playlist_id,
        part="snippet",
        maxResults=50,
        pageToken=pagetoken
    ).execute()

    for search_result in search_response["items"]:
        title = search_result["snippet"]["title"]
        video_id = search_result["snippet"]["resourceId"]["videoId"]
        videos.append(video_id)
        print(title + "/" + video_id)

    try:
        # nextPageTokenが返ってくる限り処理を繰り返す
        nextPagetoken = search_response["nextPageToken"]
        youtube_playlist_id(nextPagetoken)
    except:
        return


def get_video_ids(id):
    print("id取得")
    youtube_playlist_id(id, "")
    return videos
