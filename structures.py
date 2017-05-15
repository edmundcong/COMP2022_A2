# define set for variables and terminals
terminals = {
        "+", "-", "*", "0", "1", "2", "3", "a", "b", "c", "d", "print", "\"", "if", "else", "{", "}", "(", ")", ";", "$"
}
variables = {  # redefine P' to Q and K' to R for key'ing ease
        "P", "Q", "L", "K", "R", "W", "C'", "C", "E", "O", "V", "T"
}
parse_table = {
        "P": {
                "print": "LQ",
                "if": "LQ"
        },
        "Q": {
                "print": "LQ",
                "if": "LQ",
                "}": "",
                "$": ""
        },
        "L": {
                "print": "K;",
                "if": "C'"
        },
        "K": {
                "print": "print R"
        },
        "R": {
                '"': '"W"',
                "(": "E"
        },
        "W": {
                "a": "TW",
                "b": "TW",
                "c": "TW",
                "d": "TW",
                '"': ""
        },
        "C'": {
                "if": "if E { P } C"
        },
        "C": {
                "else": "else { P }",
                "}": "",
                "$": ""
        },
        "E": {
                "0": "V",
                "1": "V",
                "2": "V",
                "3": "V",
                "(": "(EOE)"
        },
        "O": {
                "+": "+",
                "-": "-",
                "*": "*"
        },
        "V": {
                "0": "0",
                "1": "1",
                "2": "2",
                "3": "3"
        },
        "T": {
                "a": "a",
                "b": "b",
                "c": "c",
                "d": "d"
        }
}
