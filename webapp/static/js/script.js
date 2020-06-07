function show_filters() {
    let elem=document.getElementById("serch_filter").style;
    if (elem.display == "none"){
        elem.display = "block";
    }
    else{
        elem.display = "none";
    }
        
}
document.getElementById("serch_filter").style.display="none";

function fill_filter(){
    let url=window.location.href;
    let api_values;
    if (url.split('?')[1]){
        api_values=url.split('?')[1].split('&');
    }
    else{
        return;
    }
    
    var api={
        q: api_values[0].split("="),
        due_date: api_values[1].split("="),
        status: api_values[2].split("="),
        label: api_values[3].split("="),
    };
    let q=document.getElementById("id_search");
    let due_date=document.getElementById("id_due_date");
    let status=document.getElementById("id_status");
    let label=document.getElementById("id_label");

    let c=0;
    if(api["q"]){
        q.value=api["q"][1];
        c=1;
    }
    if(api["due_date"]){
        due_date.value=api["due_date"][1];c=1;
    }
    if(api["label"]){
        label.value=api["label"][1];c=1;
    }
    if(api["status"]){
        status.value=api["status"][1];c=1;
    }
    if(c){
        show_filters();
    }
}
fill_filter();
