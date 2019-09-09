<!DOCTYPE html>
<html>
<head>
<title>Minolovec</title>
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
</head>
<body>
<div style="margin-top:50px;">
<center>
<form action="/igra/" method="post">
<table>

% for i in range(igra.velikosty):
<tr>
% for j in range(igra.velikostx):

% if igra.tabela[i][j].odkrito:

% if igra.tabela[i][j].stevilka == 0 and not igra.tabela[i][j].mina:
<th><center><button class="btn btn-success" style='background-color: #c1e0c9; margin: 0px 0px; width:37px; height:37px;' disabled></button></center></th>
% elif igra.tabela[i][j].mina and igra.tabela[i][j].odkrito:
<th><button class="btn btn-success" style='background-color: #024f2e;margin: 0px 0px; width:37px; height:37px;'></button></th>
% else:
<th><button class="btn btn-success" style='background-color: #c1e0c9; color: #000000; margin: 0px 0px; width:37px; height:37px;' disabled>{{igra.tabela[i][j].stevilka}}</button></th>
% end

% else:
<th><button name='gumb', value='{{igra.id}}-{{j}}-{{i}}', type='submit' class="btn btn-success" style='background-color: #28a745; margin: 0px 0px; width:37px; height:37px;'></button></th>
% end

% end
</tr>
% end

</table>
</form>

<br>
<br>

<form action="/novaigra/" method="post">
    <select name='tezavnost' class="custom-select w-25">
        <option value='1'>Easy</option>
        <option value='2'>Medium</option>
        <option value='3'>Hard</option>
    </select>
    <br>
    <br>
    <button type="submit" class="btn btn-success">Nova igra</button>
</form>

</center>
% if igra.zmaga():
<script>
setTimeout(function() {
window.location.href = "/zmaga/";
}, 1000);
</script>
%elif igra.konec:
<script>
setTimeout(function() {
window.location.href = "/poraz/";
}, 1000);
</script>
% end
% end
</div>
</body>

<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>

</html>