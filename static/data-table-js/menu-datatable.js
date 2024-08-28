// Function to fetch data from the API


const csrfToken = getCookie('csrftoken');  // Replace 'csrftoken' with your CSRF token's name if different
const jwtToken = localStorage.getItem('access_token');


async function fetchDataFromAPI() {

    // Or sessionStorage, depending on where you store it
    console.log(jwtToken);

    try {
        const response = await fetch('http://127.0.0.1:8000/api/menu/items/', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken,
                'Authorization': `JWT ${jwtToken}`
            }
        });

        const data = await response.json();

        if (data && data.length > 0) {
            populateTable(data);
            createCarouselItems(data);
        } else {
            handleNoData();
        }
    } catch (error) {
        console.error('Error fetching data:', error);
        handleNoData();
    }
}

// Utility function to get the CSRF token from the cookie
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


// Function to handle no data scenario
function handleNoData() {
    const tableBody = document.getElementById('menuTableBody');
    tableBody.innerHTML = '<tr><td colspan="6" class="text-center">No data available</td></tr>';

    const carousel = document.getElementById('food-carousel');
    const noDataMessage = document.createElement('div');
    noDataMessage.classList.add('text-center', 'text-white');
    noDataMessage.textContent = 'No items to display in the carousel';
    carousel.appendChild(noDataMessage);
}

// Populate table with data
function populateTable(data) {
    console.log(data);
    const tableBody = document.getElementById('menuTableBody');
    tableBody.innerHTML = ''; // Clear existing rows

    data.forEach(item => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>
                <div class="form-check form-check-muted m-0">
                    <label class="form-check-label">
                        <input type="checkbox" class="form-check-input row-checkbox" />
                    </label>
                </div>
            </td>
            <td style="display: flex; align-items: center;">
                <img src="${item.image}" alt="image" class="rounded-circle" style="width: 35px; height: 35px; object-fit: cover;" />
                <span class="pl-2" style="flex-grow: 1; margin-left: 10px;">${item.name}</span>
            </td>
            <td>${item.category}</td>
            <td>${item.price}</td>
            <td>
                <div class="badge badge-outline-${item.availability > 0 ? 'success' : 'danger'}">
                    ${item.availability > 0 ? 'Available' : 'Out of Stock'}
                </div>
            </td>
            <td>
                <i class="fa fa-edit edit-icon" title="Edit" style="cursor: pointer; margin-right: 10px;"></i>
                <i class="fa fa-trash delete-icon" title="Delete" style="cursor: pointer; margin-right: 10px;"></i>
                <i class="fa fa-eye view-icon" title="View" style="cursor: pointer;"></i>
            </td>
        `;
        tableBody.appendChild(row);
    });

    // Initialize DataTable after populating the table
    var table = $('#menuTable').DataTable({
        "paging": true,
        "lengthChange": false,
        "pageLength": 5,
        "searching": false,
        "ordering": true,
        "info": true,
        "autoWidth": false,
        "responsive": true,
        "columnDefs": [
            { "orderable": false, "targets": 0 },  // Disable ordering for the checkbox column
            { "orderable": false, "targets": 5 }
        ],
        "orderMulti": true,  // Enable multiple column sorting
        // "order": [[1, 'asc']],  // Default sort by the second column (Item Name)

        "dom": 'Bfrtip',  // Include the export buttons in the DOM
        "buttons": [
            'copy', 'csv', 'excel', 'pdf', 'print'
        ]
    });
    // Attach event listeners for the icons
    // Handle opening and populating the edit modal
    document.querySelectorAll('.edit-icon').forEach((icon, index) => {
        icon.addEventListener('click', () => {
            const item = data[index];
            // document.getElementById('editItemName').value = item.name;
            populateEditModal(item);
            loadCategories('editItemCategory');
            $('#editModal').modal('show');
        });
    });

    // Save changes in the edit modal
    document.getElementById('saveEdit').addEventListener('click', () => {
        console.log('Save edited item');
        $('#editModal').modal('hide');
    });

    // Handle opening the delete confirmation modal
    document.querySelectorAll('.delete-icon').forEach((icon, index) => {
        icon.addEventListener('click', () => {
            Swal.fire({
                title: 'Are you sure?',
                text: 'Do you really want to delete this item?',
                icon: 'warning',
                showCancelButton: true,
                confirmButtonColor: '#3085d6',
                cancelButtonColor: '#d33',
                confirmButtonText: 'Yes, delete it!'
            }).then((result) => {
                if (result.isConfirmed) {
                    // Call your delete API here
                    fetch(`http://127.0.0.1:8000/api/menu/items/${data[index].id}`, {
                        method: 'DELETE',
                        headers: {
                            'Authorization': `JWT ${jwtToken}`
                        }
                    })
                        .then(response => {
                            if (response.ok) {
                                // If the response is ok (status 200-299), handle success
                                Swal.fire(
                                    'Deleted!',
                                    'The item has been deleted.',
                                    'success'
                                );
                                $('#menuTable').DataTable().destroy(); // Destroy DataTable to refresh
                                fetchDataFromAPI(); // Reload data
                            } else {
                                // If the response is not ok, parse the error message
                                return response.json().then(errorMessage => {
                                    Swal.fire(
                                        'Error!',
                                        errorMessage.message || 'There was a problem deleting the item.',
                                        'error'
                                    );
                                });
                            }
                        })
                        .catch(error => {
                            console.log(error);
                            Swal.fire(
                                'Error!',
                                'There was a problem connecting to the server.',
                                'error'
                            );
                        });
                }
            });
        });
    });

    // Handle opening and populating the view modal
    document.querySelectorAll('.view-icon').forEach((icon, index) => {
        icon.addEventListener('click', () => {
            const item = data[index];
            // document.getElementById('viewDetails').innerText = `Item Name: ${item.itemName}, Category: ${item.category}, Price: ${item.price}`;
            document.getElementById('itemImage').src = item.image;
            document.getElementById('itemName').textContent = item.name;
            document.getElementById('itemDescription').textContent = item.description;
            document.getElementById('itemCategory').textContent = item.category;
            document.getElementById('itemPrice').textContent = item.price;
            document.getElementById('itemAvailability').textContent = item.availability;

            $('#viewModal').modal('show');
        });
    });

    // Enable cancel buttons to hide the modals
    document.querySelectorAll('[data-dismiss="modal"]').forEach(button => {
        button.addEventListener('click', () => {
            // Reset the form
            document.getElementById('editItemImage').value = ''; // Clear the file input
            document.getElementById('uploadedItemImage').src = ''; // Clear the image preview
            document.getElementById('uploadedItemImage').style.display = 'none'; // Hide the image preview

            $('.modal').modal('hide');
        });
    });


    // Apply individual column search
    $('#menuTable thead tr:eq(1) th').each(function (i) {
        var title = $(this).text();
        $('input', this).on('keyup change', function () {
            if (table.column(i).search() !== this.value) {
                table
                    .column(i)
                    .search(this.value)
                    .draw();
            }
        });

        $('select', this).on('change', function () {
            table
                .column(i)
                .search(this.value)
                .draw();
        });
    });

    // Add event listeners for row selection
    document.querySelectorAll('.row-checkbox').forEach(checkbox => {
        checkbox.addEventListener('change', function () {
            if (this.checked) {
                this.closest('tr').classList.add('selected');
            } else {
                this.closest('tr').classList.remove('selected');
            }
        });
    });

    // Select/Deselect all rows
    document.getElementById('selectAllMenuItems').addEventListener('change', function () {
        const isChecked = this.checked;
        document.querySelectorAll('.row-checkbox').forEach(checkbox => {
            checkbox.checked = isChecked;
            if (isChecked) {
                checkbox.closest('tr').classList.add('selected');
            } else {
                checkbox.closest('tr').classList.remove('selected');
            }
        });
    });
}



document.getElementById('addItemForm').addEventListener('submit', function (event) {
    loadCategories('itemCategory');
    event.preventDefault(); // Prevent the form from submitting the default way

    // Collect form data
    const formData = new FormData(this); // FormData automatically handles file inputs
    console.log(formData.get('category'))
    // Append necessary fields to the formData object
    formData.append('name', formData.get('itemName'));
    formData.append('description', formData.get('itemDescription'));
    formData.append('category', formData.get('category'));
    formData.append('price', formData.get('price'));
    formData.append('image', formData.get('image')); // File input handling
    formData.append('availability', formData.get('availability'));

    // Send POST request
    fetch('http://127.0.0.1:8000/api/menu/items/', {
        method: 'POST',
        headers: {
            'Authorization': `JWT ${jwtToken}`
        },
        body: formData // No need to stringify FormData; it handles files correctly
    })
        .then(response => response.json())
        .then(data => {
            console.log(data);
            if (data.success) {
                // Show success alert
                Swal.fire({
                    title: 'Success!',
                    text: 'Item has been added successfully.',
                    icon: 'success',
                    confirmButtonText: 'OK'
                }).then(() => {
                    // Close modal after alert is confirmed
                    document.getElementById('addItemModal').querySelector('.btn-close').click();
                    // Optionally, refresh the data on the page or reset the form
                    document.getElementById('addItemForm').reset();
                });
            } else {
                // Handle the case where the response indicates an error
                Swal.fire({
                    title: 'Error!',
                    text: 'There was a problem adding the item. Please try again.',
                    icon: 'error',
                    confirmButtonText: 'OK'
                });
            }
        })
        .catch(error => {
            console.error('Error:', error);
            // Show error alert
            Swal.fire({
                title: 'Error!',
                text: 'An unexpected error occurred. Please try again.',
                icon: 'error',
                confirmButtonText: 'OK'
            });
        });
});


async function loadCategories(id) {
    try {
        const response = await fetch('http://127.0.0.1:8000/api/menu/categories/', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                // Replace with your actual CSRF token
                'Authorization': `JWT ${jwtToken}` // Replace with your actual JWT token
            }
        });

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const categories = await response.json();

        const categorySelect = document.getElementById(id);
        categorySelect.innerHTML = ''; // Clear current options

        categories.forEach(category => {
            const option = document.createElement('option');
            option.value = category.id;
            option.textContent = category.name;
            categorySelect.appendChild(option);
        });
    } catch (error) {
        console.error('Error fetching categories:', error);
    }
}


function populateEditModal(item) {
    // Populate the form fields with item data
    document.getElementById('editItemName').value = item.name;
    document.getElementById('editItemDescription').value = item.description;
    document.getElementById('editItemCategory').value = item.category;
    document.getElementById('editItemPrice').value = item.price;
    document.getElementById('currentItemImage').src = item.image; // Display the current image
    document.getElementById('editItemAvailability').value = item.availability;
    document.getElementById('saveEdit').value = item.id;

}
document.getElementById('editItemImage').addEventListener('change', function () {
    const file = this.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function (event) {
            const uploadedImage = document.getElementById('uploadedItemImage');
            uploadedImage.src = event.target.result;
            uploadedImage.style.display = 'block'; // Show the image
        };
        reader.readAsDataURL(file);
    } else {
        const uploadedImage = document.getElementById('uploadedItemImage');
        uploadedImage.src = '';
        uploadedImage.style.display = 'none'; // Hide the image if no file is selected
    }
});


// Save edited item
document.getElementById('saveEdit').addEventListener('click', async () => {
    const formData = new FormData();
    formData.append('name', document.getElementById('editItemName').value);
    formData.append('description', document.getElementById('editItemDescription').value);
    formData.append('category', document.getElementById('editItemCategory').value);
    formData.append('price', document.getElementById('editItemPrice').value);
    formData.append('availability', document.getElementById('editItemAvailability').value);

    const imageField = document.getElementById('editItemImage');
    if (imageField.files.length > 0) {
        formData.append('image', imageField.files[0]);
    }

    // Retrieve item ID
    const id = document.getElementById('saveEdit').value;

    try {
        // Send PUT request
        const response = await fetch(`http://127.0.0.1:8000/api/menu/items/${id}/`, {
            method: 'PUT',
            headers: {
                'Authorization': `JWT ${jwtToken}`
                // Content-Type is not set because FormData handles it
            },
            body: formData
        });

        // Check for HTTP errors
        if (!response.ok) {
            const errorResponse = await response.text();
            throw new Error(`HTTP ${response.status}: ${errorResponse}`);
        }

        // Parse JSON response
        const data = await response.json();
        console.log(data);

        // Update UI
        $('#editModal').modal('hide');
        // Reset the form
        document.getElementById('editItemImage').value = ''; // Clear the file input
        document.getElementById('uploadedItemImage').src = ''; // Clear the image preview
        document.getElementById('uploadedItemImage').style.display = 'none'; // Hide the image preview

        $('#menuTable').DataTable().destroy(); // Destroy DataTable to refresh
        fetchDataFromAPI(); // Fetch updated data
    } catch (error) {
        console.error('Error updating item:', error);
    }
});




// Function to create carousel items
function createCarouselItems(items) {
    const carousel = document.getElementById('food-carousel');
    carousel.innerHTML = ''; // Clear existing items

    items.forEach((item, index) => {
        const listItem = document.createElement('li');
        listItem.classList.add('swiper-slide', 'card', 'card-slide');
        listItem.setAttribute('data-aos', 'fade-up');
        listItem.setAttribute('data-aos-delay', item.delay);

        listItem.style.backgroundImage = `url(${item.image})`;
        listItem.style.backgroundSize = 'cover';
        listItem.style.backgroundPosition = 'center';
        listItem.style.height = '300px';

        const cardBody = document.createElement('div');
        cardBody.classList.add('card-body', 'd-flex', 'flex-column', 'justify-content-end');

        const progressDetail = document.createElement('div');
        progressDetail.classList.add('progress-detail', 'mt-3', 'text-white');

        const itemName = document.createElement('p');
        itemName.classList.add('mb-2', 'text-dark');
        itemName.textContent = item.name;

        const itemDescription = document.createElement('p');
        itemDescription.classList.add('text-dark');
        itemDescription.textContent = item.description;

        progressDetail.appendChild(itemName);
        progressDetail.appendChild(itemDescription);
        cardBody.appendChild(progressDetail);
        listItem.appendChild(cardBody);
        carousel.appendChild(listItem);

        // Add fading effect
        setTimeout(() => {
            listItem.classList.add('visible');
        }, 100); // Adjust timing if needed
    });


    // Initialize Swiper after populating the carousel
    new Swiper('.d-slider1', {
        loop: true,
        autoplay: {
            delay: 3000,
        },
        speed: 800,
        spaceBetween: 10,
        slidesPerView: 1,
    });
}

// Call the function to fetch data and initialize the table and carousel
fetchDataFromAPI();
