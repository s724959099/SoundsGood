window.myAjax =
    _base: (type, urlStr, obj, callback)->
        ###
         base ajax function
        ###
        option =
            url: urlStr,
            type: type,
            dataType: "json",
            success: (data, textStatus, jqXHR)->
                data["xhr"] = jqXHR
                callback(data)
            error: (jqXHR, textStatus)->
                data =
                    xhr: jqXHR

                callback(data)
        if type != "GET"
            option["contentType"] = "application/json"

        if obj != null
            data = if type == "GET" then obj else JSON.stringify(obj)
            option["data"] = data
        $.ajax(option)

    _baseSync: (type, urlStr, obj)->
        ###
         base ajax function
        ###
        response = {}
        option =
            url: urlStr,
            type: type,
            async: false
            dataType: "json",
            success: (data, textStatus, jqXHR)->
                response = data
                response["xhr"] = jqXHR
            error: (jqXHR, textStatus)->
                response["xhr"] = jqXHR

        if type != "GET"
            option["contentType"] = "application/json"
        if obj != null
            data = if type == "GET" then obj else JSON.stringify(obj)
            option["data"] = data
        $.ajax(option)
        return response

    get: (urlStr, obj, callback)->
        @_base("GET", urlStr, obj, callback)
    post: (urlStr, obj, callback)->
        @_base("POST", urlStr, obj, callback)
    put: (urlStr, obj, callback)->
        @_base("PUT", urlStr, obj, callback)
    delete: (urlStr, obj, callback)->
        @_base("DELETE", urlStr, obj, callback)

    getSync: (urlStr, obj)->
        @_baseSync("GET", urlStr, obj)
    postSync: (urlStr, obj)->
        @_baseSync("POST", urlStr, obj)
    putSync: (urlStr, obj)->
        @_baseSync("PUT", urlStr, obj)
    deleteSync: (urlStr, obj)->
        @_baseSync("DELETE", urlStr, obj)


window.print = (str)->
    console.log(str)

###
    set trigger and listen
###
event = # an object
    clientList: [] #init
    triggerArgs: [] #init
    clear: ->
        @clientList = []
        @triggerArgs = []
    listen: (key, fn) ->
# if key not exist  then create an array
        if !@clientList[key]
            @clientList[key] = []

        # input to listen
        @clientList[key].push fn

        # if trigger before listen then still trigger
        if @triggerArgs[key]
            for args in @triggerArgs[key]
                fn.apply(@, args)

        return
    trigger: ->
# get key
        key = Array::shift.call(arguments)
        #get all fns in key
        fns = @clientList[key]

        # init triggerArgs in key
        if !@triggerArgs[key]
            @triggerArgs[key] = []
        @triggerArgs[key].push(arguments)

        #if not found fns
        if !fns or fns.length == 0
            return false

        # do fn which all in key
        i = 0
        fn = undefined
        while fn = fns[i++]
            fn.apply @, arguments
        return

installEvent = (obj) ->
# get new obj and set all key from event
    for key of event
        obj[key] = event[key]
    return obj
# create for all
window.CloudesignEvents = installEvent({})


window.mySerialize = {
    serialize_value_to_bool: (data, name)->
        for obj,index in data
            new_obj = obj

            if obj.name == name
                if obj.value == "True"
                    new_obj["value"] = true
                else if obj.value == "False"
                    new_obj["value"] = false
            data[index] = new_obj
    serialize_value_to_null: (data, name)->
        for obj,index in data
            new_obj = obj

            if obj.name == name
                if obj.value == ""
                    new_obj["value"] = null
            data[index] = new_obj

    serialize_value_to_remove: (data, name)->
        for obj,index in data
            new_obj = obj

            if obj.name == name
                debugger
                data.splice(index, 1)
                break
    serialize_to_obj: (data)->
        new_obj = {}
        for obj,index in data
            new_obj[obj.name] = obj.value
        data = new_obj
        return new_obj
    obj_to_serialize: (obj, exceptList)->
        data = []
        exceptList = if exceptList == undefined then [] else exceptList
        for key,val of obj
            if key in exceptList
                continue
            data.push({
                name: key,
                value: val
            })
        return data
    lowercase_to_specifyValue: (datas, value)->
        for obj,index in datas
            new_obj = obj
            if obj.name == value.toLowerCase()
                new_obj["name"] = value
            datas[index] = new_obj


}


window.remove_data_items = (data, idName, constrain)->
    for obj,index in data
        if obj[idName] == constrain
            data.splice(index, 1)
            break


window.dataProcess = {
    isIndata: (data, idName, val)->
        for obj,index in data
            if obj[idName] == val
                return true
        return false

    remove_data_by_id: (data, idName, val)->
        new_data = []
        for obj,index in data
            if obj[idName] != val
                new_data.push(obj)
        return new_data

}


window.myCookies = {
    getTenantCompanyId: ->
        JSON.parse(Cookies.get("Tenant")).CompanyId
    getCompanyId: ->
        CompanyId = Cookies.get("CompanyId")
    isDesigner: ->
        CompanyId = Cookies.get("CompanyId")
        return JSON.parse(Cookies.get("Tenant")).CompanyId == CompanyId

}

Vue.options.delimiters = ['${', '}']


