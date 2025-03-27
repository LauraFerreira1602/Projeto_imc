from flask import Flask, jsonify
from flask_pydantic_spec import FlaskPydanticSpec

app = Flask(__name__)
spec = FlaskPydanticSpec('flask',
                         title='First API - SENAI',
                         version = '1.0.0')
spec.register(app)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

@app.route('/imc/<peso>/<altura>')
def imc(peso, altura):
    """
        API para calcular o IMC

        ## Endpoint:
        'GET /imc/<peso>/<altura>'

        ## Parâmetros:
        - 'peso' - (float): peso do IMC
        - 'altura' - (float): altura do IMC
            - ** Qualquer outro formato resultara em erro. **

        ## Resposta (JSON):
        ''' json
        {
            "peso":
            "altura":
        }
        '''

        ## Erros possiveis:
        - Se não for numero, retornara em {"erro":"Digite somente numeros"}

        """
    try:
        peso = float(peso)
        altura = float(altura)
        resultado = peso / (altura * altura)

        if resultado < 18:
            msn = 'Esta pessoa esta abaixo do peso'

        elif resultado < 25:
            msn ='Esta pessoa esta com o Peso normal'

        elif resultado < 29:
            msn = 'Esta pessoa esta em excesso de peso'

        elif resultado < 34:
            msn = 'Esta pessoa esta com obesidade classe 1'

        elif resultado < 39:
            msn = 'Esta pessoa esta com obesidade classe 2'

        else:
            msn = 'esta pessoa esta com obesidade classe 3'

        return jsonify( {"mensagem": msn,
                "valor": resultado}
                )

    except ValueError:
        return jsonify( {"erro":"Digite somente numeros"}
                        )



if __name__ == '__main__':
    app.run(debug=True)
