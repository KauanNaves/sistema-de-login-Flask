from flask import redirect, url_for, g
import functools
# Funções auxiliares para verificação de Login do usuário

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('login'))

        return view(**kwargs)

    return wrapped_view

