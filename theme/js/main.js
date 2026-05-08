document.onreadystatechange = () => {
    if (document.readyState === "complete") {
        init();
    }
};

function init(){
    const copyBtns = document.querySelectorAll("div.code button.copy")
    copyBtns.forEach((copyBtn) => {
        copyBtn.addEventListener("click", (event) => {
            const codeText = copyBtn.previousElementSibling.innerText

            copyToClipboard(codeText).then(
                /* success */
                () => {
                    copyBtn.innerText = "Copied!" 
                    copyBtn.style.borderColor = '#2a8e29'
                    copyBtn.style.color = '#2a8e29'
                    setTimeout(() => {
                        copyBtn.innerText = "Copy"
                        copyBtn.style.borderColor = ""
                        copyBtn.style.color = ""

                    }, 800) 
                },
                /* failure */
                () => {
                    copyBtn.innerText = "Couldn't copy!" 
                    setTimeout(() => {
                        copyBtn.innerText = "Copy"
                        copyBtn.style.borderColor = ""
                        copyBtn.style.color = ""

                    }, 800) 
                }
        )

        }
        )
    }
    )
}

function copyToClipboard(text){
    return new Promise((resolve, reject) => {
        if (navigator.clipboard) {
            navigator.clipboard.writeText(text).then(() => resolve(), () => reject())
        }
        else { 
            //ugly fallback 
            const textArea = document.createElement("textarea")
            textArea.value = text
            textArea.setAttribute('readonly', '')
            textArea.style.position = 'absolute'
            textArea.style.left = '-9999px'

            document.body.appendChild(textArea)

            textArea.select()
            document.execCommand('copy')
            document.body.removeChild(textArea)

            resolve()
        }
    }
    )
}
