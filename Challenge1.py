__author__ = 'DavidGinzberg'
#http://www.pythonchallenge.com/pc/def/map.html

"""
Hint:
K -> M
O -> Q
E -> G
"""

def main():
    cypher = str.maketrans("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
                       "cdefghijklmnopqrstuvwxyzabCDEFGHIJKLMNOPQRSTUVWXYZAB")

    cyphertext = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr\
    ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj"

    cyphertext.translate(cypher)
    urlcypher = "map"
    cyphertext.translate(urlcypher)

