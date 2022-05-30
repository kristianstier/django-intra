$(document).ready(
    function(){
        // Mobile menu
        $("#show_mobile_menu").click(function(){
            if(!$("#mobile_menu").hasClass("active")){
                $("body").append("<div id='shadow' class='mobile'></div>");
                setTimeout(() => {
                    $("#mobile_menu").addClass("active");
                    $("#shadow").addClass("active");
                }, 100);
            }

        });
        $("#hide_mobile_menu").click(function(){
            if($("#mobile_menu").hasClass("active")){
                $("#shadow").removeClass("active");
                $("#mobile_menu").removeClass("active");
                setTimeout(() => {
                    $("#shadow").remove();
                }, 100);
            }
        });
    }
);

let compare_function = {
    compare: (a, b) => {
        let ax = a.toLowerCase();
        let bx  = b.toLowerCase();
        return ax.localeCompare(bx);
    }
}

let pagination = {
    enabled: true,
    limit: 10,
    summary: false
}

let language = {
    'search': {
        'placeholder': 'Search for employee'
    }
}

function render_user_table(usersJSON){
    users = $.parseJSON(usersJSON)
    let data = Array();
    users.forEach(element => {
        let arr = Object.values(element);
        for(key in arr){
            if(arr[key] === "" || arr[key] === null){
                arr[key] = "---";
            }
        }
        data.push(arr);
    });
    new gridjs.Grid({
        columns: [
            {
                name: "ID",
                hidden: true
            },
            {
                name: "",
                attributes: {"style":"width:100px;padding:0px;text-align:center;"},
                sort: false,
                search: false,
                formatter: function(cell, row){
                    if(cell != "---"){
                        return gridjs.html(`<a href="${window.location.origin+'/user/'+row.cells[0].data+'/'}"><image class="profil_image" src="${window.location.origin+'/'+cell}"/></a>`);
                    }
                    else return cell;
                }
            },
            {
                name: "Firstname",
                attributes: {"style":"text-align:left;"},
            },
            {
                name: "Lastname",
                attributes: {"style":"text-align:left;"},
            },
            {
                name: "Department",
                attributes: {"style":"text-align:left;"},
            },
            {
                name: "Action",
                search: false,
                sort: false,
                attributes: {"style":"text-align:left;width:160px;"},
                formatter: function(cell, row){
                    return gridjs.html(`<a class="profil_link" href="${window.location.origin+'/user/'+row.cells[0].data+'/'}">Details<a/>`);
                }
            },
        ],
        data: data,
        sort: compare_function,
        search: {enabled:true},
        pagination: pagination,
        language: language,
        width: "100%"
    }).render(document.getElementById("userTable"));
}