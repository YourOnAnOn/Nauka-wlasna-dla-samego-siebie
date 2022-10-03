let a = document.getElementById('a');
let b = document.getElementById('b');
let c = document.getElementById('c');
let openBtn = document.getElementById('button');
let field = document.getElementById('field');

 
openBtn.addEventListener('click', function(){
    field = (a+b+c)/2;
    field.style.display = 'field';
    
});