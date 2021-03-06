#!/usr/bin/env python 
# -*- coding: utf-8 -*-


'''
代码修改自:
http://wangwei007.blog.51cto.com/68019/983289
但这个版本有BUG, 某些T发音的汉字,比如太,他,它等返回的是s, 这里有修正

取汉字字符串的首字母,比如 
get_pinyin_letter("我是汉字")
Output: 'wshz' 
'''

def get_pinyin_letter(str_input): 
    if isinstance(str_input, unicode): 
        unicode_str = str_input 
    else: 
        try: 
            unicode_str = str_input.decode('utf8') 
        except: 
            try: 
                unicode_str = str_input.decode('gbk') 
            except: 
                print 'unknown coding' 
                return 
    
    return_list = [] 
    for one_unicode in unicode_str: 
        return_list.append(_get_pinyin(one_unicode)) 
     
    return ''.join(return_list)
    
def _get_pinyin(unicode1): 
    str1 = unicode1.encode('gbk') 
    try:         
        ord(str1) 
        return str1 
    except: 
        asc = ord(str1[0]) * 256 + ord(str1[1]) - 65536 
        
        if asc >= -20319 and asc <= -20284: 
            return 'a' 
        if asc >= -20283 and asc <= -19776: 
            return 'b' 
        if asc >= -19775 and asc <= -19219: 
            return 'c' 
        if asc >= -19218 and asc <= -18711: 
            return 'd' 
        if asc >= -18710 and asc <= -18527: 
            return 'e' 
        if asc >= -18526 and asc <= -18240: 
            return 'f' 
        if asc >= -18239 and asc <= -17923: 
            return 'g' 
        if asc >= -17922 and asc <= -17418: 
            return 'h' 
        if asc >= -17417 and asc <= -16475: 
            return 'j' 
        if asc >= -16474 and asc <= -16213: 
            return 'k' 
        if asc >= -16212 and asc <= -15641: 
            return 'l' 
        if asc >= -15640 and asc <= -15166: 
            return 'm' 
        if asc >= -15165 and asc <= -14923: 
            return 'n' 
        if asc >= -14922 and asc <= -14915: 
            return 'o' 
        if asc >= -14914 and asc <= -14631: 
            return 'p' 
        if asc >= -14630 and asc <= -14150: 
            return 'q' 
        if asc >= -14149 and asc <= -14091: 
            return 'r' 
        if asc >= -14090 and asc <= -13319: 
            return 's' 
        if asc >= -13318 and asc <= -12839: 
            return 't' 
        if asc >= -12838 and asc <= -12557: 
            return 'w' 
        if asc >= -12556 and asc <= -11848: 
            return 'x' 
        if asc >= -11847 and asc <= -11056: 
            return 'y' 
        if asc >= -11055 and asc <= -10247: 
            return 'z' 
        return '' 
    
