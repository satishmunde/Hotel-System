




    var swiper = new Swiper('.d-slider1', {
        loop: true,
        autoplay: {
            delay: 1000, // 1000ms = 1 second
        },
        speed: 800,
        spaceBetween: 10,
    });

    const staticData = [
        {
            clientImage: '/static/ui-assets/images/faces/face1.jpg',
            clientName: 'Henry Klein',
            orderNo: '02312',
            productCost: '$14,500',
            project: 'Dashboard',
            paymentMode: 'Credit card',
            startDate: '04 Dec 2019',
            paymentStatus: 'Approved'
        },
        {
            clientImage: '/static/ui-assets/images/faces/face2.jpg',
            clientName: 'Estella Bryan',
            orderNo: '02313',
            productCost: '$12,300',
            project: 'Website',
            paymentMode: 'Cash on delivered',
            startDate: '05 Dec 2019',
            paymentStatus: 'Approved'
        },
        {
            clientImage: '/static/ui-assets/images/faces/face5.jpg',
            clientName: 'Lucy Abbott',
            orderNo: '02314',
            productCost: '$18,000',
            project: 'App design',
            paymentMode: 'Credit card',
            startDate: '06 Dec 2019',
            paymentStatus: 'Rejected'
        },
        {
            clientImage: '/static/ui-assets/images/faces/face3.jpg',
            clientName: 'Peter Gill',
            orderNo: '02315',
            productCost: '$15,500',
            project: 'Development',
            paymentMode: 'Online Payment',
            startDate: '07 Dec 2019',
            paymentStatus: 'Approved'
        },
        {
            clientImage: '/static/ui-assets/images/faces/face4.jpg',
            clientName: 'Sallie Reyes',
            orderNo: '02316',
            productCost: '$13,200',
            project: 'Website',
            paymentMode: 'Credit card',
            startDate: '08 Dec 2019',
            paymentStatus: 'Approved'
        },
        {
            clientImage: '/static/ui-assets/images/faces/face1.jpg',
            clientName: 'Henry Klein',
            orderNo: '02312',
            productCost: '$14,500',
            project: 'Dashboard',
            paymentMode: 'Credit card',
            startDate: '04 Dec 2019',
            paymentStatus: 'Approved'
        },
        {
            clientImage: '/static/ui-assets/images/faces/face2.jpg',
            clientName: 'Estella Bryan',
            orderNo: '02313',
            productCost: '$12,300',
            project: 'Website',
            paymentMode: 'Cash on delivered',
            startDate: '05 Dec 2019',
            paymentStatus: 'Approved'
        },
        {
            clientImage: '/static/ui-assets/images/faces/face5.jpg',
            clientName: 'Lucy Abbott',
            orderNo: '02314',
            productCost: '$18,000',
            project: 'App design',
            paymentMode: 'Credit card',
            startDate: '06 Dec 2019',
            paymentStatus: 'Rejected'
        },
        {
            clientImage: '/static/ui-assets/images/faces/face3.jpg',
            clientName: 'Peter Gill',
            orderNo: '02315',
            productCost: '$15,500',
            project: 'Development',
            paymentMode: 'Online Payment',
            startDate: '07 Dec 2019',
            paymentStatus: 'Approved'
        },
        {
            clientImage: '/static/ui-assets/images/faces/face4.jpg',
            clientName: 'Sallie Reyes',
            orderNo: '02316',
            productCost: '$13,200',
            project: 'Website',
            paymentMode: 'Credit card',
            startDate: '08 Dec 2019',
            paymentStatus: 'Approved'
        },
        {
            clientImage: '/static/ui-assets/images/faces/face1.jpg',
            clientName: 'Henry Klein',
            orderNo: '02312',
            productCost: '$14,500',
            project: 'Dashboard',
            paymentMode: 'Credit card',
            startDate: '04 Dec 2019',
            paymentStatus: 'Approved'
        },
        {
            clientImage: '/static/ui-assets/images/faces/face2.jpg',
            clientName: 'Estella Bryan',
            orderNo: '02313',
            productCost: '$12,300',
            project: 'Website',
            paymentMode: 'Cash on delivered',
            startDate: '05 Dec 2019',
            paymentStatus: 'Approved'
        },
        {
            clientImage: '/static/ui-assets/images/faces/face5.jpg',
            clientName: 'Lucy Abbott',
            orderNo: '02314',
            productCost: '$18,000',
            project: 'App design',
            paymentMode: 'Credit card',
            startDate: '06 Dec 2019',
            paymentStatus: 'Rejected'
        },
        {
            clientImage: '/static/ui-assets/images/faces/face3.jpg',
            clientName: 'Peter Gill',
            orderNo: '02315',
            productCost: '$15,500',
            project: 'Development',
            paymentMode: 'Online Payment',
            startDate: '07 Dec 2019',
            paymentStatus: 'Approved'
        },
        {
            clientImage: '/static/ui-assets/images/faces/face4.jpg',
            clientName: 'Sallie Reyes',
            orderNo: '02316',
            productCost: '$13,200',
            project: 'Website',
            paymentMode: 'Credit card',
            startDate: '08 Dec 2019',
            paymentStatus: 'Approved'
        },
        {
            clientImage: '/static/ui-assets/images/faces/face1.jpg',
            clientName: 'Henry Klein',
            orderNo: '02312',
            productCost: '$14,500',
            project: 'Dashboard',
            paymentMode: 'Credit card',
            startDate: '04 Dec 2019',
            paymentStatus: 'Approved'
        },
        {
            clientImage: '/static/ui-assets/images/faces/face2.jpg',
            clientName: 'Estella Bryan',
            orderNo: '02313',
            productCost: '$12,300',
            project: 'Website',
            paymentMode: 'Cash on delivered',
            startDate: '05 Dec 2019',
            paymentStatus: 'Approved'
        },
        {
            clientImage: '/static/ui-assets/images/faces/face5.jpg',
            clientName: 'Lucy Abbott',
            orderNo: '02314',
            productCost: '$18,000',
            project: 'App design',
            paymentMode: 'Credit card',
            startDate: '06 Dec 2019',
            paymentStatus: 'Rejected'
        },
        {
            clientImage: '/static/ui-assets/images/faces/face3.jpg',
            clientName: 'Peter Gill',
            orderNo: '02315',
            productCost: '$15,500',
            project: 'Development',
            paymentMode: 'Online Payment',
            startDate: '07 Dec 2019',
            paymentStatus: 'Approved'
        },
        {
            clientImage: '/static/ui-assets/images/faces/face4.jpg',
            clientName: 'Sallie Reyes',
            orderNo: '02316',
            productCost: '$13,200',
            project: 'Website',
            paymentMode: 'Credit card',
            startDate: '08 Dec 2019',
            paymentStatus: 'Approved'
        },
        {
            clientImage: '/static/ui-assets/images/faces/face1.jpg',
            clientName: 'Henry Klein',
            orderNo: '02312',
            productCost: '$14,500',
            project: 'Dashboard',
            paymentMode: 'Credit card',
            startDate: '04 Dec 2019',
            paymentStatus: 'Approved'
        },
        {
            clientImage: '/static/ui-assets/images/faces/face2.jpg',
            clientName: 'Estella Bryan',
            orderNo: '02313',
            productCost: '$12,300',
            project: 'Website',
            paymentMode: 'Cash on delivered',
            startDate: '05 Dec 2019',
            paymentStatus: 'Approved'
        },
        {
            clientImage: '/static/ui-assets/images/faces/face5.jpg',
            clientName: 'Lucy Abbott',
            orderNo: '02314',
            productCost: '$18,000',
            project: 'App design',
            paymentMode: 'Credit card',
            startDate: '06 Dec 2019',
            paymentStatus: 'Rejected'
        },
        {
            clientImage: '/static/ui-assets/images/faces/face3.jpg',
            clientName: 'Peter Gill',
            orderNo: '02315',
            productCost: '$15,500',
            project: 'Development',
            paymentMode: 'Online Payment',
            startDate: '07 Dec 2019',
            paymentStatus: 'Approved'
        },
        {
            clientImage: '/static/ui-assets/images/faces/face4.jpg',
            clientName: 'Sallie Reyes',
            orderNo: '02316',
            productCost: '$13,200',
            project: 'Website',
            paymentMode: 'Credit card',
            startDate: '08 Dec 2019',
            paymentStatus: 'Approved'
        },
        {
            clientImage: '/static/ui-assets/images/faces/face1.jpg',
            clientName: 'Henry Klein',
            orderNo: '02312',
            productCost: '$14,500',
            project: 'Dashboard',
            paymentMode: 'Credit card',
            startDate: '04 Dec 2019',
            paymentStatus: 'Approved'
        },
        {
            clientImage: '/static/ui-assets/images/faces/face2.jpg',
            clientName: 'Estella Bryan',
            orderNo: '02313',
            productCost: '$12,300',
            project: 'Website',
            paymentMode: 'Cash on delivered',
            startDate: '05 Dec 2019',
            paymentStatus: 'Approved'
        },
        {
            clientImage: '/static/ui-assets/images/faces/face5.jpg',
            clientName: 'Lucy Abbott',
            orderNo: '02314',
            productCost: '$18,000',
            project: 'App design',
            paymentMode: 'Credit card',
            startDate: '06 Dec 2019',
            paymentStatus: 'Rejected'
        },
        {
            clientImage: '/static/ui-assets/images/faces/face3.jpg',
            clientName: 'Peter Gill',
            orderNo: '02315',
            productCost: '$15,500',
            project: 'Development',
            paymentMode: 'Online Payment',
            startDate: '07 Dec 2019',
            paymentStatus: 'Approved'
        },
        {
            clientImage: '/static/ui-assets/images/faces/face4.jpg',
            clientName: 'Sallie Reyes',
            orderNo: '02316',
            productCost: '$13,200',
            project: 'Website',
            paymentMode: 'Credit card',
            startDate: '08 Dec 2019',
            paymentStatus: 'Approved'
        },
        {
            clientImage: '/static/ui-assets/images/faces/face1.jpg',
            clientName: 'Henry Klein',
            orderNo: '02312',
            productCost: '$14,500',
            project: 'Dashboard',
            paymentMode: 'Credit card',
            startDate: '04 Dec 2019',
            paymentStatus: 'Approved'
        },
        {
            clientImage: '/static/ui-assets/images/faces/face2.jpg',
            clientName: 'Estella Bryan',
            orderNo: '02313',
            productCost: '$12,300',
            project: 'Website',
            paymentMode: 'Cash on delivered',
            startDate: '05 Dec 2019',
            paymentStatus: 'Approved'
        },
        {
            clientImage: '/static/ui-assets/images/faces/face5.jpg',
            clientName: 'Lucy Abbott',
            orderNo: '02314',
            productCost: '$18,000',
            project: 'App design',
            paymentMode: 'Credit card',
            startDate: '06 Dec 2019',
            paymentStatus: 'Rejected'
        },
        {
            clientImage: '/static/ui-assets/images/faces/face3.jpg',
            clientName: 'Peter Gill',
            orderNo: '02315',
            productCost: '$15,500',
            project: 'Development',
            paymentMode: 'Online Payment',
            startDate: '07 Dec 2019',
            paymentStatus: 'Approved'
        },
        {
            clientImage: '/static/ui-assets/images/faces/face4.jpg',
            clientName: 'Sallie Reyes',
            orderNo: '02316',
            productCost: '$13,200',
            project: 'Website',
            paymentMode: 'Credit card',
            startDate: '08 Dec 2019',
            paymentStatus: 'Approved'
        }
    ];

    const tableBody = document.getElementById('orderTableBody');
    const selectAllCheckbox = document.getElementById('selectAll');

    // Static data


    function populateTable(data) {
        tableBody.innerHTML = ''; // Clear existing rows

        data.forEach(order => {
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
    <img src="${order.clientImage}" alt="image" class="rounded-circle" style="width: 40px; height: 40px; object-fit: cover;" />
    <span class="pl-2" style="flex-grow: 1; margin-left: 10px;">${order.clientName}</span>
</td>

                <td>${order.orderNo}</td>
                <td>${order.productCost}</td>
                <td>${order.project}</td>
                <td>${order.paymentMode}</td>
                <td>${order.startDate}</td>
                <td>
                    <div class="badge badge-outline-${order.paymentStatus === 'Approved' ? 'success' : order.paymentStatus === 'Pending' ? 'warning' : 'danger'}">
                        ${order.paymentStatus}
                    </div>
                </td>
            `;
            tableBody.appendChild(row);
        });
        var table = $('#orderTable').DataTable({
            "paging": true,
            "lengthChange": false,
            "searching": true,
            "ordering": true,
            "info": true,
            "autoWidth": false,
            "responsive": true,
            "columnDefs": [
                { "orderable": false, "targets": 0 },  // Disable ordering for the checkbox column
                { "orderable": false, "targets": 1 }   // Disable ordering for the client image and name column
            ]
        });
    
        // Apply individual column search
        $('#orderTable thead tr:eq(1) th').each(function(i) {
            var title = $(this).text();
            $('input', this).on('keyup change', function() {
                if (table.column(i).search() !== this.value) {
                    table
                        .column(i)
                        .search(this.value)
                        .draw();
                }
            });
        });
    

        // Add event listeners for row selection
        document.querySelectorAll('.row-checkbox').forEach(checkbox => {
            checkbox.addEventListener('change', function() {
                if (this.checked) {
                    this.closest('tr').classList.add('selected');
                } else {
                    this.closest('tr').classList.remove('selected');
                }
            });
        });

        // Select/Deselect all rows
        selectAllCheckbox.addEventListener('change', function() {
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

    // Populate table with static data
    populateTable(staticData);

// document.addEventListener('DOMContentLoaded', function() {
//     const tableBody = document.getElementById('orderTableBody');
//     const selectAllCheckbox = document.getElementById('selectAll');

//     // Fetch data from API
//     fetch('https://api.example.com/orders') // Replace with your API endpoint
//         .then(response => response.json())
//         .then(data => {
//             populateTable(data);
//         })
//         .catch(error => console.error('Error fetching data:', error));

//     function populateTable(data) {
//         tableBody.innerHTML = ''; // Clear existing rows

//         data.forEach(order => {
//             const row = document.createElement('tr');
//             row.innerHTML = `
//                 <td>
//                     <div class="form-check form-check-muted m-0">
//                         <label class="form-check-label">
//                             <input type="checkbox" class="form-check-input row-checkbox" />
//                         </label>
//                     </div>
//                 </td>
//                 <td>
//                     <img src="${order.clientImage}" alt="image" class="rounded-circle" width="40" height="40" />
//                     <span class="pl-2">${order.clientName}</span>
//                 </td>
//                 <td>${order.orderNo}</td>
//                 <td>${order.productCost}</td>
//                 <td>${order.project}</td>
//                 <td>${order.paymentMode}</td>
//                 <td>${order.startDate}</td>
//                 <td>
//                     <div class="badge badge-outline-${order.paymentStatus === 'Approved' ? 'success' : order.paymentStatus === 'Pending' ? 'warning' : 'danger'}">
//                         ${order.paymentStatus}
//                     </div>
//                 </td>
//             `;
//             tableBody.appendChild(row);
//         });

//         // Add event listeners for row selection
//         document.querySelectorAll('.row-checkbox').forEach(checkbox => {
//             checkbox.addEventListener('change', function() {
//                 if (this.checked) {
//                     this.closest('tr').classList.add('selected');
//                 } else {
//                     this.closest('tr').classList.remove('selected');
//                 }
//             });
//         });

//         // Select/Deselect all rows
//         selectAllCheckbox.addEventListener('change', function() {
//             const isChecked = this.checked;
//             document.querySelectorAll('.row-checkbox').forEach(checkbox => {
//                 checkbox.checked = isChecked;
//                 if (isChecked) {
//                     checkbox.closest('tr').classList.add('selected');
//                 } else {
//                     checkbox.closest('tr').classList.remove('selected');
//                 }
//             });
//         });
//     }
// });


