from flask import Flask, render_template, request
from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate

app = Flask(__name__)

def transliterate_text(text, source_script, target_script):
    return transliterate(text, source_script, target_script)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form.get('text', '')
        source_script = request.form.get('source_script', 'DEVANAGARI')
        target_script = request.form.get('target_script', 'IAST')
        
        # Ensure correct script schemes are used
        source_script = getattr(sanscript, source_script.upper(), sanscript.DEVANAGARI)
        target_script = getattr(sanscript, target_script.upper(), sanscript.IAST)
        
        result = transliterate_text(text, source_script, target_script)
        return render_template('index.html', result=result, text=text)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
