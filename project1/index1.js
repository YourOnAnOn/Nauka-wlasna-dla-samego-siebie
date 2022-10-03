let btn=document.querySelector('#new-content');
let quote = document.querySelector('.quote');
let person = document.querySelector('.person-who-said');

const quotes = [
{
    quote: "Baca mówi, że walas nie umie się całować!",
    person: "Anonim"
},
{
    quote: "Amogus",
    person: "SUS guy"
},
{
    quote: "All my friends masturbate in religion class",
    person: "OnAnOn#2137"
},
];

btn.addEventListener('click', function(){

    let random = Math.floor(Math.random()*quotes.length);

    quote.innerText = quotes[random].quote;

    person.innerText = quotes[random].person;

});