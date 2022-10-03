from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate


from flask import Flask , jsonify
app =Flask(__name__)



@app.route('/lang/<string:l1>/<string:l2>')
def get_trans(l1,l2):

    if(l1=='hin'):
        result = jsonify(transliterate(l2, sanscript.DEVANAGARI ,sanscript.ITRANS).lower())

    if(l1=='guj'):
        result = jsonify(transliterate(l2, sanscript.GUJARATI ,sanscript.ITRANS).lower())

    if(l1=='mal'):
        result = jsonify(transliterate(l2, sanscript.MALAYALAM ,sanscript.ITRANS).lower())

    if(l1=='ori'):
        result = jsonify(transliterate(l2, sanscript.ORIYA ,sanscript.ITRANS).lower())

    if(l1=='tam'):
        result = jsonify(transliterate(l2, sanscript.TAMIL ,sanscript.ITRANS).lower())

    if(l1=='kan'):
        result = jsonify(transliterate(l2, sanscript.KANNADA ,sanscript.ITRANS).lower())

    if(l1=='tel'):
        result = jsonify(transliterate(l2, sanscript.TELUGU ,sanscript.ITRANS).lower())

    result.headers.add('Access-Control-Allow-Origin', '*')
    return result

 
if __name__=='__main__':
    app.run(debug=True)