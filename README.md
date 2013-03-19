python 取汉字的拼音首字母
========

代码修改自:
http://wangwei007.blog.51cto.com/68019/983289
但这个版本有BUG, 某些T发音的汉字,比如'太','他','它'等返回的是s, 这里有修正

取汉字字符串的首字母,比如 
get_pinyin_letter("我是汉字")
Output: 'wshz' 
