vm = new Vue(
    el:"#app"
    data:{
        old_text:null
        new_text:null
    }
    methods:{
        submit:->
            if old_text!=null
                obj={
                    text:@old_text
                }
                data=myAjax.postSync("/api/dbmodel/init",obj)
                console.log(data)
                @new_text=data.msg
    }
)

$ ->
    new Clipboard('#copy')