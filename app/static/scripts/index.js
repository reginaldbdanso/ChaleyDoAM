const modal = document.getElementById("editModal");
// Get the button that opens the modal
const editbtn = document.getElementById("editBtn");
// Get the <span> element that closes the modal
const span = document.getElementsByClassName("close")[0];
// // When the user clicks the button, open the modal 
// editbtn.onclick = function() {
//     alert("hello");
//   modal.style.display = "block";
// }

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}

function deleteTask(id) {
    const url = '/create_task/' + id;
    const domain = window.location.origin;
    const fullUrl = domain + url;
    fetch(fullUrl, {
        method: 'DELETE',
    })
        .then(response => {
            // if (!response.ok) {
            //     throw new Error('Network response was not ok');
            // }
            console.log(response);
            location.reload();
        })
        .catch((error) => {
            console.error('Error:', error);
        });
}

function editTask(id) {
    modal.style.display = "block";
    document.getElementById('editForm').addEventListener('submit', function(e) {
        e.preventDefault();  // Prevent the form from being submitted normally
    
        const url = '/create_task/' + id;
        const domain = window.location.origin;
        const fullUrl = domain + url;
    
        fetch(fullUrl, {
            method: 'PUT',
            body: new FormData(e.target)  // This sends the form data
        })
        .then(response => {
            // modal.style.display = "none";
            console.log(response);
            location.reload();
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            // Handle the response here
        })
        .catch((error) => {
            console.error('Error:', error);
        });
    });
    // const url = '/create_task/' + id;
    // const domain = window.location.origin;
    // const fullUrl = domain + url;
    // fetch(fullUrl
    // )
    // // .then(response => response.json())
    // .then(task => {
    //     // Populate the modal with the current values of the task
    //     document.getElementById('mtitle').value = task.title;
    //     document.getElementById('mdescription').value = task.description;
    //     document.getElementById('mdue_date').value = task.due_date;
    //     // Show the modal
    //     document.getElementById('editModal').style.display = "block";
    // });

    // // When the form is submitted, send a PUT request to the server to update the task
    // document.getElementById('editForm').addEventListener('submit', function(event) {
    //     event.preventDefault();
    //     fetch('/tasks/' + id, {
    //         method: 'PUT',
    //         body: new FormData(event.target)  // This sends the form data
    //     })
    //     .then(response => {
    //         if (!response.ok) {
    //             throw new Error('Network response was not ok');
    //         }
    //         // Reload the page to reflect the changes
    //         location.reload();
    //     })
    //     .catch((error) => {
    //         console.error('Error:', error);
    //     });
    // });
}


// Get the modal

// function saveToLocalStorage() {
//     const data = { key: 'value' };  // Replace with your data
//     localStorage.setItem('myData', JSON.stringify(data));

//     // Send data to the server (Flask in this case)
//     fetch('/save_data', {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json'
//         },
//         body: JSON.stringify(data)
//     })
//     .then(response => response.json())
//     .then(result => console.log(result))
//     .catch(error => console.error('Error:', error));
// }

// // Retrieve data from local storage
// function retrieveFromLocalStorage() {
//     const storedData = localStorage.getItem('myData');
//     const parsedData = JSON.parse(storedData);
//     console.log(parsedData);
// }