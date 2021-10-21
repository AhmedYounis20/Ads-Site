function favpost(url,id){
fetch(url,{
    method:"POST",
    mode:'cors',
    cache:'no-cache',
    credentials:"same-origin",
    headers:{
        'content_type':'application/x-www-form-urlencoded',

    },
    redirect:'follow',
    referrer:'no-referrer',
}).then(function(data){
    console.log('url','finished');
    $('#unfavorite_star_'+id).toggle();
    $('#favorite_star_'+id).toggle();
}).catch(()=>{
    console.log(url,'error')
})
    
}