const TEXT_FILES_SELECTED_COUNTER = " FILES SELECTED"; // Prepend number to this string
const TEXT_FILES_UPLOADING = "UPLOADING "; // Append dots to this string


var BUTTON_FILE_PICKER = null;
var LABEL_BUTTON_FILE_PICKER = null;
var BUTTON_FILE_UPLOADER = null;
var LABEL_BUTTON_FILE_UPLOADER = null;
var DIV_FILES_STATUS_INDICATOR = null;

window.addEventListener("load", function() 
{
    BUTTON_FILE_PICKER = document.getElementById("file_picker");
    LABEL_BUTTON_FILE_PICKER = document.getElementById("file_picker_label");
    BUTTON_FILE_UPLOADER = document.getElementById("file_uploader");
    LABEL_BUTTON_FILE_UPLOADER = document.getElementById("file_uploader_label");
    DIV_FILES_STATUS_INDICATOR = document.getElementById("files_status_indicator");    
});

function return_home(specific_message="")
{
    toggle_ui_button(BUTTON_FILE_PICKER, LABEL_BUTTON_FILE_PICKER, true);
    toggle_ui_button(BUTTON_FILE_UPLOADER, LABEL_BUTTON_FILE_UPLOADER, false);
    DIV_FILES_STATUS_INDICATOR.innerText = specific_message.length > 0 ? specific_message : "0" + TEXT_FILES_SELECTED_COUNTER;
}

function toggle_ui_button(input_element, label_element, is_enabled)
{
	if(is_enabled == true)
	{
		input_element.removeAttribute("disabled");
		label_element.classList.remove("disabled_button_ui");
	}
	else
	{
		input_element.setAttribute("disabled", true);
		label_element.classList.add("disabled_button_ui");
	}    
}

function set_selected_files(event)
{
    let file_list = BUTTON_FILE_PICKER.files;
    DIV_FILES_STATUS_INDICATOR.innerText = String(file_list.length) + TEXT_FILES_SELECTED_COUNTER;

    if(file_list.length > 0)
    {
        toggle_ui_button(BUTTON_FILE_UPLOADER, LABEL_BUTTON_FILE_UPLOADER, true);
    }
    else
    {
        toggle_ui_button(BUTTON_FILE_UPLOADER, LABEL_BUTTON_FILE_UPLOADER, false);
    }
}

function upload_selected_files(event)
{
    let is_pending = false;
    let post_req = null;
    let file_index = 0;
    toggle_ui_button(BUTTON_FILE_PICKER, LABEL_BUTTON_FILE_PICKER, false);
    toggle_ui_button(BUTTON_FILE_UPLOADER, LABEL_BUTTON_FILE_UPLOADER, false);

    function animate_while_pending(dot_amount)
    {
        function action()
        {
            if(is_pending == true)
            {
                DIV_FILES_STATUS_INDICATOR.innerText = TEXT_FILES_UPLOADING + ".".repeat(dot_amount);
                animate_while_pending(dot_amount < 3 ? dot_amount + 1 : 0);
            }
        }

        window.setTimeout(action, 100);
    }

    function on_response()
    {
        // 4 means done
        if(post_req.readyState != 4)
        {
            return; // Leave this function temporarily.
        } 

        is_pending = false;
        file_index = file_index + 1;

        // 200 is OK
        if(post_req.status != 200) 
        {
            return_home("SERVER DID NOT RETURN AN OK MESSAGE");
        }
        else if(file_index < BUTTON_FILE_PICKER.files.length)
        {
            upload_file();
        }
        else
        {
            return_home();
        }
    }

    function upload_file()
    {
        let file = BUTTON_FILE_PICKER.files[file_index];

        post_req = new XMLHttpRequest();
        post_req.onreadystatechange = on_response;
        post_req.open("POST", "/upload", true);

        let form_data = new FormData();
        form_data.append("file", file);

        post_req.send(form_data);

        is_pending = true;

        animate_while_pending(0);
    }

    upload_file()
}