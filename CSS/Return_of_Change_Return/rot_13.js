'use strict';

var input 

function decrypter(crypString, rotation) {
    //
    var alphabet = 'abcdefghijklmnopqrstuvwxyz';
    var cypherFormer = alphabet.slice();
    var cypherLatter = alphabet.slice();
    var cypherProper = cypherLatter + cypherFormer
    // var caesar13 = 'nopqrstuvwxyzabcdefghijklm';
    var degarbled = '';

    for (var i=0;i<garbled.length;i++) {
        var crypChar = encoded[i];
        var crypLoc = caesar13.indexOf(crypChar);
        var decodedChar = alphabet[crypLoc];
        degarbled.push(decodedChar)
    }

    var eureka = degarbled.join('');
    alert(eureka);
}

decrypter('yynznf', 13);
