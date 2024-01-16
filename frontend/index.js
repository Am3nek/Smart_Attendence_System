
console.log("Works")
const getAPI=()=>{
//e.preventDefault();
    console.log("Reached");
    let a=document.getElementById('regno').value
    fetch(`http://127.0.0.1:8000/SData/${a}`).then(data=>data.json()).then(d=>{
        if(d.val=='A'){
            document.getElementById('absent').style.display='block';
            document.getElementById('present').style.display='none';
            console.log("A")
        }else if(d.val=='P'){
            document.getElementById('present').style.display='block';
            document.getElementById('absent').style.display='none';
            console.log("P")
        }
    }).catch(e=>
    console.log(e)
    );
}