import random

desafios = {

    "matematica": {

        1: [

            {
                "pergunta":"2 + 3 = ?",
                "resposta":"5"
            },

            {
                "pergunta":"5 + 7 = ?",
                "resposta":"12"
            },

            {
                "pergunta":"2,4,6,8, ?",
                "resposta":"10"
            }

        ],

        2: [

            {
                "pergunta":"12 x 3 = ?",
                "resposta":"36"
            },

            {
                "pergunta":"50 / 5 = ?",
                "resposta":"10"
            }

        ]

    },

    "logica": {

        1: [

            {

                "pergunta":"Se João estuda e João estuda, João passa? (sim/nao)",

                "resposta":"sim"

            },

            {

                "pergunta":"Negação de 'Está chovendo'?",

                "resposta":"nao esta chovendo"

            }

        ],

        2: [

            {

                "pergunta":"Todos os dragões voam. Draco é dragão. Draco voa? (sim/nao)",

                "resposta":"sim"

            }

        ]

    },

    "sequencia": {

        1: [

            {

                "pergunta":"2,4,8,16, ?",

                "resposta":"32"

            },

            {

                "pergunta":"1,1,2,3,5, ?",

                "resposta":"8"

            }

        ],

        2: [

            {

                "pergunta":"3,6,12,24, ?",

                "resposta":"48"

            }

        ]

    }

}


def obter_desafio(categoria, nivel):

    if nivel not in desafios[categoria]:

        nivel = max(desafios[categoria].keys())

    return random.choice(desafios[categoria][nivel])