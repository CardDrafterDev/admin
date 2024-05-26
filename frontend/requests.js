const viewCards = () => {
    fetch('http://127.0.0.1:8080/admin/cards', {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
        },
    }).then(res => {
        return res.json()
    }).then(data => {
        console.log(data)
    })
}

const login = () => {
    let password = document.querySelector('input[type="password"]').value
    let username = document.querySelector('input[type="text"]').value
    if (password && username) {
        fetch('http://127.0.0.1:8080/admin/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                username: username,
                password: password
            })
        }).then(res => {
            return res.json()
        }).then(data => {
            if (data == 202){
                window.location.href = 'adminPanel.html'
            }
        })


        
    }
}