import json
f = open('settings.json',)
d = json.load(f)
block_width=d["size"]["block width"]
block_height=d["size"]["block height"]
ww=d["size"]["window width"]*block_width
wh=d["size"]["windows height"]*block_height
full_screen=d["full screen"]
aud=d["audio"]
m_font_size=d["msg"]["font size"]
m_font_color=d["msg"]["font color"]
m_font_type=d["msg"]["type"]
hbb=d["size"]["happy birthday banner height"]
score_font_size=d["score"]["font size"]
score_font_color=d["score"]["color"]
score_type=d["score"]["type"]
speed=d["speed"]
speed_increment=d["speed increment"]
f.close()