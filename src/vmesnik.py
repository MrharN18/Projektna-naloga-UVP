import bottle, model

minolovec = model.Minolovec()


@bottle.get('/')
def prva_stran():
    return bottle.template('src/views/index.html')


@bottle.post('/novaigra/')
def novaigra():
    tezavnost = bottle.request.forms.get('tezavnost')
    id = minolovec.nova_igra(int(tezavnost))
    igra = minolovec.igre[id]

    return bottle.template('src/views/igra.tpl', igra=igra)

@bottle.post('/igra/')
def igra():
    gumb = bottle.request.forms.get('gumb')
    id, x, y = gumb.split('-')
    igra = minolovec.igre[int(id)]
    igra.klik(int(x), int(y))
    
    return bottle.template('src/views/igra.tpl', igra=igra)



@bottle.get('/zmaga/')
def zmaga():
    return bottle.template('src/views/zmaga.html')


@bottle.get('/poraz/')
def poraz():
    return bottle.template('src/views/poraz.html')


bottle.run(reloader=True)