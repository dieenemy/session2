import datetime
now = datetime.datetime.now()

from gmail import GMail, Message

html_content = '''
<p>Ch&agrave;o sếp,</p>
<p>H&ocirc;m nay thức dậy, em thấy m&igrave;nh mệt mỏi. B&aacute;c sĩ bảo em bị <em><strong>ung thư giai đoạn cuối</strong></em> rồi&nbsp;<img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-cry.gif" alt="cry" /></p>
<p>Sếp cho em nghỉ ốm&nbsp;<img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-cry.gif" alt="cry" /></p>
<p>&nbsp;</p>
'''

gmail = GMail('dieenemy1994@gmail.com','tungmkqn123')
msg = Message('Đơn xin nghỉ ốm',to='dieenemy1996@gmail.com',html=html_content)

if now.hour == 7:
    gmail.send(msg)
else:
    print("not even 7am yet")

