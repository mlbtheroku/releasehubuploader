class Translation(object):
    START_TEXT = """Hi {} ๐,
I'm <b>Simple Uploader Bot! โจ</b>

<u>I can upload various kind of direct link formats such as:</u>

1. MP4
2. some M3U8 links
3. YouTube
4. Mediafire
5. Google Drive (if link is public)
6. Fembed (<code>fembed.com</code> domain)
7. Streamtape (beta)
and many other direct links!... ๐ฅณ
    
<i><b>Note:</b> Support for other links will be added soon.</i>

<i>You have the ability to set custom captions and custom thumbnails for your uploads too! ๐ซ</i>

<b>So what are you waiting for!...

Send me a direct link and I will upload it to telegram as a file/video.</b>

/help for more details!"""
    ADD_CAPTION_HELP = """Select an uploaded file/video or forward me <b>Any Telegram File</b> and just write the text you want to be on the file <b>as a reply to the file</b> and the text you wrote will be attached as the caption! ๐คฉ
    
Ex: <a href='https://telegra.ph/file/198bcda5944f787373122.jpg'>See This!</a> ๐"""
    INCORRECT_REQUEST = """<b>โMake sure you submit your request correctlyโ</b>
    
/help for more details!"""
    DISPLAY_PROGRESS = """[{0}{1}] {2}%
<i>๐ {3}</i>

<b>๐นFinished โ:</b> <i>{4} of {5}</i>
<b>๐นSpeed ๐:</b> <i>{6}/s</i>
<b>๐นTime left ๐:</b> <i>{7}</i>"""
    FORMAT_SELECTION = """<b>If you haven't set <a href='{}'>a thumbnail</a> before you can send a photo now. If you don't want to don't worry - You will get an auto genarated thumbnail from the video to your upload ๐</b>
    
๐๐ฆ๐ฒ๐น๐ฒ๐ฐ๐ ๐๐ป๐ฑ ๐๐ต๐ผ๐๐ฒ ๐ฌ๐ผ๐๐ฟ ๐๐ผ๐ฟ๐บ๐ฎ๐๐
(If your link is a video and if you want it as a streamable video select a video option. If you want your upload in document format select a file option).

<b>Make sure that the format you select is no larger than 2 GB.</b>"""
    SET_CUSTOM_USERNAME_PASSWORD = """If you want to download premium videos, provide in the following format:
URL | filename | username | password"""
    DOWNLOAD_START = """<b>File detected:</b> {}
    
<b>Downloading to my server... ๐ฅ</b>

Please wait uploading will start as soon as possible ๐"""
    UPLOAD_START = "<b>Uploading to Telegram... ๐ค</b>"
    RCHD_TG_API_LIMIT = """<b>โThe file couldn't be uploadedโ</b>
Sorry. I cannot upload files greater than 2GB due to Telegram API limitations.

<b>๐ธFile detected:</b> <i>{}</i>
<b>๐ธDownloaded:</b> <i>in {} seconds</i>
<b>๐ธDetected file size:</b> <i>{}</i>"""
    UNKNOWN_ERROR = """<b>โUNKNOWN ERRORโ</b>
I don't know what just happened ๐
But I'm going to find out and fix it as soon as possible ๐ง"""
    AFTER_SUCCESSFUL_UPLOAD_MSG = "๐ Thanks for using @SimpleUploaderBot."
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = """<i>โ Downloaded in <b>{} seconds</b></i>
<i>โ Uploaded in <b>{} seconds</b></i>"""
    SAVED_CUSTOM_THUMB_NAIL = "โ Custom video/file thumbnail saved. This image will be used in the video/file."
    DEL_ETED_CUSTOM_THUMB_NAIL = "โ Custom thumbnail cleared succesfully."
    CUSTOM_CAPTION_UL_FILE = "{}"
    NO_FILE_FOUND = """<b>โI couldn't find any video/fileโ</b>
Go check if you can access the content in the URL from your browser first!"""
    NO_VOID_FORMAT_FOUND = """<b>โSOMETHING WENT WRONGโ</b>
I think you have entered an unaccessible URL or a private URL (which only works with your IP).

<b>๐จAdditional info:</b>
{}"""
    HELP_USER = """<b>How to use me?</b> ๐ค
Follow these steps! ๐
    
<b>1. Send URL</b>

If you want a custom caption on your video/file send the name/text you want to set on the video/file in the following format ๐

<b>Link * caption</b> (without extension). 
<i>[Separate the link and the caption name with "*" mark].</i>

<u>It is important that you separate with spaces the URL, * and the caption.</u>

<b>๐ Send something like this:</b>
<code>https://www.website.com/video.mp4 * caption text</code>

<b>๐คก Not like this:</b>
<code>โ https://www.website.com/video.mp4*caption text โ</code>

The caption/text you type will be automatically set as the custom name of the uploaded file ๐

<i><b>Note:</b> You can change/add any caption later if you want as explained in the end.</i>

<b>2. Then send custom thumbnail when asked while uploading the URL</b> (This step is optional) 

๐น It means it is not necessary to send an image to include as an thumbnail.
If you don't send a thumbnail the video/file will be uploaded with an auto generated thumbnail from the video.
<i>(The thumbnail you send will be used for your next uploads)</i>

๐น Press /delthumbnail if you want to delete the previously saved thumbnail.
<i>(Then the video will be uploaded with an auto-genarated thumbnail)</i>

<b>3. Select the button</b>

  <u>Video-option</u>: Give video/file in video format
  <u>File-option</u>: Give video/file in file format
   
<b>๐ Special feature: Set caption to any file you want! โจ</b>

๐น Select an uploaded file/video or forward me <b>Any Telegram File</b> and just write the text you want to be on the file <b>as a reply to the file</b> by selecting it (as replying to a message) and the text you wrote will be attached as caption! ๐คฉ

Ex: <a href='https://telegra.ph/file/198bcda5944f787373122.jpg'>Send Like This! It's Easy</a> ๐ฅณ"""
    REPLY_TO_MEDIA_ALBUM_TO_GEN_THUMB = "Reply /generatecustomthumbnail to a media album, to generate custom thumbail."
    ERR_ONLY_TWO_MEDIA_IN_ALBUM = """Media Album should contain only two photos. Please re-send the media album, and then try again, or send only two photos in an album."
You can use /rename command after receiving file to rename it with custom thumbnail support.
"""
    CANCEL_STR = "Process Cancelled."
    ZIP_UPLOADED_STR = "Uploaded {} files in {} seconds."
    SLOW_URL_DECED = "Gosh that seems to be a very slow URL. Since you were screwing my home, I am in no mood to download this file. Meanwhile, why don't you try this:==> https://shrtz.me/PtsVnf6 and get me a fast URL so that I can upload to Telegram, without me slowing down for other users."
