
$( document ).ready(function() {


    $(".select-level").change(function(ev) {

            ev.preventDefault();

            levels = {}

            $(".select-level").each(function() {

                levels[$(this).attr('id')] = $(this).prop('checked')
            })

            console.log(levels)

            $(".entry").each(function() {
                level = $(this).data("level")

                if (levels[level] == true) {
                    $(this).show()
                } else {
                    $(this).hide()
                }
            })
    })

    $(".entry").click(function(ev) {
        
        ev.preventDefault();
        id = $(this).attr("id")

        traduction =  $(this).find(".translation").text()

        console.log(data[id])

        text = ""
        table = ""
        for(var i = 0;i < data[id].length;i++)
        {
            elm = data[id][i]
            if (elm.is_vocabulary)
            {
                text += '<span class="badge bg-primary">' + elm.text +"</span> "
                table += "<tr><td>"+elm.text+"</td><td>"+elm.lemma+"</td><td>"+elm.pos+"</td><td>"+elm.level+"</td></tr>"
            }
            else
            {
                text += "<span>" + elm.text +"</span> "
            }
        }

        console.log(text)


        $('#details').find(".modal-body-text").html(text)

        $('#details').find(".modal-body-table").html(table)
        $('#details').find(".modal-body-translation").text(traduction)
        

        $('#details').modal('show');
    })



});